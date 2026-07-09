"""
Structured query response model.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class QueryMetrics:
    """
    Performance metrics.
    """

    documents: int

    retrieval_time: float

    generation_time: float

    total_time: float


@dataclass(slots=True)
class RetrievedChunk:
    """
    Retrieved chunk metadata.
    """

    document: str

    chunk: int | str

    preview: str


@dataclass(slots=True)
class QueryResponse:
    """
    Structured RAG response.
    """

    answer: str

    sources: list[dict]

    retrieved_chunks: list[RetrievedChunk]

    context: str

    metrics: QueryMetrics

    prompt: str = ""

    llm: str = ""