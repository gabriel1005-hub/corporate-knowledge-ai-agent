"""
Retriever module.

Provides a unified interface for retrieving relevant
documents from the vector database.
"""

from app.rag.retrieval_config import RetrievalConfig
from app.vectorstore.chroma_store import ChromaStore


class Retriever:
    """
    Enterprise Retriever.

    Responsible only for retrieving relevant documents.
    """

    def __init__(self):

        self.vectorstore = ChromaStore()

    # -------------------------------------------------
    # PUBLIC
    # -------------------------------------------------

    def retrieve(
        self,
        question: str,
        config: RetrievalConfig | None = None,
    ):
        """
        Retrieve documents using the configured strategy.

        Parameters
        ----------
        question : str
            User question.

        config : RetrievalConfig | None
            Retrieval configuration.

        Returns
        -------
        list
            Retrieved LangChain documents.
        """

        if config is None:

            config = RetrievalConfig()

        documents = []

        # -------------------------------------------------
        # Vector Search
        # -------------------------------------------------

        if config.use_vector_search:

            documents = self.vectorstore.similarity_search(
                query=question,
                k=config.top_k,
            )

        # -------------------------------------------------
        # Similarity Threshold
        # (Reserved for future implementation)
        # -------------------------------------------------

        if config.similarity_threshold > 0:

            # Chroma similarity_search() currently does not
            # expose scores in this implementation.
            # This section is intentionally left as a hook
            # for future similarity_search_with_score().
            pass

        # -------------------------------------------------
        # Keyword Search
        # (Reserved for Hybrid Retrieval)
        # -------------------------------------------------

        if config.use_keyword_search:

            # Future implementation:
            #
            # keyword_documents =
            #     self.keyword_search(...)
            #
            # documents =
            #     self.merge_results(
            #         documents,
            #         keyword_documents,
            #     )
            #
            pass

        return documents

    # -------------------------------------------------
    # FUTURE EXTENSIONS
    # -------------------------------------------------

    def keyword_search(
        self,
        question: str,
    ):
        """
        Placeholder for BM25 / keyword search.

        Returns
        -------
        list
        """

        return []

    def merge_results(
        self,
        vector_results,
        keyword_results,
    ):
        """
        Placeholder for Reciprocal Rank Fusion (RRF)
        or hybrid ranking.
        """

        return vector_results