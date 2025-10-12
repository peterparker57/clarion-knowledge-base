"""
Qdrant Vector Store Integration for Clarion Knowledge Base
Handles storage and retrieval of document embeddings
"""

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue
from typing import List, Dict, Optional
import logging
import uuid

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ClarionVectorStore:
    """
    Vector store for Clarion documentation using Qdrant.
    """

    def __init__(
        self,
        host: str = None,
        port: int = 6333,
        collection_name: str = "clarion_docs"
    ):
        """
        Initialize connection to Qdrant.

        Args:
            host: Qdrant server host (defaults to env QDRANT_HOST or 'localhost')
            port: Qdrant server port
            collection_name: Name of the collection
        """
        import os

        # Allow environment variable override for Docker networking
        if host is None:
            host = os.environ.get('QDRANT_HOST', 'localhost')

        self.collection_name = collection_name
        self.client = QdrantClient(host=host, port=port)

        logger.info(f"Connected to Qdrant at {host}:{port}")

    def create_collection(
        self,
        vector_size: int,
        distance: Distance = Distance.COSINE,
        recreate: bool = False
    ):
        """
        Create a collection for storing embeddings.

        Args:
            vector_size: Dimension of embedding vectors
            distance: Distance metric (COSINE, EUCLID, DOT)
            recreate: Whether to recreate if exists
        """
        try:
            if recreate:
                self.client.delete_collection(self.collection_name)
                logger.info(f"Deleted existing collection: {self.collection_name}")
        except:
            pass  # Collection doesn't exist

        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=distance
            )
        )

        logger.info(
            f"Created collection '{self.collection_name}' "
            f"with vector size {vector_size} and {distance} distance"
        )

    def collection_exists(self) -> bool:
        """Check if collection exists."""
        try:
            self.client.get_collection(self.collection_name)
            return True
        except:
            return False

    def add_chunks(
        self,
        chunks: List[Dict],
        batch_size: int = 100
    ):
        """
        Add chunks with embeddings to the collection.

        Args:
            chunks: List of chunk dictionaries with 'embedding' and 'metadata'
            batch_size: Number of chunks to upload at once
        """
        if not chunks:
            logger.warning("No chunks to add")
            return

        total = len(chunks)
        logger.info(f"Adding {total} chunks to collection '{self.collection_name}'")

        # Process in batches
        for i in range(0, total, batch_size):
            batch = chunks[i:i + batch_size]
            points = []

            for chunk in batch:
                # Generate unique ID
                point_id = str(uuid.uuid4())

                # Create point
                point = PointStruct(
                    id=point_id,
                    vector=chunk['embedding'],
                    payload={
                        'text': chunk['text'],
                        'metadata': chunk['metadata']
                    }
                )
                points.append(point)

            # Upload batch
            self.client.upsert(
                collection_name=self.collection_name,
                points=points
            )

            logger.info(f"Uploaded batch {i // batch_size + 1}: {len(batch)} chunks")

        logger.info(f"Successfully added {total} chunks to Qdrant")

    def search(
        self,
        query_vector: List[float],
        limit: int = 5,
        score_threshold: Optional[float] = None,
        filter_dict: Optional[Dict] = None
    ) -> List[Dict]:
        """
        Search for similar chunks.

        Args:
            query_vector: Query embedding vector
            limit: Number of results to return
            score_threshold: Minimum similarity score
            filter_dict: Metadata filters (e.g., {'doc_type': 'core_language'})

        Returns:
            List of search results with text, metadata, and score
        """
        # Build filter if provided
        search_filter = None
        if filter_dict:
            conditions = []
            for key, value in filter_dict.items():
                conditions.append(
                    FieldCondition(
                        key=f"metadata.{key}",
                        match=MatchValue(value=value)
                    )
                )
            search_filter = Filter(must=conditions)

        # Perform search
        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=limit,
            score_threshold=score_threshold,
            query_filter=search_filter
        )

        # Format results
        formatted_results = []
        for result in results:
            formatted_results.append({
                'text': result.payload['text'],
                'metadata': result.payload['metadata'],
                'score': result.score,
                'id': result.id
            })

        return formatted_results

    def get_collection_info(self) -> Dict:
        """Get information about the collection."""
        try:
            info = self.client.get_collection(self.collection_name)
            return {
                'name': self.collection_name,
                'vectors_count': info.vectors_count,
                'points_count': info.points_count,
                'status': info.status
            }
        except Exception as e:
            logger.error(f"Error getting collection info: {e}")
            return {}


def test_vector_store():
    """Test the vector store with sample data."""
    import json
    from pathlib import Path
    from embeddings import EmbeddingModel
    import sys

    # Fix encoding for Windows console
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')

    # Load enriched chunks
    chunks_path = Path("data/chunks/enriched_sample_chunks.json")
    if not chunks_path.exists():
        print("Error: enriched_sample_chunks.json not found. Run embeddings.py first.")
        return

    with open(chunks_path, 'r', encoding='utf-8') as f:
        chunks = json.load(f)

    print(f"Loaded {len(chunks)} enriched chunks")

    # Initialize vector store
    vector_store = ClarionVectorStore()

    # Create collection (recreate to start fresh)
    embedding_dim = len(chunks[0]['embedding'])
    vector_store.create_collection(
        vector_size=embedding_dim,
        recreate=True
    )

    # Add chunks to collection
    vector_store.add_chunks(chunks)

    # Get collection info
    info = vector_store.get_collection_info()
    print(f"\n=== Collection Info ===")
    print(f"Name: {info['name']}")
    print(f"Points: {info['points_count']}")
    print(f"Vectors: {info['vectors_count']}")
    print(f"Status: {info['status']}")

    # Test search with a query
    print(f"\n=== Testing Search ===")

    # Use first chunk's embedding as query (should return itself as top result)
    query_vector = chunks[0]['embedding']
    results = vector_store.search(
        query_vector=query_vector,
        limit=3
    )

    print(f"Found {len(results)} results:")
    for i, result in enumerate(results, 1):
        print(f"\nResult {i}:")
        print(f"  Score: {result['score']:.4f}")
        print(f"  Source: {result['metadata']['source']}")
        print(f"  Chunk: {result['metadata']['chunk_index'] + 1}/{result['metadata']['chunk_count']}")
        print(f"  Text preview: {result['text'][:100]}...")

    # Test semantic search with actual query
    print(f"\n=== Testing Semantic Search ===")
    embedding_model = EmbeddingModel()
    query_text = "How do I define a QUEUE in Clarion?"
    query_embedding = embedding_model.encode_text(query_text)

    results = vector_store.search(
        query_vector=query_embedding.tolist(),
        limit=3,
        score_threshold=0.3
    )

    print(f"Query: '{query_text}'")
    print(f"Found {len(results)} results:")
    for i, result in enumerate(results, 1):
        print(f"\nResult {i}:")
        print(f"  Score: {result['score']:.4f}")
        print(f"  Source: {result['metadata']['source']}")
        print(f"  Text preview: {result['text'][:200]}...")


if __name__ == "__main__":
    test_vector_store()
