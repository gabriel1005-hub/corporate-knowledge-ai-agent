"""
System information service.
"""

from pathlib import Path

from app.config.settings import settings
from app.vectorstore.chroma_store import ChromaStore


class SystemService:
    """
    Provides runtime statistics for the application.
    """

    def __init__(self):

        self.documents_path = Path(
            settings.DOCUMENTS_PATH
        )

    def get_stats(self):

        stats = {
            "documents": 0,
            "chunks": 0,
            "embedding_model": settings.EMBEDDING_MODEL,
            "llm_model": settings.LLM_MODEL,
        }

        # -------------------------
        # Documents
        # -------------------------

        if self.documents_path.exists():

            pdfs = list(
                self.documents_path.glob("*.pdf")
            )

            stats["documents"] = len(pdfs)

        # -------------------------
        # Chunks
        # -------------------------

        try:

            store = ChromaStore()

            collection = store.vectorstore._collection

            stats["chunks"] = collection.count()

        except Exception:

            stats["chunks"] = 0

        return stats