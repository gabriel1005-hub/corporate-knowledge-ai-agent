"""
Retrieval configuration.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class RetrievalConfig:
    """
    Configuration for retrieval.
    """

    top_k: int = 5

    use_vector_search: bool = True

    use_keyword_search: bool = False

    similarity_threshold: float = 0.0