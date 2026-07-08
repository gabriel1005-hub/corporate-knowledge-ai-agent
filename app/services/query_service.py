"""
Query service for NovaCore Knowledge AI.
"""

from langchain_ollama import ChatOllama

from app.config.settings import settings
from app.vectorstore.chroma_store import ChromaStore


class QueryService:
    """
    Handles question answering using Chroma + Ollama.
    """

    def __init__(self):

        self.vectorstore = ChromaStore()

        self.llm = ChatOllama(
            model=settings.LLM_MODEL,
            temperature=0,
        )

    def ask(self, question: str) -> str:

        documents = self.vectorstore.similarity_search(
            question,
            k=5,
        )

        if not documents:
            return "No relevant information was found."

        context = "\n\n".join(
            doc.page_content for doc in documents
        )

        sources = sorted(
            {
                doc.metadata.get("source", "Unknown")
                for doc in documents
            }
        )

        prompt = f"""
You are NovaCore Knowledge AI.

Answer ONLY using the provided context.

If the answer is not contained in the context, reply exactly:

I could not find that information in the corporate documentation.

Context:

{context}

Question:

{question}
"""

        response = self.llm.invoke(prompt)

        answer = response.content

        answer += "\n\nSources:\n"

        for source in sources:
            answer += f"- {source}\n"

        return answer