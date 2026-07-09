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
            model=settings.EMBEDDING_MODEL,
            base_url=settings.OLLAMA_BASE_URL,
        )

        self.vectorstore = Chroma(
            persist_directory=settings.VECTOR_DB_PATH,
            embedding_function=self.embeddings,
        )

    # -------------------------------------------------
    # ADD DOCUMENTS
    # -------------------------------------------------

    def add_documents(
        self,
        documents: list[LangchainDocument],
    ):

        self.vectorstore.add_documents(documents)

    # -------------------------------------------------
    # SEARCH
    # -------------------------------------------------

    def similarity_search(
        self,
        query: str,
        k: int = 4,
    ):

        return self.vectorstore.similarity_search(
            query=query,
            k=k,
        )

    # -------------------------------------------------
    # DELETE DOCUMENT
    # -------------------------------------------------

    def delete_document(
        self,
        document_name: str,
    ) -> bool:

        try:

            self.vectorstore.delete(
                where={
                    "document_id": document_name
                }
            )

            return True

        except Exception as e:

            print(e)

            return False

    # -------------------------------------------------
    # COLLECTION
    # -------------------------------------------------

    @property
    def collection(self):

        return self.vectorstore._collection