"""
Query service for NovaCore Knowledge AI.
"""

import time

from langchain_ollama import ChatOllama

from app.config.settings import settings
from app.vectorstore.chroma_store import ChromaStore


class QueryService:
    """
    Enterprise RAG query service.
    """

    def __init__(self):

        self.vectorstore = ChromaStore()

        self.llm = ChatOllama(
            model=settings.LLM_MODEL,
            temperature=0,
        )

    def ask(
        self,
        question: str,
    ) -> dict:

        retrieval_start = time.perf_counter()

        documents = (
            self.vectorstore.similarity_search(
                question,
                k=5,
            )
        )

        retrieval_time = (
            time.perf_counter()
            - retrieval_start
        )

        if not documents:

            return {

                "answer":
                "I could not find that information in the corporate documentation.",

                "sources":[],

                "retrieved_chunks":[],

                "context":"",

                "metrics":{

                    "documents":0,

                    "retrieval_time":retrieval_time,

                    "generation_time":0,

                    "total_time":retrieval_time,

                }

            }

        context = "\n\n".join(

            doc.page_content

            for doc in documents

        )

        retrieved_chunks = []

        sources = []

        seen = set()

        for doc in documents:

            source = doc.metadata.get(
                "source",
                "Unknown"
            )

            chunk = doc.metadata.get(
                "chunk_id",
                "-"
            )

            retrieved_chunks.append(
                {
                    "document":source,
                    "chunk":chunk,
                    "preview":doc.page_content[:250]
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
                        "document":source,
                        "chunk":chunk,
                    }
                )

        prompt = f"""
You are NovaCore Knowledge AI.

Answer ONLY using the provided context.

Never invent information.

Context
-------
{context}

Question
--------
{question}

Answer:
"""

        generation_start = (
            time.perf_counter()
        )

        response = self.llm.invoke(
            prompt
        )

        generation_time = (
            time.perf_counter()
            - generation_start
        )

        return {

            "answer":
            response.content.strip(),

            "sources":
            sources,

            "retrieved_chunks":
            retrieved_chunks,

            "context":
            context,

            "metrics":{

                "documents":
                len(documents),

                "retrieval_time":
                retrieval_time,

                "generation_time":
                generation_time,

                "total_time":
                retrieval_time +
                generation_time,

            }

        }