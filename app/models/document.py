"""
Document model.

Defines the structure used across the application to represent
a processed document ready for indexing.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Document:
    """
    Represents a processed document.

    Attributes
    ----------
    content : str
        Extracted textual content.

    source : str
        Original filename or document path.

    file_type : str
        Document extension (pdf, csv, docx, etc.).

    metadata : dict[str, Any]
        Additional document information.
    """

    content: str
    source: str
    file_type: str
    metadata: dict[str, Any] = field(default_factory=dict)