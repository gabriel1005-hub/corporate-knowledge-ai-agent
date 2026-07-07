from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Document:
    """
    Represents a processed document ready for indexing.
    """

    content: str

    source: str

    file_type: str

    metadata: Dict = field(default_factory=dict)