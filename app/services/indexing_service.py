"""
Document indexing service.
"""

from app.config.settings import settings
from app.loaders.pdf_loader import PDFLoader
from app.processors.document_processor import DocumentProcessor
from app.rag.chunker import DocumentChunker
from app.utils.file_manager import FileManager
from app.vectorstore.chroma_store import ChromaStore


class IndexingService:

    def __init__(self):

        self.loader = PDFLoader()
        self.processor = DocumentProcessor()
        self.chunker = DocumentChunker()
        self.vectorstore = ChromaStore()

    def index_documents(self):

        pdf_files = FileManager.get_pdf_files(
            settings.DOCUMENTS_PATH
        )

        total_chunks = 0

        for pdf in pdf_files:

            print(f"📄 {pdf.name}")

            document = self.loader.load(str(pdf))

            document = self.processor.process(document)

            chunks = self.chunker.split(document)

            self.vectorstore.add_documents(chunks)

            total_chunks += len(chunks)

        print("\n------------------------------------")
        print(f"Indexed documents : {len(pdf_files)}")
        print(f"Generated chunks  : {total_chunks}")