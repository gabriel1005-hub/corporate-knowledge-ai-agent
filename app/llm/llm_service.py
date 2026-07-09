"""
LLM service.
"""

from langchain_ollama import ChatOllama

from app.config.settings import settings


class LLMService:
    """
    Wrapper around ChatOllama.
    """

    def __init__(self):

        self.llm = ChatOllama(
            model=settings.LLM_MODEL,
            temperature=0,
        )

    def generate(
        self,
        prompt: str,
    ):

        response = self.llm.invoke(
            prompt
        )

        return response.content.strip()