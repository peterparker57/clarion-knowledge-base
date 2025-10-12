"""
Embedding Model Management for Clarion Knowledge Base
Uses sentence-transformers for generating vector embeddings
"""

from sentence_transformers import SentenceTransformer
from typing import List, Dict
import logging
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EmbeddingModel:
    """
    Wrapper for embedding model with batch processing support.
    """

    def __init__(
        self,
        model_name: str = "sentence-transformers/all-mpnet-base-v2",
        device: str = None
    ):
        """
        Initialize the embedding model.

        Args:
            model_name: HuggingFace model identifier
            device: Device to use ('cuda', 'cpu', or None for auto)
        """
        self.model_name = model_name

        logger.info(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name, device=device)

        self.embedding_dim = self.model.get_sentence_embedding_dimension()
        logger.info(
            f"Model loaded successfully. Embedding dimension: {self.embedding_dim}"
        )

    def encode_text(
        self,
        text: str,
        show_progress: bool = False
    ) -> np.ndarray:
        """
        Encode a single text into an embedding vector.

        Args:
            text: Text to encode
            show_progress: Whether to show progress bar

        Returns:
            Numpy array of embedding vector
        """
        embedding = self.model.encode(
            text,
            show_progress_bar=show_progress,
            convert_to_numpy=True
        )
        return embedding

    def encode_texts(
        self,
        texts: List[str],
        batch_size: int = 32,
        show_progress: bool = True
    ) -> np.ndarray:
        """
        Encode multiple texts into embedding vectors (batch processing).

        Args:
            texts: List of texts to encode
            batch_size: Number of texts to process at once
            show_progress: Whether to show progress bar

        Returns:
            Numpy array of embedding vectors
        """
        logger.info(f"Encoding {len(texts)} texts with batch size {batch_size}")

        embeddings = self.model.encode(
            texts,
            batch_size=batch_size,
            show_progress_bar=show_progress,
            convert_to_numpy=True
        )

        logger.info(f"Generated {len(embeddings)} embeddings of dimension {self.embedding_dim}")
        return embeddings

    def encode_chunks(
        self,
        chunks: List[Dict],
        text_key: str = 'text',
        batch_size: int = 32,
        show_progress: bool = True
    ) -> List[Dict]:
        """
        Encode chunks with embeddings added to each chunk dictionary.

        Args:
            chunks: List of chunk dictionaries
            text_key: Key in chunk dict that contains text
            batch_size: Batch size for encoding
            show_progress: Whether to show progress bar

        Returns:
            List of chunks with 'embedding' field added
        """
        # Extract texts
        texts = [chunk[text_key] for chunk in chunks]

        # Generate embeddings
        embeddings = self.encode_texts(texts, batch_size, show_progress)

        # Add embeddings to chunks
        enriched_chunks = []
        for chunk, embedding in zip(chunks, embeddings):
            enriched_chunk = {
                **chunk,
                'embedding': embedding.tolist()  # Convert to list for JSON serialization
            }
            enriched_chunks.append(enriched_chunk)

        return enriched_chunks

    def get_embedding_dim(self) -> int:
        """Get the embedding dimension."""
        return self.embedding_dim

    def similarity(
        self,
        embedding1: np.ndarray,
        embedding2: np.ndarray
    ) -> float:
        """
        Compute cosine similarity between two embeddings.

        Args:
            embedding1: First embedding vector
            embedding2: Second embedding vector

        Returns:
            Cosine similarity score (0 to 1)
        """
        # Ensure numpy arrays
        if not isinstance(embedding1, np.ndarray):
            embedding1 = np.array(embedding1)
        if not isinstance(embedding2, np.ndarray):
            embedding2 = np.array(embedding2)

        # Compute cosine similarity
        dot_product = np.dot(embedding1, embedding2)
        norm1 = np.linalg.norm(embedding1)
        norm2 = np.linalg.norm(embedding2)

        if norm1 == 0 or norm2 == 0:
            return 0.0

        return dot_product / (norm1 * norm2)


def test_embeddings():
    """Test the embedding model."""
    import json
    from pathlib import Path

    # Load sample chunks
    chunks_path = Path("data/chunks/sample_chunks.json")
    if not chunks_path.exists():
        print("Error: sample_chunks.json not found. Run chunking.py first.")
        return

    with open(chunks_path, 'r', encoding='utf-8') as f:
        chunks = json.load(f)

    # Use only first 10 chunks for testing
    test_chunks = chunks[:10]

    print(f"Loaded {len(test_chunks)} chunks for testing")

    # Initialize embedding model
    embedding_model = EmbeddingModel(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    # Encode chunks
    enriched_chunks = embedding_model.encode_chunks(
        test_chunks,
        batch_size=10,
        show_progress=True
    )

    # Display results
    print(f"\n=== Embedding Test Results ===")
    print(f"Embedding dimension: {embedding_model.get_embedding_dim()}")
    print(f"Encoded {len(enriched_chunks)} chunks")

    # Show sample embedding
    sample = enriched_chunks[0]
    embedding_preview = sample['embedding'][:10]  # First 10 dimensions
    print(f"\nSample chunk from: {sample['metadata']['source']}")
    print(f"Text length: {len(sample['text'])} chars")
    print(f"Embedding preview (first 10 dims): {[f'{x:.4f}' for x in embedding_preview]}")

    # Test similarity between two chunks
    if len(enriched_chunks) >= 2:
        emb1 = np.array(enriched_chunks[0]['embedding'])
        emb2 = np.array(enriched_chunks[1]['embedding'])
        similarity = embedding_model.similarity(emb1, emb2)
        print(f"\nSimilarity between chunks 0 and 1: {similarity:.4f}")

    # Save enriched chunks
    output_path = Path("data/chunks/enriched_sample_chunks.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(enriched_chunks, f, indent=2, ensure_ascii=False)
    print(f"\nSaved enriched chunks to: {output_path}")

    return enriched_chunks


if __name__ == "__main__":
    test_embeddings()
