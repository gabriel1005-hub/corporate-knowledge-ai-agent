"""
System information service.
"""

from pathlib import Path

from app.config.settings import settings
from app.vectorstore.chroma_store import ChromaStore


class SystemService:
    """
    Provides system metrics for the Streamlit UI.
    """

    def __init__(self):

        self.store = ChromaStore()

    def get_stats(self) -> dict:

        stats = {
            "documents": 0,
            "chunks": 0,
            "embedding_model": settings.EMBEDDING_MODEL,
            "llm_model": settings.LLM_MODEL,
            "status": "Ready",
        }

        # -------------------------
        # Documents
        # -------------------------

        data_path = Path(settings.DOCUMENTS_PATH)

        if data_path.exists():

            stats["documents"] = len(
                list(data_path.glob("*.pdf"))
            )

        # -------------------------
        # Chunks
        # -------------------------

        try:

            collection = self.store.vectorstore._collection

            stats["chunks"] = collection.count()

        except Exception:

            stats["chunks"] = 0

        return stats