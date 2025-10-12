"""
Semantic Chunking Strategy for Clarion Documentation
Implements recursive chunking with code-awareness
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List, Dict
import logging
from pathlib import Path
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ClarionDocumentChunker:
    """
    Intelligent chunking for Clarion technical documentation.
    Respects code blocks, tables, and semantic boundaries.
    """

    def __init__(
        self,
        chunk_size: int = 800,
        chunk_overlap: int = 100,
        separators: List[str] = None
    ):
        """
        Initialize the document chunker.

        Args:
            chunk_size: Target size in tokens (approximately characters)
            chunk_overlap: Overlap between chunks for continuity
            separators: Custom separators for Clarion-aware splitting
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        # Define separators optimized for technical documentation
        # Order matters: try larger semantic units first
        if separators is None:
            self.separators = [
                "\n\n## ",      # Major sections (H2)
                "\n\n### ",     # Subsections (H3)
                "\n\n#### ",    # Sub-subsections (H4)
                "\n\n```",      # Code blocks (keep together)
                "\n\n",         # Paragraphs
                "\n",           # Lines
                ". ",           # Sentences
                " ",            # Words
                ""              # Characters (last resort)
            ]
        else:
            self.separators = separators

        # Create LangChain text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=self.separators,
            length_function=len,
            is_separator_regex=False
        )

        logger.info(
            f"Chunker initialized: size={chunk_size}, overlap={chunk_overlap}"
        )

    def chunk_document(
        self,
        text: str,
        metadata: Dict
    ) -> List[Dict]:
        """
        Chunk a single document with metadata preservation.

        Args:
            text: Document text (Markdown)
            metadata: Document metadata

        Returns:
            List of chunk dictionaries with text and metadata
        """
        # Split text into chunks
        text_chunks = self.text_splitter.split_text(text)

        # Create chunk objects with metadata
        chunks = []
        for i, chunk_text in enumerate(text_chunks):
            chunk = {
                'text': chunk_text,
                'metadata': {
                    **metadata,  # Inherit document metadata
                    'chunk_index': i,
                    'chunk_count': len(text_chunks),
                    'chunk_size': len(chunk_text),
                    'is_first': i == 0,
                    'is_last': i == len(text_chunks) - 1
                }
            }
            chunks.append(chunk)

        logger.info(
            f"Chunked {metadata.get('source', 'document')}: "
            f"{len(text)} chars → {len(chunks)} chunks"
        )

        return chunks

    def chunk_documents(
        self,
        documents: List[Dict]
    ) -> List[Dict]:
        """
        Chunk multiple documents.

        Args:
            documents: List of document dictionaries with 'text' and 'metadata'

        Returns:
            List of all chunks from all documents
        """
        all_chunks = []

        for doc in documents:
            doc_chunks = self.chunk_document(doc['text'], doc['metadata'])
            all_chunks.extend(doc_chunks)

        logger.info(
            f"Chunked {len(documents)} documents into {len(all_chunks)} total chunks"
        )

        return all_chunks

    def save_chunks(
        self,
        chunks: List[Dict],
        output_path: str
    ):
        """
        Save chunks to a JSON file for inspection/debugging.

        Args:
            chunks: List of chunk dictionaries
            output_path: Path to save JSON file
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(chunks, f, indent=2, ensure_ascii=False)

        logger.info(f"Saved {len(chunks)} chunks to {output_path}")

    def get_chunk_statistics(
        self,
        chunks: List[Dict]
    ) -> Dict:
        """
        Calculate statistics about chunks.

        Args:
            chunks: List of chunk dictionaries

        Returns:
            Dictionary with chunk statistics
        """
        if not chunks:
            return {}

        chunk_sizes = [len(c['text']) for c in chunks]
        doc_types = {}

        for chunk in chunks:
            doc_type = chunk['metadata'].get('doc_type', 'unknown')
            doc_types[doc_type] = doc_types.get(doc_type, 0) + 1

        stats = {
            'total_chunks': len(chunks),
            'total_characters': sum(chunk_sizes),
            'avg_chunk_size': sum(chunk_sizes) / len(chunks),
            'min_chunk_size': min(chunk_sizes),
            'max_chunk_size': max(chunk_sizes),
            'chunks_by_doc_type': doc_types,
            'unique_documents': len(set(c['metadata']['source'] for c in chunks))
        }

        return stats


def test_chunking():
    """Test the chunking strategy on processed documents."""
    from pathlib import Path

    # Load already-processed markdown files
    processed_dir = Path("data/processed")
    md_files = sorted(processed_dir.glob("*.md"))[:3]  # First 3

    documents = []
    for md_file in md_files:
        text = md_file.read_text(encoding='utf-8')
        doc_name = md_file.stem
        metadata = {
            'source': doc_name,
            'doc_type': 'test',  # Simplified for testing
            'markdown_path': str(md_file)
        }
        documents.append({'text': text, 'metadata': metadata})

    # Chunk the documents
    chunker = ClarionDocumentChunker(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = chunker.chunk_documents(documents)

    # Get and display statistics
    stats = chunker.get_chunk_statistics(chunks)

    print(f"\n=== Chunking Statistics ===")
    print(f"Total chunks: {stats['total_chunks']}")
    print(f"Total characters: {stats['total_characters']:,}")
    print(f"Average chunk size: {stats['avg_chunk_size']:.0f} chars")
    print(f"Min chunk size: {stats['min_chunk_size']}")
    print(f"Max chunk size: {stats['max_chunk_size']}")
    print(f"Unique documents: {stats['unique_documents']}")
    print(f"\nChunks by document type:")
    for doc_type, count in stats['chunks_by_doc_type'].items():
        print(f"  {doc_type}: {count}")

    # Save chunks for inspection
    chunker.save_chunks(chunks, "data/chunks/sample_chunks.json")

    # Display a sample chunk
    print(f"\n=== Sample Chunk ===")
    sample = chunks[10]
    print(f"Source: {sample['metadata']['source']}")
    print(f"Chunk {sample['metadata']['chunk_index'] + 1} of {sample['metadata']['chunk_count']}")
    print(f"Size: {sample['metadata']['chunk_size']} chars")
    print(f"\nText preview (first 300 chars):")
    print(sample['text'][:300] + "...")

    return chunks


if __name__ == "__main__":
    test_chunking()
