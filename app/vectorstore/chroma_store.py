"""
Chroma vector store.
"""

from langchain_chroma import Chroma
from langchain_core.documents import Document as LangchainDocument
from langchain_ollama import OllamaEmbeddings

from app.config.settings import settings


class ChromaStore:
    """
    Wrapper around ChromaDB.
    """

    def __init__(self):

        self.embeddings = OllamaEmbeddings(
            model=settings.EMBEDDING_MODEL
        )

        self.vectorstore = Chroma(
            persist_directory=settings.VECTOR_DB_PATH,
            embedding_function=self.embeddings,
        )

    def add_documents(
        self,
        documents: list[LangchainDocument],
    ):

        self.vectorstore.add_documents(documents)

    def similarity_search(
        self,
        query: str,
        k: int = 4,
    ):

        return self.vectorstore.similarity_search(
            query,
            k=k,
        )