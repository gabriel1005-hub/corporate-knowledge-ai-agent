"""
Application settings.
"""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    """
    Centralized application configuration.
    """

    LLM_MODEL: str = os.getenv(
        "LLM_MODEL",
        "qwen2.5:3b",
    )

    EMBEDDING_MODEL: str = os.getenv(
        "EMBEDDING_MODEL",
        "nomic-embed-text",
    )

    OLLAMA_BASE_URL: str = os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434",
    )

    VECTOR_DB_PATH: str = "data/vector_db"

    CHUNK_SIZE: int = 1000

    CHUNK_OVERLAP: int = 200

    DOCUMENTS_PATH: str = "data/raw/corporate_docs"


settings = Settings()