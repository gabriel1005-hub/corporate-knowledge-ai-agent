"""
Application settings.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """
    Centralized application configuration.
    """

    LLM_MODEL: str = "qwen2.5:3b"

    EMBEDDING_MODEL: str = "nomic-embed-text"

    VECTOR_DB_PATH: str = "data/vector_db"

    CHUNK_SIZE: int = 1000

    CHUNK_OVERLAP: int = 200

    DOCUMENTS_PATH: str = "data/raw/corporate_docs"


settings = Settings()