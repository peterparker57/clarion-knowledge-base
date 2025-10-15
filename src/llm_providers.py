"""
LLM Provider Abstraction Layer for Clarion Knowledge Base

This module provides a unified interface for multiple LLM providers, including:
- DeepSeek (default, cost-effective)
- Ollama (local inference, free)

Each provider implements the LLMProvider abstract base class and returns
standardized responses with answer, model info, token usage, and cost estimates.
"""

import os
import json
import logging
from abc import ABC, abstractmethod
from typing import Dict, Optional, Any
import requests


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Prompt template for all providers
PROMPT_TEMPLATE = """You are a helpful Clarion programming assistant. Answer the user's question based ONLY on the provided documentation context.

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

ANSWER:"""


class LLMProviderError(Exception):
    """Base exception for LLM provider errors"""
    pass


class APIKeyError(LLMProviderError):
    """Raised when API key is invalid or missing"""
    pass


class NetworkError(LLMProviderError):
    """Raised when network request fails"""
    pass


class RateLimitError(LLMProviderError):
    """Raised when rate limit is exceeded"""
    pass


class ModelNotFoundError(LLMProviderError):
    """Raised when requested model is not available"""
    pass


class ServiceUnavailableError(LLMProviderError):
    """Raised when the LLM service is unavailable"""
    pass


def estimate_tokens(text: str) -> int:
    """
    Estimate token count using simple approximation.

    Args:
        text: Input text to estimate tokens for

    Returns:
        Estimated token count (1 token ≈ 4 characters)
    """
    return len(text) // 4


class LLMProvider(ABC):
    """Abstract base class for LLM providers"""

    @abstractmethod
    def query(self, context: str, question: str, **kwargs) -> Dict[str, Any]:
        """
        Query the LLM with context and question.

        Args:
            context: Retrieved documentation chunks
            question: User's question
            **kwargs: Provider-specific options (e.g., temperature, max_tokens)

        Returns:
            {
                "answer": str,
                "model": str,
                "tokens_used": int,
                "cost_estimate": float
            }

        Raises:
            LLMProviderError: For various provider-specific errors
        """
        pass

    def _format_prompt(self, context: str, question: str) -> str:
        """
        Format the prompt using the standard template.

        Args:
            context: Documentation context
            question: User question

        Returns:
            Formatted prompt string
        """
        return PROMPT_TEMPLATE.format(context=context, question=question)


class DeepseekProvider(LLMProvider):
    """
    DeepSeek LLM Provider - Cost-effective, code-focused model

    API Documentation: https://api.deepseek.com/v1
    Pricing: $0.14 per 1M input tokens, $0.28 per 1M output tokens
    """

    API_ENDPOINT = "https://api.deepseek.com/v1/chat/completions"
    DEFAULT_MODEL = "deepseek-chat"
    INPUT_COST_PER_1M = 0.14  # USD
    OUTPUT_COST_PER_1M = 0.28  # USD

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        """
        Initialize DeepSeek provider.

        Args:
            api_key: DeepSeek API key (or set DEEPSEEK_API_KEY env var)
            model: Model to use (default: deepseek-chat)

        Raises:
            APIKeyError: If API key is not provided
        """
        self.api_key = api_key or os.environ.get("DEEPSEEK_API_KEY")
        if not self.api_key:
            raise APIKeyError(
                "DeepSeek API key not found. Set DEEPSEEK_API_KEY environment "
                "variable or pass api_key parameter."
            )

        self.model = model or self.DEFAULT_MODEL
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })

        logger.info(f"Initialized DeepSeek provider with model: {self.model}")

    def query(self, context: str, question: str, **kwargs) -> Dict[str, Any]:
        """
        Query DeepSeek API with context and question.

        Args:
            context: Documentation context
            question: User question
            **kwargs: Optional parameters (temperature, max_tokens, etc.)

        Returns:
            Response dictionary with answer, model, tokens, and cost

        Raises:
            APIKeyError: Invalid API key
            RateLimitError: Rate limit exceeded
            NetworkError: Network/connectivity issues
            LLMProviderError: Other API errors
        """
        prompt = self._format_prompt(context, question)

        # Prepare request payload
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": kwargs.get("temperature", 0.7),
            "max_tokens": kwargs.get("max_tokens", 2000),
            "stream": False
        }

        try:
            logger.debug(f"Sending request to DeepSeek API: {self.model}")
            response = self.session.post(
                self.API_ENDPOINT,
                json=payload,
                timeout=kwargs.get("timeout", 60)
            )

            # Handle various HTTP errors
            if response.status_code == 401:
                raise APIKeyError("Invalid DeepSeek API key")
            elif response.status_code == 429:
                raise RateLimitError("DeepSeek API rate limit exceeded")
            elif response.status_code == 404:
                raise ModelNotFoundError(f"Model '{self.model}' not found")
            elif response.status_code >= 500:
                raise ServiceUnavailableError(
                    f"DeepSeek API unavailable (status: {response.status_code})"
                )
            elif response.status_code != 200:
                error_msg = response.json().get("error", {}).get("message", "Unknown error")
                raise LLMProviderError(
                    f"DeepSeek API error ({response.status_code}): {error_msg}"
                )

            # Parse response
            result = response.json()
            answer = result["choices"][0]["message"]["content"]

            # Extract token usage
            usage = result.get("usage", {})
            input_tokens = usage.get("prompt_tokens", estimate_tokens(prompt))
            output_tokens = usage.get("completion_tokens", estimate_tokens(answer))
            total_tokens = input_tokens + output_tokens

            # Calculate cost
            input_cost = (input_tokens / 1_000_000) * self.INPUT_COST_PER_1M
            output_cost = (output_tokens / 1_000_000) * self.OUTPUT_COST_PER_1M
            total_cost = input_cost + output_cost

            logger.info(
                f"DeepSeek query successful: {total_tokens} tokens, "
                f"${total_cost:.6f} cost"
            )

            return {
                "answer": answer.strip(),
                "model": self.model,
                "tokens_used": total_tokens,
                "cost_estimate": round(total_cost, 6)
            }

        except requests.exceptions.Timeout:
            raise NetworkError("DeepSeek API request timed out")
        except requests.exceptions.ConnectionError:
            raise NetworkError("Failed to connect to DeepSeek API")
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Network error: {str(e)}")
        except (KeyError, json.JSONDecodeError) as e:
            raise LLMProviderError(f"Invalid API response format: {str(e)}")


class OllamaProvider(LLMProvider):
    """
    Ollama LLM Provider - Local inference, free to use

    Requires Ollama to be running locally or in Docker network.
    Supports models: llama3, mistral, codellama
    """

    DEFAULT_ENDPOINT = "http://ollama:11434"  # Docker network endpoint
    SUPPORTED_MODELS = ["llama3", "mistral", "codellama"]

    def __init__(
        self,
        endpoint: Optional[str] = None,
        model: Optional[str] = None
    ):
        """
        Initialize Ollama provider.

        Args:
            endpoint: Ollama API endpoint (default: http://ollama:11434)
            model: Model to use (default: llama3)
        """
        self.endpoint = endpoint or os.environ.get("OLLAMA_ENDPOINT", self.DEFAULT_ENDPOINT)
        self.model = model or "llama3"

        if self.model not in self.SUPPORTED_MODELS:
            logger.warning(
                f"Model '{self.model}' not in supported list: {self.SUPPORTED_MODELS}. "
                "Proceeding anyway..."
            )

        self.api_url = f"{self.endpoint}/api/generate"
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

        logger.info(f"Initialized Ollama provider: {self.endpoint} (model: {self.model})")

    def _check_connection(self) -> bool:
        """
        Check if Ollama service is available.

        Returns:
            True if service is available, False otherwise
        """
        try:
            response = self.session.get(
                f"{self.endpoint}/api/tags",
                timeout=5
            )
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def query(self, context: str, question: str, **kwargs) -> Dict[str, Any]:
        """
        Query Ollama API with context and question.

        Args:
            context: Documentation context
            question: User question
            **kwargs: Optional parameters (temperature, num_predict, etc.)

        Returns:
            Response dictionary with answer, model, tokens, and cost (always 0.0)

        Raises:
            ServiceUnavailableError: Ollama service not running
            ModelNotFoundError: Requested model not available
            NetworkError: Network/connectivity issues
            LLMProviderError: Other API errors
        """
        # Check if Ollama is available
        if not self._check_connection():
            raise ServiceUnavailableError(
                f"Ollama service not available at {self.endpoint}. "
                "Make sure Ollama is running."
            )

        prompt = self._format_prompt(context, question)

        # Prepare request payload (Ollama format)
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": kwargs.get("temperature", 0.7),
                "num_predict": kwargs.get("max_tokens", 2000)
            }
        }

        try:
            logger.debug(f"Sending request to Ollama API: {self.model}")
            response = self.session.post(
                self.api_url,
                json=payload,
                timeout=kwargs.get("timeout", 120)  # Longer timeout for local inference
            )

            # Handle errors
            if response.status_code == 404:
                raise ModelNotFoundError(
                    f"Model '{self.model}' not found. "
                    f"Run 'ollama pull {self.model}' to download it."
                )
            elif response.status_code != 200:
                error_msg = response.text
                raise LLMProviderError(
                    f"Ollama API error ({response.status_code}): {error_msg}"
                )

            # Parse response
            result = response.json()
            answer = result.get("response", "")

            if not answer:
                raise LLMProviderError("Empty response from Ollama")

            # Estimate tokens (Ollama doesn't always provide exact counts)
            input_tokens = estimate_tokens(prompt)
            output_tokens = estimate_tokens(answer)
            total_tokens = input_tokens + output_tokens

            logger.info(
                f"Ollama query successful: {total_tokens} tokens (estimated), "
                f"$0.00 cost (local)"
            )

            return {
                "answer": answer.strip(),
                "model": self.model,
                "tokens_used": total_tokens,
                "cost_estimate": 0.0  # Local inference is free
            }

        except requests.exceptions.Timeout:
            raise NetworkError(
                f"Ollama API request timed out. Model '{self.model}' may be slow "
                "or not responding."
            )
        except requests.exceptions.ConnectionError:
            raise NetworkError(
                f"Failed to connect to Ollama at {self.endpoint}. "
                "Is Ollama running?"
            )
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Network error: {str(e)}")
        except (KeyError, json.JSONDecodeError) as e:
            raise LLMProviderError(f"Invalid API response format: {str(e)}")


def get_llm_provider(
    provider_id: str,
    api_key: Optional[str] = None,
    model: Optional[str] = None,
    **kwargs
) -> LLMProvider:
    """
    Factory function to create LLM provider instances.

    Args:
        provider_id: Provider identifier ("deepseek", "ollama")
        api_key: API key for commercial providers
        model: Model name to use
        **kwargs: Additional provider-specific parameters

    Returns:
        Configured LLMProvider instance

    Raises:
        ValueError: For unsupported provider IDs
        APIKeyError: For missing API keys

    Example:
        >>> provider = get_llm_provider("deepseek", api_key="sk-...")
        >>> result = provider.query(context="...", question="...")
        >>> print(result["answer"])
    """
    provider_id = provider_id.lower().strip()

    if provider_id == "deepseek":
        return DeepseekProvider(api_key=api_key, model=model)

    elif provider_id == "ollama":
        endpoint = kwargs.get("endpoint")
        return OllamaProvider(endpoint=endpoint, model=model)

    else:
        raise ValueError(
            f"Unsupported provider: '{provider_id}'. "
            f"Supported providers: deepseek, ollama"
        )


# Example usage
if __name__ == "__main__":
    # Example 1: DeepSeek provider
    print("=== Example 1: DeepSeek Provider ===")
    try:
        provider = get_llm_provider(
            "deepseek",
            api_key=os.environ.get("DEEPSEEK_API_KEY")
        )

        context = """
        The ACCEPT statement transfers control from one procedure to another.

        Syntax: ACCEPT

        Example:
        MyProcedure PROCEDURE
            CODE
            ! Do some work
            ACCEPT
            ! More code
        """

        question = "How do I use the ACCEPT statement in Clarion?"

        result = provider.query(context, question)
        print(f"Answer: {result['answer'][:200]}...")
        print(f"Model: {result['model']}")
        print(f"Tokens: {result['tokens_used']}")
        print(f"Cost: ${result['cost_estimate']:.6f}")

    except LLMProviderError as e:
        print(f"Error: {e}")

    print("\n=== Example 2: Ollama Provider ===")
    try:
        provider = get_llm_provider("ollama", model="llama3")

        result = provider.query(context, question)
        print(f"Answer: {result['answer'][:200]}...")
        print(f"Model: {result['model']}")
        print(f"Tokens: {result['tokens_used']}")
        print(f"Cost: ${result['cost_estimate']:.2f}")

    except LLMProviderError as e:
        print(f"Error: {e}")
