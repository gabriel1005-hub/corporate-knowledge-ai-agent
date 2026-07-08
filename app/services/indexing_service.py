"""
Document indexing service.
"""

from pathlib import Path

from app.config.settings import settings
from app.loaders.pdf_loader import PDFLoader
from app.processors.document_processor import DocumentProcessor
from app.rag.chunker import DocumentChunker
from app.utils.file_manager import FileManager
from app.vectorstore.chroma_store import ChromaStore


class IndexingService:
    """
    Handles document indexing.
    """

    def __init__(self):

        self.loader = PDFLoader()
        self.processor = DocumentProcessor()
        self.chunker = DocumentChunker()
        self.vectorstore = ChromaStore()

    def index_document(self, pdf_path: str) -> int:
        """
        Index a single PDF document.
        """

        pdf = Path(pdf_path)

        print(f"\n📄 {pdf.name}")

        print("1️⃣ Loading PDF...")
        document = self.loader.load(str(pdf))

        print("2️⃣ Processing document...")
        document = self.processor.process(document)

        print("3️⃣ Splitting into chunks...")
        chunks = self.chunker.split(document)

        print(f"4️⃣ Generated {len(chunks)} chunks")

        print("5️⃣ Writing to ChromaDB...")
        self.vectorstore.add_documents(chunks)

        print("✅ Indexing completed")

        return len(chunks)

    def index_documents(self):
        """
        Index every PDF inside DOCUMENTS_PATH.
        """

        pdf_files = FileManager.get_pdf_files(
            settings.DOCUMENTS_PATH
        )

        total_chunks = 0

        for pdf in pdf_files:

            total_chunks += self.index_document(
                str(pdf)
            )

        print("\n------------------------------------")
        print(f"Indexed documents : {len(pdf_files)}")
        print(f"Generated chunks  : {total_chunks}")