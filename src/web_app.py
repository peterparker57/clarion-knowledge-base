"""
FastAPI Web Application for Clarion Knowledge Base
Provides REST API endpoints for semantic search, RAG queries, and documentation access
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
import logging
from contextlib import asynccontextmanager
import os
import json
import time
import tarfile
import shutil
import requests
from abc import ABC, abstractmethod
from cryptography.fernet import Fernet
from pathlib import Path

from vector_store import ClarionVectorStore
from embeddings import EmbeddingModel

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global instances (loaded at startup)
vector_store: Optional[ClarionVectorStore] = None
embedding_model: Optional[EmbeddingModel] = None

# Global state for API keys (in-memory storage)
api_keys: Dict[str, str] = {}

# Encryption key for API keys (generate or load from env)
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')
if not ENCRYPTION_KEY:
    # Generate a key if not provided (will be different each restart in production)
    ENCRYPTION_KEY = Fernet.generate_key().decode()
    logger.warning("No ENCRYPTION_KEY in environment, generated temporary key")

fernet = Fernet(ENCRYPTION_KEY.encode() if isinstance(ENCRYPTION_KEY, str) else ENCRYPTION_KEY)


# ============================================================================
# LLM Provider Layer (Inline Implementation)
# ============================================================================

class LLMProvider(ABC):
    """Abstract base class for LLM providers."""

    @abstractmethod
    def query(self, context: str, question: str, **kwargs) -> dict:
        """
        Query the LLM with context and question.

        Args:
            context: Retrieved documentation chunks
            question: User's question
            **kwargs: Provider-specific options

        Returns:
            {
                "answer": str,
                "model": str,
                "tokens_used": int,
                "cost_estimate": float
            }
        """
        pass


class DeepseekProvider(LLMProvider):
    """Deepseek API provider."""

    def __init__(self, api_key: str, model: str = "deepseek-chat"):
        self.api_key = api_key
        self.model = model
        self.base_url = "https://api.deepseek.com/v1"

    def query(self, context: str, question: str, mode: str = "augmented", **kwargs) -> dict:
        """Query Deepseek API."""
        import requests

        prompt = self._build_prompt(context, question, mode)

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful Clarion programming assistant."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.3,
            "max_tokens": 2000
        }

        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload,
                timeout=300  # 5 minutes for complex documentation queries
            )
            response.raise_for_status()
            data = response.json()

            answer = data['choices'][0]['message']['content']
            usage = data.get('usage', {})
            prompt_tokens = usage.get('prompt_tokens', 0)
            completion_tokens = usage.get('completion_tokens', 0)
            tokens_used = usage.get('total_tokens', prompt_tokens + completion_tokens)

            # Deepseek pricing (2025): V3.2-Exp (cache miss pricing)
            # Input: $0.28/1M, Output: $0.42/1M
            cost_estimate = (prompt_tokens / 1_000_000 * 0.28) + (completion_tokens / 1_000_000 * 0.42)

            return {
                "answer": answer,
                "model": self.model,
                "tokens_used": tokens_used,
                "cost_estimate": cost_estimate
            }

        except requests.exceptions.Timeout:
            logger.error("Deepseek API timeout - request took longer than 5 minutes")
            raise HTTPException(
                status_code=504,
                detail="Query timed out after 5 minutes. Try using 'Chat' mode (faster, no doc search) or ask a more specific question."
            )
        except requests.exceptions.RequestException as e:
            logger.error(f"Deepseek API error: {e}")
            raise HTTPException(
                status_code=503,
                detail=f"AI provider error: {str(e)}. Please check your API key and try again."
            )

    def _build_augmented_prompt(self, context: str, question: str) -> str:
        """Prompt for augmented mode - uses docs + LLM knowledge."""
        return f"""You are an expert Clarion programming assistant with access to official documentation.

AVAILABLE DOCUMENTATION:
{context if context and context.strip() else "No specific documentation found for this query."}

USER QUESTION:
{question}

INSTRUCTIONS:
1. You are a Clarion expert - use your comprehensive knowledge to provide helpful answers
2. When the documentation above is relevant, cite and reference it (include source names)
3. You may supplement documentation with your general Clarion programming knowledge
4. Generate practical code examples even if not explicitly in the documentation
5. If documentation contradicts your knowledge, prefer the documentation and note the discrepancy
6. Use proper Clarion syntax and best practices
7. Clearly indicate when you're using documentation vs your expert knowledge

FORMAT YOUR ANSWER:
- Start with a direct answer to the question
- Include working code examples where applicable
- Cite documentation sources when used (e.g., "According to the Language Reference...")
- Add helpful context and best practices

Provide a comprehensive, helpful answer:"""

    def _build_strict_prompt(self, context: str, question: str) -> str:
        """Prompt for strict mode - docs only (current behavior)."""
        return f"""You are a helpful Clarion programming assistant. Answer the user's question based ONLY on the provided documentation context.

CONTEXT FROM CLARION DOCUMENTATION:
{context}

USER QUESTION:
{question}

INSTRUCTIONS:
1. Answer based solely on the provided context
2. If the context doesn't contain the answer, say so clearly
3. Include relevant code examples from the context
4. Cite which manual/section the information comes from
5. Format Clarion code with proper indentation
6. Do NOT use external knowledge - stick to the documentation provided

ANSWER:"""

    def _build_chat_prompt(self, question: str) -> str:
        """Prompt for chat mode - no docs, pure LLM."""
        return f"""You are an expert Clarion programming assistant.

USER QUESTION:
{question}

INSTRUCTIONS:
1. Provide a helpful, accurate answer using your Clarion programming expertise
2. Include practical code examples where applicable
3. Use proper Clarion syntax and conventions
4. Explain concepts clearly and concisely
5. Note: You don't have access to documentation for this query, but use your expert knowledge

Provide a helpful answer:"""

    def _build_prompt(self, context: str, question: str, mode: str = "augmented") -> str:
        """Build the prompt based on query mode."""
        if mode == "strict":
            return self._build_strict_prompt(context, question)
        elif mode == "chat":
            return self._build_chat_prompt(question)
        else:  # augmented
            return self._build_augmented_prompt(context, question)


class OllamaProvider(LLMProvider):
    """Ollama local provider."""

    def __init__(self, model: str = "llama3", base_url: str = "http://ollama:11434"):
        self.model = model
        self.base_url = base_url

    def query(self, context: str, question: str, mode: str = "augmented", **kwargs) -> dict:
        """Query Ollama API."""
        import requests

        prompt = self._build_prompt(context, question, mode)

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                timeout=300  # 5 minutes for local models
            )
            response.raise_for_status()
            data = response.json()

            answer = data.get('response', '')

            # Estimate tokens (rough approximation)
            tokens_used = len(prompt.split()) + len(answer.split())

            return {
                "answer": answer,
                "model": self.model,
                "tokens_used": tokens_used,
                "cost_estimate": 0.0  # Free for local
            }

        except requests.exceptions.Timeout:
            logger.error("Ollama API timeout - request took longer than 5 minutes")
            raise HTTPException(
                status_code=504,
                detail="Ollama timed out after 5 minutes. Try using 'Chat' mode (faster) or a smaller/faster model."
            )
        except requests.exceptions.RequestException as e:
            logger.error(f"Ollama API error: {e}")
            raise HTTPException(
                status_code=503,
                detail=f"Ollama API error: {str(e)}. Is Ollama running? Check 'docker ps' to verify the ollama container is up."
            )

    def _build_augmented_prompt(self, context: str, question: str) -> str:
        """Prompt for augmented mode - uses docs + LLM knowledge."""
        return f"""You are an expert Clarion programming assistant with access to official documentation.

AVAILABLE DOCUMENTATION:
{context if context and context.strip() else "No specific documentation found for this query."}

USER QUESTION:
{question}

INSTRUCTIONS:
1. You are a Clarion expert - use your comprehensive knowledge to provide helpful answers
2. When the documentation above is relevant, cite and reference it (include source names)
3. You may supplement documentation with your general Clarion programming knowledge
4. Generate practical code examples even if not explicitly in the documentation
5. If documentation contradicts your knowledge, prefer the documentation and note the discrepancy
6. Use proper Clarion syntax and best practices
7. Clearly indicate when you're using documentation vs your expert knowledge

FORMAT YOUR ANSWER:
- Start with a direct answer to the question
- Include working code examples where applicable
- Cite documentation sources when used (e.g., "According to the Language Reference...")
- Add helpful context and best practices

Provide a comprehensive, helpful answer:"""

    def _build_strict_prompt(self, context: str, question: str) -> str:
        """Prompt for strict mode - docs only (current behavior)."""
        return f"""You are a helpful Clarion programming assistant. Answer the user's question based ONLY on the provided documentation context.

CONTEXT FROM CLARION DOCUMENTATION:
{context}

USER QUESTION:
{question}

INSTRUCTIONS:
1. Answer based solely on the provided context
2. If the context doesn't contain the answer, say so clearly
3. Include relevant code examples from the context
4. Cite which manual/section the information comes from
5. Format Clarion code with proper indentation
6. Do NOT use external knowledge - stick to the documentation provided

ANSWER:"""

    def _build_chat_prompt(self, question: str) -> str:
        """Prompt for chat mode - no docs, pure LLM."""
        return f"""You are an expert Clarion programming assistant.

USER QUESTION:
{question}

INSTRUCTIONS:
1. Provide a helpful, accurate answer using your Clarion programming expertise
2. Include practical code examples where applicable
3. Use proper Clarion syntax and conventions
4. Explain concepts clearly and concisely
5. Note: You don't have access to documentation for this query, but use your expert knowledge

Provide a helpful answer:"""

    def _build_prompt(self, context: str, question: str, mode: str = "augmented") -> str:
        """Build the prompt based on query mode."""
        if mode == "strict":
            return self._build_strict_prompt(context, question)
        elif mode == "chat":
            return self._build_chat_prompt(question)
        else:  # augmented
            return self._build_augmented_prompt(context, question)


class OpenAIProvider(LLMProvider):
    """OpenAI API provider."""

    def __init__(self, api_key: str, model: str = "gpt-4-turbo-preview"):
        self.api_key = api_key
        self.model = model
        self.base_url = "https://api.openai.com/v1"

    def query(self, context: str, question: str, mode: str = "augmented", **kwargs) -> dict:
        """Query OpenAI API."""
        import requests

        prompt = self._build_prompt(context, question, mode)

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful Clarion programming assistant."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.3,
            "max_tokens": 2000
        }

        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload,
                timeout=300  # 5 minutes for complex documentation queries
            )
            response.raise_for_status()
            data = response.json()

            answer = data['choices'][0]['message']['content']
            usage = data.get('usage', {})
            prompt_tokens = usage.get('prompt_tokens', 0)
            completion_tokens = usage.get('completion_tokens', 0)
            total_tokens = usage.get('total_tokens', 0)

            # OpenAI pricing varies by model (2025 pricing)
            if self.model == 'gpt-5':
                # GPT-5: $1.25/1M input, $10/1M output
                cost_estimate = (prompt_tokens / 1_000_000 * 1.25) + (completion_tokens / 1_000_000 * 10)
            elif 'gpt-4o' in self.model:
                if 'mini' in self.model:
                    # GPT-4o Mini: $0.15/1M input, $0.60/1M output
                    cost_estimate = (prompt_tokens / 1_000_000 * 0.15) + (completion_tokens / 1_000_000 * 0.60)
                else:
                    # GPT-4o: $2.50/1M input, $10/1M output (corrected)
                    cost_estimate = (prompt_tokens / 1_000_000 * 2.50) + (completion_tokens / 1_000_000 * 10)
            elif self.model == 'o1':
                # o1 reasoning model: $15/1M input, $60/1M output
                cost_estimate = (prompt_tokens / 1_000_000 * 15) + (completion_tokens / 1_000_000 * 60)
            elif self.model in ['o3-mini', 'o1-mini']:
                # o3-mini / o1-mini: $1.10/1M input, $4.40/1M output
                cost_estimate = (prompt_tokens / 1_000_000 * 1.10) + (completion_tokens / 1_000_000 * 4.40)
            elif 'gpt-4-turbo' in self.model or 'gpt-4' in self.model:
                # GPT-4 Turbo: $10/1M input, $30/1M output
                cost_estimate = (prompt_tokens / 1_000_000 * 10) + (completion_tokens / 1_000_000 * 30)
            elif 'gpt-3.5' in self.model:
                # GPT-3.5 Turbo: $0.50/1M input, $1.50/1M output
                cost_estimate = (prompt_tokens / 1_000_000 * 0.5) + (completion_tokens / 1_000_000 * 1.5)
            else:
                # Default estimate for unknown models
                cost_estimate = (prompt_tokens / 1_000_000 * 2.5) + (completion_tokens / 1_000_000 * 10)

            return {
                "answer": answer,
                "model": self.model,
                "tokens_used": total_tokens,
                "cost_estimate": cost_estimate
            }

        except requests.exceptions.Timeout:
            logger.error("OpenAI API timeout - request took longer than 5 minutes")
            raise HTTPException(status_code=504, detail="OpenAI timed out after 5 minutes. Try using 'Chat' mode (faster) or ask a more specific question.")
        except requests.exceptions.RequestException as e:
            logger.error(f"OpenAI API error: {e}")
            raise HTTPException(status_code=503, detail=f"OpenAI error: {str(e)}")

    def _build_augmented_prompt(self, context: str, question: str) -> str:
        return f"""You are an expert Clarion programming assistant with access to official documentation.

AVAILABLE DOCUMENTATION:
{context if context and context.strip() else "No specific documentation found for this query."}

USER QUESTION:
{question}

INSTRUCTIONS:
1. You are a Clarion expert - use your comprehensive knowledge to provide helpful answers
2. When the documentation above is relevant, cite and reference it (include source names)
3. You may supplement documentation with your general Clarion programming knowledge
4. Generate practical code examples even if not explicitly in the documentation
5. If documentation contradicts your knowledge, prefer the documentation and note the discrepancy
6. Use proper Clarion syntax and best practices
7. Clearly indicate when you're using documentation vs your expert knowledge

FORMAT YOUR ANSWER:
- Start with a direct answer to the question
- Include working code examples where applicable
- Cite documentation sources when used (e.g., "According to the Language Reference...")
- Add helpful context and best practices

Provide a comprehensive, helpful answer:"""

    def _build_strict_prompt(self, context: str, question: str) -> str:
        return f"""You are a helpful Clarion programming assistant. Answer the user's question based ONLY on the provided documentation context.

CONTEXT FROM CLARION DOCUMENTATION:
{context}

USER QUESTION:
{question}

INSTRUCTIONS:
1. Answer based solely on the provided context
2. If the context doesn't contain the answer, say so clearly
3. Include relevant code examples from the context
4. Cite which manual/section the information comes from
5. Format Clarion code with proper indentation
6. Do NOT use external knowledge - stick to the documentation provided

ANSWER:"""

    def _build_chat_prompt(self, question: str) -> str:
        return f"""You are an expert Clarion programming assistant.

USER QUESTION:
{question}

INSTRUCTIONS:
1. Provide a helpful, accurate answer using your Clarion programming expertise
2. Include practical code examples where applicable
3. Use proper Clarion syntax and conventions
4. Explain concepts clearly and concisely
5. Note: You don't have access to documentation for this query, but use your expert knowledge

Provide a helpful answer:"""

    def _build_prompt(self, context: str, question: str, mode: str = "augmented") -> str:
        if mode == "strict":
            return self._build_strict_prompt(context, question)
        elif mode == "chat":
            return self._build_chat_prompt(question)
        else:
            return self._build_augmented_prompt(context, question)


class AnthropicProvider(LLMProvider):
    """Anthropic Claude API provider."""

    def __init__(self, api_key: str, model: str = "claude-3-5-sonnet-20241022"):
        self.api_key = api_key
        self.model = model
        self.base_url = "https://api.anthropic.com/v1"

    def query(self, context: str, question: str, mode: str = "augmented", **kwargs) -> dict:
        """Query Anthropic API."""
        import requests

        prompt = self._build_prompt(context, question, mode)

        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "max_tokens": 2000,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        try:
            response = requests.post(
                f"{self.base_url}/messages",
                headers=headers,
                json=payload,
                timeout=300  # 5 minutes for complex documentation queries
            )
            response.raise_for_status()
            data = response.json()

            answer = data['content'][0]['text']
            usage = data.get('usage', {})
            input_tokens = usage.get('input_tokens', 0)
            output_tokens = usage.get('output_tokens', 0)
            total_tokens = input_tokens + output_tokens

            # Anthropic pricing (2025)
            if 'opus-4-1' in self.model:
                # Claude Opus 4.1: $15/1M input, $75/1M output (corrected)
                cost_estimate = (input_tokens / 1_000_000 * 15) + (output_tokens / 1_000_000 * 75)
            elif 'opus-4' in self.model or 'opus' in self.model:
                # Claude Opus 4: $15/1M input, $75/1M output
                cost_estimate = (input_tokens / 1_000_000 * 15) + (output_tokens / 1_000_000 * 75)
            elif 'sonnet' in self.model:
                # Claude Sonnet 4.5/4: $3/1M input, $15/1M output
                cost_estimate = (input_tokens / 1_000_000 * 3) + (output_tokens / 1_000_000 * 15)
            elif 'haiku-3-5' in self.model or 'haiku-3.5' in self.model:
                # Claude Haiku 3.5: $0.80/1M input, $4.00/1M output (corrected)
                cost_estimate = (input_tokens / 1_000_000 * 0.80) + (output_tokens / 1_000_000 * 4.00)
            elif 'haiku' in self.model:
                # Claude Haiku 3 (older): $0.25/1M input, $1.25/1M output
                cost_estimate = (input_tokens / 1_000_000 * 0.25) + (output_tokens / 1_000_000 * 1.25)
            else:
                # Default estimate
                cost_estimate = (input_tokens / 1_000_000 * 3) + (output_tokens / 1_000_000 * 15)

            return {
                "answer": answer,
                "model": self.model,
                "tokens_used": total_tokens,
                "cost_estimate": cost_estimate
            }

        except requests.exceptions.Timeout:
            logger.error("Anthropic API timeout - request took longer than 5 minutes")
            raise HTTPException(status_code=504, detail="Anthropic timed out after 5 minutes. Try using 'Chat' mode (faster) or ask a more specific question.")
        except requests.exceptions.RequestException as e:
            logger.error(f"Anthropic API error: {e}")
            raise HTTPException(status_code=503, detail=f"Anthropic error: {str(e)}")

    def _build_augmented_prompt(self, context: str, question: str) -> str:
        return f"""You are an expert Clarion programming assistant with access to official documentation.

AVAILABLE DOCUMENTATION:
{context if context and context.strip() else "No specific documentation found for this query."}

USER QUESTION:
{question}

INSTRUCTIONS:
1. You are a Clarion expert - use your comprehensive knowledge to provide helpful answers
2. When the documentation above is relevant, cite and reference it (include source names)
3. You may supplement documentation with your general Clarion programming knowledge
4. Generate practical code examples even if not explicitly in the documentation
5. If documentation contradicts your knowledge, prefer the documentation and note the discrepancy
6. Use proper Clarion syntax and best practices
7. Clearly indicate when you're using documentation vs your expert knowledge

FORMAT YOUR ANSWER:
- Start with a direct answer to the question
- Include working code examples where applicable
- Cite documentation sources when used (e.g., "According to the Language Reference...")
- Add helpful context and best practices

Provide a comprehensive, helpful answer:"""

    def _build_strict_prompt(self, context: str, question: str) -> str:
        return f"""You are a helpful Clarion programming assistant. Answer the user's question based ONLY on the provided documentation context.

CONTEXT FROM CLARION DOCUMENTATION:
{context}

USER QUESTION:
{question}

INSTRUCTIONS:
1. Answer based solely on the provided context
2. If the context doesn't contain the answer, say so clearly
3. Include relevant code examples from the context
4. Cite which manual/section the information comes from
5. Format Clarion code with proper indentation
6. Do NOT use external knowledge - stick to the documentation provided

ANSWER:"""

    def _build_chat_prompt(self, question: str) -> str:
        return f"""You are an expert Clarion programming assistant.

USER QUESTION:
{question}

INSTRUCTIONS:
1. Provide a helpful, accurate answer using your Clarion programming expertise
2. Include practical code examples where applicable
3. Use proper Clarion syntax and conventions
4. Explain concepts clearly and concisely
5. Note: You don't have access to documentation for this query, but use your expert knowledge

Provide a helpful answer:"""

    def _build_prompt(self, context: str, question: str, mode: str = "augmented") -> str:
        if mode == "strict":
            return self._build_strict_prompt(context, question)
        elif mode == "chat":
            return self._build_chat_prompt(question)
        else:
            return self._build_augmented_prompt(context, question)


class GeminiProvider(LLMProvider):
    """Google Gemini API provider."""

    def __init__(self, api_key: str, model: str = "gemini-1.5-pro"):
        self.api_key = api_key
        self.model = model
        self.base_url = "https://generativelanguage.googleapis.com/v1beta"

    def query(self, context: str, question: str, mode: str = "augmented", **kwargs) -> dict:
        """Query Google Gemini API."""
        import requests

        prompt = self._build_prompt(context, question, mode)

        payload = {
            "contents": [
                {"parts": [{"text": prompt}]}
            ],
            "generationConfig": {
                "temperature": 0.3,
                "maxOutputTokens": 2000
            }
        }

        try:
            response = requests.post(
                f"{self.base_url}/models/{self.model}:generateContent?key={self.api_key}",
                json=payload,
                timeout=300  # 5 minutes for complex documentation queries
            )
            response.raise_for_status()
            data = response.json()

            answer = data['candidates'][0]['content']['parts'][0]['text']

            # Estimate tokens (Gemini doesn't always return token counts in the same way)
            usage_metadata = data.get('usageMetadata', {})
            prompt_tokens = usage_metadata.get('promptTokenCount', 0)
            completion_tokens = usage_metadata.get('candidatesTokenCount', 0)
            total_tokens = usage_metadata.get('totalTokenCount', prompt_tokens + completion_tokens)

            # Gemini pricing (2025)
            if '2.5-pro' in self.model:
                # Gemini 2.5 Pro: $1.25/1M input, $10/1M output (≤200K tokens)
                cost_estimate = (prompt_tokens / 1_000_000 * 1.25) + (completion_tokens / 1_000_000 * 10)
            elif '2.0-flash-lite' in self.model:
                # Gemini 2.0 Flash Lite: $0.075/1M input, $0.30/1M output
                cost_estimate = (prompt_tokens / 1_000_000 * 0.075) + (completion_tokens / 1_000_000 * 0.30)
            elif '2.0-flash' in self.model:
                # Gemini 2.0 Flash: $0.10/1M input, $0.40/1M output
                cost_estimate = (prompt_tokens / 1_000_000 * 0.10) + (completion_tokens / 1_000_000 * 0.40)
            elif '1.5-pro' in self.model:
                # Gemini 1.5 Pro: $1.25/1M input, $5.00/1M output (≤128K tokens) - corrected
                cost_estimate = (prompt_tokens / 1_000_000 * 1.25) + (completion_tokens / 1_000_000 * 5.00)
            else:
                # Gemini 1.0 Pro: $0.50/1M input, $1.50/1M output
                cost_estimate = (prompt_tokens / 1_000_000 * 0.5) + (completion_tokens / 1_000_000 * 1.5)

            return {
                "answer": answer,
                "model": self.model,
                "tokens_used": total_tokens,
                "cost_estimate": cost_estimate
            }

        except requests.exceptions.Timeout:
            logger.error("Gemini API timeout - request took longer than 5 minutes")
            raise HTTPException(status_code=504, detail="Gemini timed out after 5 minutes. Try using 'Chat' mode (faster) or ask a more specific question.")
        except requests.exceptions.RequestException as e:
            logger.error(f"Gemini API error: {e}")
            raise HTTPException(status_code=503, detail=f"Gemini error: {str(e)}")

    def _build_augmented_prompt(self, context: str, question: str) -> str:
        return f"""You are an expert Clarion programming assistant with access to official documentation.

AVAILABLE DOCUMENTATION:
{context if context and context.strip() else "No specific documentation found for this query."}

USER QUESTION:
{question}

INSTRUCTIONS:
1. You are a Clarion expert - use your comprehensive knowledge to provide helpful answers
2. When the documentation above is relevant, cite and reference it (include source names)
3. You may supplement documentation with your general Clarion programming knowledge
4. Generate practical code examples even if not explicitly in the documentation
5. If documentation contradicts your knowledge, prefer the documentation and note the discrepancy
6. Use proper Clarion syntax and best practices
7. Clearly indicate when you're using documentation vs your expert knowledge

FORMAT YOUR ANSWER:
- Start with a direct answer to the question
- Include working code examples where applicable
- Cite documentation sources when used (e.g., "According to the Language Reference...")
- Add helpful context and best practices

Provide a comprehensive, helpful answer:"""

    def _build_strict_prompt(self, context: str, question: str) -> str:
        return f"""You are a helpful Clarion programming assistant. Answer the user's question based ONLY on the provided documentation context.

CONTEXT FROM CLARION DOCUMENTATION:
{context}

USER QUESTION:
{question}

INSTRUCTIONS:
1. Answer based solely on the provided context
2. If the context doesn't contain the answer, say so clearly
3. Include relevant code examples from the context
4. Cite which manual/section the information comes from
5. Format Clarion code with proper indentation
6. Do NOT use external knowledge - stick to the documentation provided

ANSWER:"""

    def _build_chat_prompt(self, question: str) -> str:
        return f"""You are an expert Clarion programming assistant.

USER QUESTION:
{question}

INSTRUCTIONS:
1. Provide a helpful, accurate answer using your Clarion programming expertise
2. Include practical code examples where applicable
3. Use proper Clarion syntax and conventions
4. Explain concepts clearly and concisely
5. Note: You don't have access to documentation for this query, but use your expert knowledge

Provide a helpful answer:"""

    def _build_prompt(self, context: str, question: str, mode: str = "augmented") -> str:
        if mode == "strict":
            return self._build_strict_prompt(context, question)
        elif mode == "chat":
            return self._build_chat_prompt(question)
        else:
            return self._build_augmented_prompt(context, question)


class GrokProvider(LLMProvider):
    """xAI Grok API provider."""

    def __init__(self, api_key: str, model: str = "grok-beta"):
        self.api_key = api_key
        self.model = model
        self.base_url = "https://api.x.ai/v1"

    def query(self, context: str, question: str, mode: str = "augmented", **kwargs) -> dict:
        """Query xAI Grok API."""
        import requests

        prompt = self._build_prompt(context, question, mode)

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful Clarion programming assistant."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.3,
            "max_tokens": 2000
        }

        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload,
                timeout=300  # 5 minutes for complex documentation queries
            )
            response.raise_for_status()
            data = response.json()

            answer = data['choices'][0]['message']['content']
            usage = data.get('usage', {})
            total_tokens = usage.get('total_tokens', 0)

            # Grok pricing (2025)
            prompt_tokens = usage.get('prompt_tokens', 0)
            completion_tokens = usage.get('completion_tokens', 0)
            if 'grok-4-fast' in self.model:
                # Grok 4 Fast: $0.20/1M input (≤128K), $0.50/1M output (average)
                cost_estimate = (prompt_tokens / 1_000_000 * 0.20) + (completion_tokens / 1_000_000 * 0.50)
            elif 'grok-4' in self.model:
                # Grok 4: $3/1M input, $15/1M output
                cost_estimate = (prompt_tokens / 1_000_000 * 3.00) + (completion_tokens / 1_000_000 * 15.00)
            else:
                # Grok 3: $3/1M input, $15/1M output
                cost_estimate = (prompt_tokens / 1_000_000 * 3.00) + (completion_tokens / 1_000_000 * 15.00)

            return {
                "answer": answer,
                "model": self.model,
                "tokens_used": total_tokens,
                "cost_estimate": cost_estimate
            }

        except requests.exceptions.Timeout:
            logger.error("Grok API timeout - request took longer than 5 minutes")
            raise HTTPException(status_code=504, detail="Grok timed out after 5 minutes. Try using 'Chat' mode (faster) or ask a more specific question.")
        except requests.exceptions.RequestException as e:
            logger.error(f"Grok API error: {e}")
            raise HTTPException(status_code=503, detail=f"Grok error: {str(e)}")

    def _build_augmented_prompt(self, context: str, question: str) -> str:
        return f"""You are an expert Clarion programming assistant with access to official documentation.

AVAILABLE DOCUMENTATION:
{context if context and context.strip() else "No specific documentation found for this query."}

USER QUESTION:
{question}

INSTRUCTIONS:
1. You are a Clarion expert - use your comprehensive knowledge to provide helpful answers
2. When the documentation above is relevant, cite and reference it (include source names)
3. You may supplement documentation with your general Clarion programming knowledge
4. Generate practical code examples even if not explicitly in the documentation
5. If documentation contradicts your knowledge, prefer the documentation and note the discrepancy
6. Use proper Clarion syntax and best practices
7. Clearly indicate when you're using documentation vs your expert knowledge

FORMAT YOUR ANSWER:
- Start with a direct answer to the question
- Include working code examples where applicable
- Cite documentation sources when used (e.g., "According to the Language Reference...")
- Add helpful context and best practices

Provide a comprehensive, helpful answer:"""

    def _build_strict_prompt(self, context: str, question: str) -> str:
        return f"""You are a helpful Clarion programming assistant. Answer the user's question based ONLY on the provided documentation context.

CONTEXT FROM CLARION DOCUMENTATION:
{context}

USER QUESTION:
{question}

INSTRUCTIONS:
1. Answer based solely on the provided context
2. If the context doesn't contain the answer, say so clearly
3. Include relevant code examples from the context
4. Cite which manual/section the information comes from
5. Format Clarion code with proper indentation
6. Do NOT use external knowledge - stick to the documentation provided

ANSWER:"""

    def _build_chat_prompt(self, question: str) -> str:
        return f"""You are an expert Clarion programming assistant.

USER QUESTION:
{question}

INSTRUCTIONS:
1. Provide a helpful, accurate answer using your Clarion programming expertise
2. Include practical code examples where applicable
3. Use proper Clarion syntax and conventions
4. Explain concepts clearly and concisely
5. Note: You don't have access to documentation for this query, but use your expert knowledge

Provide a helpful answer:"""

    def _build_prompt(self, context: str, question: str, mode: str = "augmented") -> str:
        if mode == "strict":
            return self._build_strict_prompt(context, question)
        elif mode == "chat":
            return self._build_chat_prompt(question)
        else:
            return self._build_augmented_prompt(context, question)


def get_llm_provider(provider_id: str, model: Optional[str] = None) -> LLMProvider:
    """
    Get an LLM provider instance.

    Args:
        provider_id: Provider identifier (deepseek, ollama, openai, anthropic, gemini, grok)
        model: Optional model name override

    Returns:
        LLMProvider instance

    Raises:
        HTTPException: If provider not configured or invalid
    """
    global api_keys

    if provider_id == "deepseek":
        if provider_id not in api_keys:
            raise HTTPException(
                status_code=401,
                detail="Deepseek API key not configured. Use POST /api/configure to set it."
            )
        encrypted_key = api_keys[provider_id]
        decrypted_key = fernet.decrypt(encrypted_key.encode()).decode()
        model_name = model or "deepseek-chat"
        return DeepseekProvider(api_key=decrypted_key, model=model_name)

    elif provider_id == "openai":
        if provider_id not in api_keys:
            raise HTTPException(
                status_code=401,
                detail="OpenAI API key not configured. Use POST /api/configure to set it."
            )
        encrypted_key = api_keys[provider_id]
        decrypted_key = fernet.decrypt(encrypted_key.encode()).decode()
        model_name = model or "gpt-4o"  # Updated to GPT-4o as default
        return OpenAIProvider(api_key=decrypted_key, model=model_name)

    elif provider_id == "anthropic":
        if provider_id not in api_keys:
            raise HTTPException(
                status_code=401,
                detail="Anthropic API key not configured. Use POST /api/configure to set it."
            )
        encrypted_key = api_keys[provider_id]
        decrypted_key = fernet.decrypt(encrypted_key.encode()).decode()
        model_name = model or "claude-sonnet-4-5"  # Updated to Sonnet 4.5
        return AnthropicProvider(api_key=decrypted_key, model=model_name)

    elif provider_id == "gemini":
        if provider_id not in api_keys:
            raise HTTPException(
                status_code=401,
                detail="Google Gemini API key not configured. Use POST /api/configure to set it."
            )
        encrypted_key = api_keys[provider_id]
        decrypted_key = fernet.decrypt(encrypted_key.encode()).decode()
        model_name = model or "gemini-2.0-flash"  # Updated to 2.0 Flash
        return GeminiProvider(api_key=decrypted_key, model=model_name)

    elif provider_id == "grok":
        if provider_id not in api_keys:
            raise HTTPException(
                status_code=401,
                detail="Grok API key not configured. Use POST /api/configure to set it."
            )
        encrypted_key = api_keys[provider_id]
        decrypted_key = fernet.decrypt(encrypted_key.encode()).decode()
        model_name = model or "grok-4-fast"  # Updated to Grok 4 Fast
        return GrokProvider(api_key=decrypted_key, model=model_name)

    elif provider_id == "ollama":
        # Ollama doesn't require API key
        model_name = model or "llama3"
        ollama_url = os.getenv('OLLAMA_URL', 'http://localhost:11434')
        return OllamaProvider(model=model_name, base_url=ollama_url)

    else:
        raise HTTPException(
            status_code=400,
            detail=f"Unknown provider: {provider_id}. Available: deepseek, openai, anthropic, gemini, grok, ollama"
        )


# ============================================================================
# Pydantic Models
# ============================================================================

# Existing models (kept unchanged)
class SearchRequest(BaseModel):
    """Request model for semantic search."""
    query: str = Field(..., description="Natural language query about Clarion programming")
    max_results: int = Field(5, ge=1, le=50, description="Maximum number of results to return")
    min_score: float = Field(0.3, ge=0.0, le=1.0, description="Minimum similarity score threshold")
    doc_type: Optional[str] = Field(None, description="Filter by document type")

    class Config:
        json_schema_extra = {
            "example": {
                "query": "How do I define a QUEUE in Clarion?",
                "max_results": 5,
                "min_score": 0.3,
                "doc_type": "core_language"
            }
        }


class SearchResult(BaseModel):
    """Single search result."""
    text: str = Field(..., description="Content of the documentation chunk")
    score: float = Field(..., description="Similarity score (0.0 to 1.0)")
    metadata: Dict[str, Any] = Field(..., description="Metadata about the chunk")
    id: str = Field(..., description="Unique identifier for the chunk")


class SearchResponse(BaseModel):
    """Response model for semantic search."""
    query: str = Field(..., description="Original query")
    results: List[SearchResult] = Field(..., description="List of search results")
    total_results: int = Field(..., description="Number of results returned")

    class Config:
        json_schema_extra = {
            "example": {
                "query": "How do I define a QUEUE in Clarion?",
                "results": [
                    {
                        "text": "QUEUE is a structured data type...",
                        "score": 0.85,
                        "metadata": {
                            "source": "Language Reference",
                            "doc_type": "core_language",
                            "chunk_index": 0,
                            "chunk_count": 10
                        },
                        "id": "abc-123-def"
                    }
                ],
                "total_results": 1
            }
        }


class CollectionInfo(BaseModel):
    """Information about the vector store collection."""
    name: str = Field(..., description="Name of the collection")
    vectors_count: int = Field(..., description="Number of vectors in the collection")
    points_count: int = Field(..., description="Number of points in the collection")
    status: str = Field(..., description="Status of the collection")


class HealthResponse(BaseModel):
    """Health check response."""
    status: str = Field(..., description="Health status")
    vector_store: str = Field(..., description="Vector store status")
    embedding_model: str = Field(..., description="Embedding model status")
    collection_exists: bool = Field(..., description="Whether the collection exists")
    configured_providers: List[str] = Field(default_factory=list, description="List of configured LLM providers")


class DocType(BaseModel):
    """Document type information."""
    name: str = Field(..., description="Name of the document type")
    description: str = Field(..., description="Description of the document type")


# New models for RAG endpoints
class RAGQueryRequest(BaseModel):
    """Request model for RAG query."""
    query: str = Field(..., description="Natural language question about Clarion programming")
    max_results: int = Field(5, ge=1, le=20, description="Maximum number of context chunks to retrieve")
    min_score: float = Field(0.3, ge=0.0, le=1.0, description="Minimum similarity score threshold")
    doc_type: Optional[str] = Field(None, description="Filter by document type")
    llm_provider: str = Field("deepseek", description="LLM provider to use (deepseek, ollama)")
    llm_model: Optional[str] = Field(None, description="Specific model to use (optional)")
    mode: str = Field(
        "augmented",
        description="Query mode: augmented (default), strict, or chat"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "query": "How do I define a QUEUE in Clarion?",
                "max_results": 5,
                "min_score": 0.3,
                "doc_type": "core_language",
                "llm_provider": "deepseek",
                "llm_model": "deepseek-chat",
                "mode": "augmented"
            }
        }


class RAGChunk(BaseModel):
    """Single context chunk used for RAG."""
    text: str = Field(..., description="Content of the chunk")
    score: float = Field(..., description="Similarity score")
    source: str = Field(..., description="Source document")
    doc_type: str = Field(..., description="Document type")
    chunk_index: int = Field(..., description="Chunk index in source document")


class RAGMetadata(BaseModel):
    """Metadata about RAG query execution."""
    chunks_retrieved: int = Field(..., description="Number of chunks retrieved")
    model_used: str = Field(..., description="LLM model used")
    tokens_used: int = Field(..., description="Total tokens used")
    cost_estimate: float = Field(..., description="Estimated cost in USD")
    response_time_ms: int = Field(..., description="Response time in milliseconds")
    query_mode: str = Field(..., description="Query mode used (augmented, strict, or chat)")


class RAGQueryResponse(BaseModel):
    """Response model for RAG query."""
    answer: str = Field(..., description="Generated answer from LLM")
    chunks: List[RAGChunk] = Field(..., description="Context chunks used")
    metadata: RAGMetadata = Field(..., description="Execution metadata")

    class Config:
        json_schema_extra = {
            "example": {
                "answer": "To define a QUEUE in Clarion...",
                "chunks": [
                    {
                        "text": "QUEUE is a structured data type...",
                        "score": 0.85,
                        "source": "Language Reference.pdf",
                        "doc_type": "core_language",
                        "chunk_index": 42
                    }
                ],
                "metadata": {
                    "chunks_retrieved": 5,
                    "model_used": "deepseek-chat",
                    "tokens_used": 1234,
                    "cost_estimate": 0.00017,
                    "response_time_ms": 856
                }
            }
        }


class ConfigureRequest(BaseModel):
    """Request model for provider configuration."""
    provider: str = Field(..., description="Provider ID (deepseek, ollama)")
    api_key: Optional[str] = Field(None, description="API key (if required by provider)")
    model: Optional[str] = Field(None, description="Default model to use (optional)")

    class Config:
        json_schema_extra = {
            "example": {
                "provider": "deepseek",
                "api_key": "sk-xxxxxxxxxxxxxxxx"
            }
        }


class ConfigureResponse(BaseModel):
    """Response model for provider configuration."""
    status: str = Field(..., description="Status (success, error)")
    message: str = Field(..., description="Human-readable message")


class ModelInfo(BaseModel):
    """Information about a specific model."""
    name: str = Field(..., description="Model name")
    input_cost_per_1m: float = Field(..., description="Input cost per 1M tokens (USD)")
    output_cost_per_1m: float = Field(..., description="Output cost per 1M tokens (USD)")
    avg_cost_per_1m: float = Field(..., description="Average cost per 1M tokens (USD)")


class ProviderInfo(BaseModel):
    """Information about an LLM provider."""
    id: str = Field(..., description="Provider ID")
    name: str = Field(..., description="Display name")
    models: List[ModelInfo] = Field(..., description="Available models with pricing")
    configured: bool = Field(..., description="Whether provider is configured")
    requires_api_key: bool = Field(..., description="Whether provider requires API key")
    cost_per_1m_tokens: float = Field(..., description="Average cost per 1M tokens (USD) - for backwards compatibility")
    price_range: str = Field(..., description="Price range across all models (e.g., '$0.15 - $10.00/1M')")


class ProvidersResponse(BaseModel):
    """Response model for providers list."""
    providers: List[ProviderInfo] = Field(..., description="List of available providers")


# ============================================================================
# Helper Functions
# ============================================================================

def build_context_from_chunks(chunks: List[dict]) -> str:
    """
    Build context string from retrieved chunks.

    Args:
        chunks: List of chunk dictionaries from vector store

    Returns:
        Formatted context string
    """
    context_parts = []

    for i, chunk in enumerate(chunks, 1):
        source = chunk.get('metadata', {}).get('source', 'Unknown')
        text = chunk.get('text', '')

        context_parts.append(f"--- Source {i}: {source} ---")
        context_parts.append(text)
        context_parts.append("")  # Empty line for separation

    return "\n".join(context_parts)


def mask_api_key(api_key: str) -> str:
    """
    Mask API key for logging.

    Args:
        api_key: API key to mask

    Returns:
        Masked API key (e.g., "sk-****")
    """
    if not api_key:
        return ""

    if len(api_key) <= 4:
        return "****"

    prefix = api_key[:3]
    return f"{prefix}****"


# ============================================================================
# Lifespan Context Manager
# ============================================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for FastAPI.
    Loads models at startup and cleans up at shutdown.
    """
    global vector_store, embedding_model, api_keys

    logger.info("Starting up Clarion Knowledge Base API...")

    # Initialize vector store
    try:
        vector_store = ClarionVectorStore()
        logger.info("Vector store initialized")
    except Exception as e:
        logger.error(f"Failed to initialize vector store: {e}")
        raise

    # Check if collection exists, if not restore from snapshot
    try:
        if not vector_store.collection_exists():
            logger.info("Collection 'clarion_docs' not found. Attempting to restore from snapshot...")
            snapshot_path = Path("/app/qdrant-snapshot.tar.gz")

            if snapshot_path.exists():
                logger.info(f"Found snapshot file: {snapshot_path}")

                # Extract snapshot
                temp_dir = Path("/tmp/qdrant_snapshot")
                temp_dir.mkdir(exist_ok=True)

                logger.info("Extracting snapshot...")
                with tarfile.open(snapshot_path, "r:gz") as tar:
                    tar.extractall(temp_dir)

                # Find .snapshot file
                snapshot_files = list(temp_dir.glob("*.snapshot"))
                if snapshot_files:
                    snapshot_file = snapshot_files[0]
                    logger.info(f"Uploading snapshot to Qdrant...")

                    # Upload snapshot to Qdrant
                    qdrant_host = os.getenv("QDRANT_HOST", "qdrant")
                    qdrant_port = os.getenv("QDRANT_PORT", "6333")

                    with open(snapshot_file, 'rb') as f:
                        response = requests.post(
                            f"http://{qdrant_host}:{qdrant_port}/collections/clarion_docs/snapshots/upload",
                            files={'snapshot': f},
                            timeout=300
                        )
                        response.raise_for_status()

                    logger.info("Snapshot uploaded successfully!")
                    logger.info(f"Collection 'clarion_docs' is now available with 21,747 documentation chunks")

                    # Cleanup temp files
                    shutil.rmtree(temp_dir, ignore_errors=True)
                else:
                    logger.error("No .snapshot file found in archive")
            else:
                logger.warning(f"Snapshot file not found at {snapshot_path}")
        else:
            info = vector_store.get_collection_info()
            points_count = info.get('points_count', 0) if info else 0
            logger.info(f"Collection 'clarion_docs' exists with {points_count:,} points")
    except Exception as e:
        logger.error(f"Error checking/restoring collection: {e}")
        # Don't raise - allow app to start even if restore fails

    # Initialize embedding model (lazy load - will load on first use)
    try:
        embedding_model = EmbeddingModel()
        logger.info("Embedding model loaded")
    except Exception as e:
        logger.error(f"Failed to load embedding model: {e}")
        raise

    # Load API keys from environment if available
    deepseek_key = os.getenv('DEEPSEEK_API_KEY')
    if deepseek_key:
        try:
            encrypted_key = fernet.encrypt(deepseek_key.encode()).decode()
            api_keys['deepseek'] = encrypted_key
            logger.info(f"Loaded Deepseek API key from environment: {mask_api_key(deepseek_key)}")
        except Exception as e:
            logger.error(f"Failed to encrypt Deepseek API key: {e}")

    logger.info("Startup complete")

    yield

    # Cleanup
    logger.info("Shutting down...")


# ============================================================================
# FastAPI App
# ============================================================================

# Create FastAPI app
app = FastAPI(
    title="Clarion Knowledge Base API",
    description="REST API for semantic search and RAG queries across Clarion documentation",
    version="1.2.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
static_dir = Path(__file__).parent.parent / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


# ============================================================================
# Endpoints - General
# ============================================================================

@app.get("/", tags=["General"])
async def root():
    """
    Serve the main web interface.
    """
    index_file = Path(__file__).parent.parent / "static" / "index.html"
    if index_file.exists():
        return FileResponse(str(index_file))

    # Fallback to API information if static files not found
    return {
        "name": "Clarion Knowledge Base API",
        "version": "1.2.0",
        "description": "REST API for semantic search and RAG queries across Clarion documentation",
        "endpoints": {
            "health": "/health",
            "search": "/search",
            "rag_query": "/api/query",
            "configure": "/api/configure",
            "providers": "/api/providers",
            "collection_info": "/collection/info",
            "doc_types": "/doc-types"
        }
    }


@app.get("/health", response_model=HealthResponse, tags=["General"])
async def health_check():
    """
    Health check endpoint to verify service status.
    """
    global vector_store, embedding_model, api_keys

    vector_store_status = "ok" if vector_store is not None else "not initialized"
    embedding_model_status = "ok" if embedding_model is not None else "not initialized"

    collection_exists = False
    if vector_store:
        try:
            collection_exists = vector_store.collection_exists()
        except Exception as e:
            logger.error(f"Error checking collection: {e}")

    # List configured providers
    configured = list(api_keys.keys())

    # Always include ollama if it doesn't require API key
    if "ollama" not in configured:
        configured.append("ollama")

    return HealthResponse(
        status="healthy" if (vector_store and embedding_model) else "degraded",
        vector_store=vector_store_status,
        embedding_model=embedding_model_status,
        collection_exists=collection_exists,
        configured_providers=configured
    )


# ============================================================================
# Endpoints - Search (Existing)
# ============================================================================

@app.post("/search", response_model=SearchResponse, tags=["Search"])
async def search_docs(request: SearchRequest):
    """
    Perform semantic search across Clarion documentation.

    Returns relevant documentation chunks with similarity scores and source citations.

    Note: Code examples may have lost indentation during PDF conversion.
    Manually format Clarion code (e.g., indent MAP statements) before use.
    """
    global vector_store, embedding_model

    if not vector_store or not embedding_model:
        raise HTTPException(
            status_code=503,
            detail="Service not ready. Vector store or embedding model not initialized."
        )

    try:
        # Generate query embedding
        logger.info(f"Processing search query: '{request.query}'")
        query_embedding = embedding_model.encode_text(request.query)

        # Build filter
        filter_dict = {}
        if request.doc_type:
            filter_dict['doc_type'] = request.doc_type

        # Perform search
        results = vector_store.search(
            query_vector=query_embedding.tolist(),
            limit=request.max_results,
            score_threshold=request.min_score,
            filter_dict=filter_dict if filter_dict else None
        )

        # Convert to response model
        search_results = [
            SearchResult(
                text=r['text'],
                score=r['score'],
                metadata=r['metadata'],
                id=r['id']
            )
            for r in results
        ]

        logger.info(f"Found {len(search_results)} results for query: '{request.query}'")

        return SearchResponse(
            query=request.query,
            results=search_results,
            total_results=len(search_results)
        )

    except Exception as e:
        logger.error(f"Error during search: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Search failed: {str(e)}"
        )


@app.get("/search", response_model=SearchResponse, tags=["Search"])
async def search_docs_get(
    query: str = Query(..., description="Natural language query about Clarion programming"),
    max_results: int = Query(5, ge=1, le=50, description="Maximum number of results"),
    min_score: float = Query(0.3, ge=0.0, le=1.0, description="Minimum similarity score"),
    doc_type: Optional[str] = Query(None, description="Filter by document type")
):
    """
    Perform semantic search using GET method (query parameters).

    Alternative to POST /search for simpler integrations.
    """
    request = SearchRequest(
        query=query,
        max_results=max_results,
        min_score=min_score,
        doc_type=doc_type
    )
    return await search_docs(request)


# ============================================================================
# Endpoints - RAG (New)
# ============================================================================

@app.post("/api/query", response_model=RAGQueryResponse, tags=["RAG"])
async def query_rag(request: RAGQueryRequest):
    """
    Perform RAG query: retrieve relevant docs and generate answer using LLM.

    This endpoint:
    1. Generates query embedding
    2. Searches vector store for relevant chunks
    3. Builds context from retrieved chunks
    4. Queries configured LLM with context + question
    5. Returns answer with source citations
    """
    global vector_store, embedding_model

    if not vector_store or not embedding_model:
        raise HTTPException(
            status_code=503,
            detail="Service not ready. Vector store or embedding model not initialized."
        )

    start_time = time.time()

    try:
        # Skip vector search for chat mode (performance optimization)
        if request.mode == "chat":
            logger.info("Chat mode: skipping vector search")
            chunks = []
            context = ""
        else:
            # 1. Generate query embedding
            logger.info(f"Processing RAG query in {request.mode} mode: '{request.query}'")
            query_embedding = embedding_model.encode_text(request.query)

            # 2. Build filter
            filter_dict = {}
            if request.doc_type:
                filter_dict['doc_type'] = request.doc_type

            # 3. Search vector store
            chunks = vector_store.search(
                query_vector=query_embedding.tolist(),
                limit=request.max_results,
                score_threshold=request.min_score,
                filter_dict=filter_dict if filter_dict else None
            )

        # Smart fallback based on mode
        if not chunks:
            if request.mode == "strict":
                # Strict mode requires documentation
                raise HTTPException(
                    status_code=404,
                    detail="No relevant documentation found for your query. Try lowering min_score, broadening your question, or switching to 'augmented' mode."
                )
            elif request.mode in ["augmented", "chat"]:
                # Augmented and chat modes can continue without docs
                logger.info(f"No docs found for query in {request.mode} mode, continuing with LLM knowledge")
                chunks = []  # Empty list
                context = "No specific documentation found for this query."
            else:
                raise HTTPException(
                    status_code=400,
                    detail=f"Invalid mode: {request.mode}. Use 'augmented', 'strict', or 'chat'."
                )
        else:
            # Build context from chunks
            context = build_context_from_chunks(chunks)

        # 5. Get LLM provider
        try:
            provider = get_llm_provider(request.llm_provider, request.llm_model)
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error getting LLM provider: {e}")
            raise HTTPException(
                status_code=500,
                detail=f"Failed to initialize LLM provider: {str(e)}"
            )

        # 6. Query LLM
        try:
            llm_result = provider.query(context=context, question=request.query, mode=request.mode)
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error querying LLM: {e}")
            raise HTTPException(
                status_code=500,
                detail=f"LLM query failed: {str(e)}"
            )

        # 7. Calculate response time
        response_time_ms = int((time.time() - start_time) * 1000)

        # 8. Build response
        rag_chunks = [
            RAGChunk(
                text=chunk['text'],
                score=chunk['score'],
                source=chunk.get('metadata', {}).get('source', 'Unknown'),
                doc_type=chunk.get('metadata', {}).get('doc_type', 'unknown'),
                chunk_index=chunk.get('metadata', {}).get('chunk_index', 0)
            )
            for chunk in chunks
        ]

        metadata = RAGMetadata(
            chunks_retrieved=len(chunks),
            model_used=llm_result['model'],
            tokens_used=llm_result['tokens_used'],
            cost_estimate=llm_result['cost_estimate'],
            response_time_ms=response_time_ms,
            query_mode=request.mode
        )

        logger.info(
            f"RAG query complete: {len(chunks)} chunks, {llm_result['tokens_used']} tokens, "
            f"{response_time_ms}ms, ${llm_result['cost_estimate']:.6f}"
        )

        return RAGQueryResponse(
            answer=llm_result['answer'],
            chunks=rag_chunks,
            metadata=metadata
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error during RAG query: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"RAG query failed: {str(e)}"
        )


@app.post("/api/configure", response_model=ConfigureResponse, tags=["Configuration"])
async def configure_provider(request: ConfigureRequest):
    """
    Configure LLM provider with API key.

    API keys are encrypted before storage and never logged.
    """
    global api_keys

    provider_id = request.provider.lower()

    # Validate provider
    valid_providers = ["deepseek", "openai", "anthropic", "gemini", "grok", "ollama"]
    if provider_id not in valid_providers:
        raise HTTPException(
            status_code=400,
            detail=f"Unknown provider: {provider_id}. Available: {', '.join(valid_providers)}"
        )

    # Ollama doesn't require API key
    if provider_id == "ollama":
        return ConfigureResponse(
            status="success",
            message="Ollama configured (no API key required for local inference)"
        )

    # Validate API key presence
    if not request.api_key:
        raise HTTPException(
            status_code=400,
            detail=f"API key required for provider: {provider_id}"
        )

    # Validate API key format (basic check)
    if provider_id in ["deepseek", "openai", "anthropic"]:
        if not request.api_key.startswith("sk-"):
            raise HTTPException(
                status_code=400,
                detail=f"Invalid {provider_id.title()} API key format (should start with 'sk-')"
            )

    try:
        # Encrypt and store API key
        encrypted_key = fernet.encrypt(request.api_key.encode()).decode()
        api_keys[provider_id] = encrypted_key

        logger.info(f"API key configured for provider: {provider_id} ({mask_api_key(request.api_key)})")

        return ConfigureResponse(
            status="success",
            message=f"API key saved securely for {provider_id}"
        )

    except Exception as e:
        logger.error(f"Error configuring provider: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to save API key: {str(e)}"
        )


@app.get("/api/providers", response_model=ProvidersResponse, tags=["Configuration"])
async def list_providers():
    """
    List available LLM providers with configuration status and per-model pricing.
    """
    global api_keys

    providers = [
        ProviderInfo(
            id="deepseek",
            name="Deepseek",
            models=[
                ModelInfo(name="deepseek-chat", input_cost_per_1m=0.28, output_cost_per_1m=0.42, avg_cost_per_1m=0.35),
                ModelInfo(name="deepseek-reasoner", input_cost_per_1m=0.28, output_cost_per_1m=0.42, avg_cost_per_1m=0.35)
            ],
            configured="deepseek" in api_keys,
            requires_api_key=True,
            cost_per_1m_tokens=0.35,  # Same pricing for both models
            price_range="$0.35/1M"
        ),
        ProviderInfo(
            id="openai",
            name="OpenAI",
            models=[
                ModelInfo(name="gpt-5", input_cost_per_1m=1.25, output_cost_per_1m=10.00, avg_cost_per_1m=5.63),
                ModelInfo(name="gpt-4o", input_cost_per_1m=2.50, output_cost_per_1m=10.00, avg_cost_per_1m=6.25),
                ModelInfo(name="gpt-4o-mini", input_cost_per_1m=0.15, output_cost_per_1m=0.60, avg_cost_per_1m=0.38),
                ModelInfo(name="o1", input_cost_per_1m=15.00, output_cost_per_1m=60.00, avg_cost_per_1m=37.50),
                ModelInfo(name="o3-mini", input_cost_per_1m=1.10, output_cost_per_1m=4.40, avg_cost_per_1m=2.75),
                ModelInfo(name="gpt-4-turbo", input_cost_per_1m=10.00, output_cost_per_1m=30.00, avg_cost_per_1m=20.00)
            ],
            configured="openai" in api_keys,
            requires_api_key=True,
            cost_per_1m_tokens=12.09,  # Average across models
            price_range="$0.38 - $37.50/1M"
        ),
        ProviderInfo(
            id="anthropic",
            name="Anthropic Claude",
            models=[
                ModelInfo(name="claude-sonnet-4-5", input_cost_per_1m=3.00, output_cost_per_1m=15.00, avg_cost_per_1m=9.00),
                ModelInfo(name="claude-opus-4-1", input_cost_per_1m=15.00, output_cost_per_1m=75.00, avg_cost_per_1m=45.00),
                ModelInfo(name="claude-haiku-3-5", input_cost_per_1m=0.80, output_cost_per_1m=4.00, avg_cost_per_1m=2.40)
            ],
            configured="anthropic" in api_keys,
            requires_api_key=True,
            cost_per_1m_tokens=18.80,  # Average across models
            price_range="$2.40 - $45.00/1M"
        ),
        ProviderInfo(
            id="gemini",
            name="Google Gemini",
            models=[
                ModelInfo(name="gemini-2.5-pro", input_cost_per_1m=1.25, output_cost_per_1m=10.00, avg_cost_per_1m=5.63),
                ModelInfo(name="gemini-2.0-flash", input_cost_per_1m=0.10, output_cost_per_1m=0.40, avg_cost_per_1m=0.25),
                ModelInfo(name="gemini-2.0-flash-lite", input_cost_per_1m=0.075, output_cost_per_1m=0.30, avg_cost_per_1m=0.19),
                ModelInfo(name="gemini-1.5-pro", input_cost_per_1m=1.25, output_cost_per_1m=5.00, avg_cost_per_1m=3.13)
            ],
            configured="gemini" in api_keys,
            requires_api_key=True,
            cost_per_1m_tokens=2.30,  # Average across models
            price_range="$0.19 - $5.63/1M"
        ),
        ProviderInfo(
            id="grok",
            name="xAI Grok",
            models=[
                ModelInfo(name="grok-4", input_cost_per_1m=3.00, output_cost_per_1m=15.00, avg_cost_per_1m=9.00),
                ModelInfo(name="grok-4-fast", input_cost_per_1m=0.20, output_cost_per_1m=0.50, avg_cost_per_1m=0.35),
                ModelInfo(name="grok-3", input_cost_per_1m=3.00, output_cost_per_1m=15.00, avg_cost_per_1m=9.00)
            ],
            configured="grok" in api_keys,
            requires_api_key=True,
            cost_per_1m_tokens=6.12,  # Average across models
            price_range="$0.35 - $9.00/1M"
        ),
        ProviderInfo(
            id="ollama",
            name="Ollama (Local)",
            models=[
                ModelInfo(name="llama3", input_cost_per_1m=0.0, output_cost_per_1m=0.0, avg_cost_per_1m=0.0),
                ModelInfo(name="mistral", input_cost_per_1m=0.0, output_cost_per_1m=0.0, avg_cost_per_1m=0.0),
                ModelInfo(name="codellama", input_cost_per_1m=0.0, output_cost_per_1m=0.0, avg_cost_per_1m=0.0),
                ModelInfo(name="deepseek-r1", input_cost_per_1m=0.0, output_cost_per_1m=0.0, avg_cost_per_1m=0.0)
            ],
            configured=True,  # Always configured (no API key needed)
            requires_api_key=False,
            cost_per_1m_tokens=0.0,
            price_range="FREE"
        )
    ]

    return ProvidersResponse(providers=providers)


# ============================================================================
# Endpoints - Collection Info (Existing)
# ============================================================================

@app.get("/collection/info", response_model=CollectionInfo, tags=["Collection"])
async def get_collection_info():
    """
    Get information about the vector store collection.
    """
    global vector_store

    if not vector_store:
        raise HTTPException(
            status_code=503,
            detail="Vector store not initialized"
        )

    try:
        info = vector_store.get_collection_info()

        if not info:
            raise HTTPException(
                status_code=404,
                detail="Collection not found or information not available"
            )

        return CollectionInfo(
            name=info['name'],
            vectors_count=info['vectors_count'],
            points_count=info['points_count'],
            status=info['status']
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting collection info: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to get collection info: {str(e)}"
        )


@app.get("/doc-types", response_model=List[DocType], tags=["Documentation"])
async def list_doc_types():
    """
    List available document types for filtering searches.
    """
    doc_types = [
        DocType(
            name="core_language",
            description="Language reference, programming guide, and learning materials"
        ),
        DocType(
            name="libraries",
            description="ABC Library, Internet Builder, Business Math library references"
        ),
        DocType(
            name="ide_development",
            description="IDE reference, user guides, and getting started materials"
        ),
        DocType(
            name="templates",
            description="Template guide and language reference"
        ),
        DocType(
            name="specialized",
            description="Database drivers, XML support, Report Writer, Application Broker"
        ),
        DocType(
            name="advanced",
            description="Advanced topics and techniques"
        ),
        DocType(
            name="utilities",
            description="Utilities and tools"
        )
    ]

    return doc_types


# ============================================================================
# Error Handlers
# ============================================================================

@app.exception_handler(404)
async def not_found_handler(request, exc):
    """Handle 404 errors."""
    return JSONResponse(
        status_code=404,
        content={
            "error": "Not Found",
            "detail": "The requested resource was not found",
            "path": str(request.url)
        }
    )


@app.exception_handler(500)
async def internal_error_handler(request, exc):
    """Handle 500 errors."""
    logger.error(f"Internal error: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "detail": "An internal error occurred. Please try again later."
        }
    )


# ============================================================================
# Main Entry Point
# ============================================================================

if __name__ == "__main__":
    import uvicorn

    # Run the server
    uvicorn.run(
        "web_app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
