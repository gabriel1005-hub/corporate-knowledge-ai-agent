"""
Chunking service.
"""

from langchain_core.documents import Document as LangchainDocument
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config.settings import settings
from app.models.document import Document


class DocumentChunker:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
        )

    def split(
        self,
        document: Document,
    ) -> list[LangchainDocument]:

        texts = self.splitter.split_text(
            document.content
        )

        return [
            LangchainDocument(
                page_content=text,
                metadata={
                    **document.metadata,
                    "source": document.source,
                    "file_type": document.file_type,
                },
            )
            for text in texts
        ]