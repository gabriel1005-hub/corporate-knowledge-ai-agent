"""
Enterprise Query Service.

Coordinates the RAG pipeline.
"""

import time

from app.llm.llm_service import LLMService
from app.rag.prompt_builder import PromptBuilder
from app.rag.retrieval_config import RetrievalConfig
from app.rag.retriever import Retriever


class QueryService:
    """
    Enterprise RAG Orchestrator.
    """

    def __init__(self):

        self.retriever = Retriever()

        self.llm = LLMService()

    # -------------------------------------------------

    def ask(
        self,
        question: str,
        conversation_context: str = "",
    ) -> dict:
        """
        Execute the complete RAG pipeline.
        """

        config = RetrievalConfig()

        # ---------------------------------------------
        # Retrieval
        # ---------------------------------------------

        retrieval_start = time.perf_counter()

        documents = self.retriever.retrieve(
            question=question,
            config=config,
        )

        retrieval_time = (
            time.perf_counter()
            - retrieval_start
        )

        # ---------------------------------------------
        # No results
        # ---------------------------------------------

        if not documents:

            return {

                "answer":
                (
                    "I could not find that "
                    "information in the "
                    "corporate documentation."
                ),

                "sources": [],

                "retrieved_chunks": [],

                "context": "",

                "metrics": {

                    "documents": 0,

                    "retrieval_time":
                    retrieval_time,

                    "generation_time": 0,

                    "total_time":
                    retrieval_time,

                },

            }

        # ---------------------------------------------
        # Context
        # ---------------------------------------------

        context = "\n\n".join(

            document.page_content

            for document in documents

        )

        # ---------------------------------------------
        # Sources
        # ---------------------------------------------

        sources = []

        retrieved_chunks = []

        seen = set()

        for document in documents:

            source = document.metadata.get(
                "source",
                "Unknown",
            )

            chunk = document.metadata.get(
                "chunk_id",
                "-",
            )

            retrieved_chunks.append(
                {
                    "document": source,
                    "chunk": chunk,
                    "preview":
                    document.page_content[:250],
                }
            )

            key = (
                source,
                chunk,
            )

            if key not in seen:

                seen.add(key)

                sources.append(
                    {
                        "document": source,
                        "chunk": chunk,
                    }
                )

        # ---------------------------------------------
        # Prompt
        # ---------------------------------------------

        prompt = PromptBuilder.build(

            question=question,

            retrieved_context=context,

            conversation_context=conversation_context,

        )

        # ---------------------------------------------
        # Generation
        # ---------------------------------------------

        generation_start = time.perf_counter()

        answer = self.llm.generate(
            prompt
        )

        generation_time = (
            time.perf_counter()
            - generation_start
        )

        # ---------------------------------------------
        # Response
        # ---------------------------------------------

        return {

            "answer": answer,

            "sources": sources,

            "retrieved_chunks":
            retrieved_chunks,

            "context": context,

            "metrics": {

                "documents":
                len(documents),

                "retrieval_time":
                retrieval_time,

                "generation_time":
                generation_time,

                "total_time":
                retrieval_time
                + generation_time,

            },

        }