"""
Query service for NovaCore Knowledge AI.
"""

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

    def ask(self, question: str) -> dict:
        """
        Returns a structured response.
        """

        documents = self.vectorstore.similarity_search(
            question,
            k=5,
        )

        if not documents:

            return {
                "answer": "I could not find that information in the corporate documentation.",
                "sources": [],
            }

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        sources = sorted(
            {
                doc.metadata.get(
                    "source",
                    "Unknown Document",
                )
                for doc in documents
            }
        )

        prompt = f"""
You are NovaCore Knowledge AI.

You are an enterprise knowledge assistant.

Answer ONLY using the provided context.

Never invent information.

If the answer does not exist in the context say exactly:

I could not find that information in the corporate documentation.

Context
-------
{context}

Question
--------
{question}

Answer:
"""

        response = self.llm.invoke(prompt)

        return {
            "answer": response.content.strip(),
            "sources": sources,
        }