"""
PDF Processor v3 - Simple approach: Use raw text extraction
This preserves ALL indentation by using PyMuPDF's raw text mode
"""

import pymupdf
from pathlib import Path
from typing import Dict, List, Optional
import logging
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ClarionPDFProcessorV3:
    """
    Simplified processor that uses raw text extraction.
    Preserves indentation at the cost of some formatting.
    """

    def __init__(self, output_dir: str = "data/processed"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"PDF Processor V3 initialized (raw text mode)")

    def classify_doc_type(self, doc_name: str) -> str:
        """Classify document type based on filename."""
        doc_name_lower = doc_name.lower()

        if any(term in doc_name_lower for term in [
            'languageprogramming', 'languagereference', 'learningclarion'
        ]):
            return 'core_language'
        elif any(term in doc_name_lower for term in [
            'ide', 'gettingstarted', 'quickref'
        ]):
            return 'ide_development'
        elif any(term in doc_name_lower for term in [
            'advanced', 'programming'
        ]):
            return 'advanced'
        elif any(term in doc_name_lower for term in [
            'abc', 'internet', 'businessmath', 'library'
        ]):
            return 'libraries'
        elif 'template' in doc_name_lower:
            return 'templates'
        elif any(term in doc_name_lower for term in [
            'database', 'xml', 'report', 'broker'
        ]):
            return 'specialized'
        elif any(term in doc_name_lower for term in [
            'subversion', 'faq', 'tips', 'tricks'
        ]):
            return 'utilities'
        else:
            return 'other'

    def enhance_formatting(self, raw_text: str) -> str:
        """
        Add minimal markdown formatting to raw text.
        Preserves indentation while adding structure.
        """
        lines = raw_text.split('\n')
        enhanced = []

        for line in lines:
            # Detect headings (all caps lines)
            if line.strip() and line.strip().isupper() and len(line.strip()) > 3:
                # Make it a heading
                enhanced.append(f"## {line.strip()}")
            # Detect code blocks (lines with PROCEDURE, MAP, etc.)
            elif re.match(r'^\s*(MAP|CODE|END|PROCEDURE|PROGRAM|MODULE|MEMBER)\b', line):
                # Preserve indentation for code
                enhanced.append(line)
            else:
                enhanced.append(line)

        return '\n'.join(enhanced)

    def process_pdf(
        self,
        pdf_path: str,
        save_markdown: bool = True
    ) -> Dict:
        """
        Convert PDF using raw text extraction (preserves indentation).

        Args:
            pdf_path: Path to PDF file
            save_markdown: Whether to save markdown to disk

        Returns:
            Dictionary containing text and metadata
        """
        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        logger.info(f"Processing PDF (v3 - raw text): {pdf_path.name}")

        try:
            # Open PDF and extract raw text (preserves spacing)
            doc = pymupdf.open(str(pdf_path))

            pages_text = []
            for page_num, page in enumerate(doc):
                # Use 'text' mode which preserves indentation
                page_text = page.get_text("text")
                pages_text.append(page_text)

            doc.close()

            # Join all pages
            raw_text = '\n\n---\n\n'.join(pages_text)

            # Add minimal formatting
            enhanced_text = self.enhance_formatting(raw_text)

            # Extract metadata
            doc_name = pdf_path.stem
            doc_type = self.classify_doc_type(doc_name)

            metadata = {
                'source': doc_name,
                'doc_type': doc_type,
                'original_path': str(pdf_path),
                'char_count': len(enhanced_text),
                'line_count': len(enhanced_text.split('\n')),
                'version': 'v3_raw_text_indentation_preserved'
            }

            # Save if requested
            if save_markdown:
                output_path = self.output_dir / f"{doc_name}.md"
                output_path.write_text(enhanced_text, encoding='utf-8')
                metadata['markdown_path'] = str(output_path)
                logger.info(f"Saved to: {output_path}")

            logger.info(f"✓ {doc_name}: {metadata['char_count']} chars")

            return {
                'text': enhanced_text,
                'metadata': metadata
            }

        except Exception as e:
            logger.error(f"Error processing {pdf_path.name}: {str(e)}")
            raise

    def process_directory(
        self,
        pdf_dir: str,
        file_pattern: str = "*.pdf",
        limit: Optional[int] = None
    ) -> List[Dict]:
        """Process all PDFs in directory."""
        pdf_dir = Path(pdf_dir)
        pdf_files = sorted(pdf_dir.glob(file_pattern))

        if limit:
            pdf_files = pdf_files[:limit]

        logger.info(f"Processing {len(pdf_files)} PDFs (v3 - indentation preserved)")

        results = []
        for pdf_file in pdf_files:
            try:
                result = self.process_pdf(pdf_file)
                results.append(result)
            except Exception as e:
                logger.error(f"Skipping {pdf_file.name}: {e}")
                continue

        logger.info(f"✓ Processed {len(results)}/{len(pdf_files)} PDFs")
        return results


if __name__ == "__main__":
    # Quick test
    proc = ClarionPDFProcessorV3()
    result = proc.process_pdf("Documents/LearningClarion.pdf")

    # Check for MAP with indentation
    if ' MAP' in result['text']:
        print("✓ Indentation preserved!")
    else:
        print("✗ Indentation lost")
