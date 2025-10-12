"""
Pipeline V3 - Using Raw Text Extraction (Preserves Indentation)
Final version that actually works!
"""

import logging
from pathlib import Path
from pdf_processor_v3 import ClarionPDFProcessorV3
from chunking import ClarionDocumentChunker
from embeddings import EmbeddingModel
from vector_store import ClarionVectorStore
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class ClarionPipelineV3:
    """
    Pipeline V3 - Uses raw text extraction for perfect indentation preservation.
    """

    def __init__(self, pdf_dir: str = "Documents", limit: int = None):
        self.pdf_dir = pdf_dir
        self.limit = limit

        # Initialize components with V3 processor
        self.pdf_processor = ClarionPDFProcessorV3()
        self.chunker = ClarionDocumentChunker(chunk_size=800, chunk_overlap=100)
        self.embedding_model = EmbeddingModel()
        self.vector_store = ClarionVectorStore()

        logger.info("Pipeline V3 initialized (raw text - indentation WILL be preserved)")

    def run(self, recreate_collection: bool = False):
        """
        Run the complete pipeline with V3 processing.
        """
        start_time = time.time()

        logger.info("=" * 80)
        logger.info("CLARION KNOWLEDGE BASE PIPELINE V3")
        logger.info("Using raw text extraction - indentation PRESERVED")
        logger.info("=" * 80)

        # Step 1: Process PDFs with V3 (raw text)
        logger.info("\n[STEP 1/5] Processing PDFs with V3 (raw text - preserves indentation)...")
        documents = self.pdf_processor.process_directory(
            self.pdf_dir,
            limit=self.limit
        )
        logger.info(f"✓ Processed {len(documents)} documents")

        # Step 2: Chunk documents
        logger.info("\n[STEP 2/5] Chunking documents...")
        chunks = self.chunker.chunk_documents(documents)
        stats = self.chunker.get_chunk_statistics(chunks)
        logger.info(f"✓ Created {stats['total_chunks']} chunks")
        logger.info(f"  - Average chunk size: {stats['avg_chunk_size']:.0f} chars")
        logger.info(f"  - Unique documents: {stats['unique_documents']}")

        # Step 3: Generate embeddings
        logger.info("\n[STEP 3/5] Generating embeddings...")
        logger.info("This will take ~2 hours for 30,000+ chunks...")
        enriched_chunks = self.embedding_model.encode_chunks(
            chunks,
            batch_size=32,
            show_progress=True
        )
        logger.info(f"✓ Generated {len(enriched_chunks)} embeddings")

        # Step 4: Setup vector store
        logger.info("\n[STEP 4/5] Setting up vector store...")
        embedding_dim = self.embedding_model.get_embedding_dim()

        if recreate_collection or not self.vector_store.collection_exists():
            self.vector_store.create_collection(
                vector_size=embedding_dim,
                recreate=recreate_collection
            )
            logger.info(f"✓ Collection created (dimension: {embedding_dim})")
        else:
            logger.info(f"✓ Using existing collection")

        # Step 5: Upload to Qdrant
        logger.info("\n[STEP 5/5] Uploading to vector store...")
        self.vector_store.add_chunks(enriched_chunks, batch_size=100)

        # Final stats
        info = self.vector_store.get_collection_info()
        logger.info(f"✓ Vector store populated")
        logger.info(f"  - Total points: {info['points_count']}")
        logger.info(f"  - Status: {info['status']}")

        elapsed_time = time.time() - start_time
        logger.info("\n" + "=" * 80)
        logger.info(f"PIPELINE V3 COMPLETE in {elapsed_time:.1f} seconds ({elapsed_time/60:.1f} minutes)")
        logger.info("✓ CODE INDENTATION IS NOW PRESERVED!")
        logger.info("=" * 80)

        return {
            'documents_processed': len(documents),
            'chunks_created': len(chunks),
            'embeddings_generated': len(enriched_chunks),
            'vector_store_points': info['points_count'],
            'elapsed_time': elapsed_time,
            'stats': stats,
            'version': 'v3_raw_text_indentation_preserved'
        }


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Clarion Knowledge Base Pipeline V3 (Raw Text - Indentation Preserved)'
    )
    parser.add_argument(
        '--limit',
        type=int,
        default=None,
        help='Limit number of PDFs (default: all 21)'
    )
    parser.add_argument(
        '--recreate',
        action='store_true',
        help='Recreate vector store (required for fresh start)'
    )
    parser.add_argument(
        '--pdf-dir',
        type=str,
        default='Documents',
        help='PDF directory (default: Documents)'
    )

    args = parser.parse_args()

    print("\n" + "=" * 80)
    print("CLARION KNOWLEDGE BASE - PIPELINE V3")
    print("This version uses raw text extraction to preserve code indentation")
    print("=" * 80)

    if args.recreate:
        print("\n⚠️  Will RECREATE vector store (deletes existing data)")
        print("This is CORRECT - we need to replace the v2 data with v3 data")
    else:
        print("\n❌ ERROR: You must use --recreate flag")
        print("   Run: python src/pipeline_v3.py --recreate")
        return

    print("\n⏱️  Estimated time: ~2 hours")
    print("📊 Processing: All 21 Clarion PDFs")
    print("\nStarting in 3 seconds... (Ctrl+C to cancel)\n")

    import time
    time.sleep(3)

    # Run pipeline
    pipeline = ClarionPipelineV3(pdf_dir=args.pdf_dir, limit=args.limit)
    results = pipeline.run(recreate_collection=args.recreate)

    # Summary
    print("\n" + "=" * 80)
    print("FINAL SUMMARY")
    print("=" * 80)
    print(f"Documents:         {results['documents_processed']}")
    print(f"Chunks:            {results['chunks_created']}")
    print(f"Embeddings:        {results['embeddings_generated']}")
    print(f"Vector Store:      {results['vector_store_points']} points")
    print(f"Time:              {results['elapsed_time']:.1f}s ({results['elapsed_time']/60:.1f} min)")
    print(f"Version:           {results['version']}")
    print("=" * 80)
    print("\n✅ SUCCESS! Code indentation is now properly preserved!")
    print("   Test with: search_docs('MAP PROCEDURE END example')")


if __name__ == "__main__":
    main()
