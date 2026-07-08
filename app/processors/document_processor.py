"""
Document processor.

Responsible for cleaning and normalizing document content.
"""

import re

from app.models.document import Document


class DocumentProcessor:
    """
    Cleans document text before chunking.
    """

    def process(self, document: Document) -> Document:
        """
        Normalize document content.
        """

        text = document.content

        # Replace multiple spaces with a single space
        text = re.sub(r"[ \t]+", " ", text)

        # Replace 3+ line breaks with only 2
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Remove leading/trailing spaces
        text = text.strip()

        return Document(
            content=text,
            source=document.source,
            file_type=document.file_type,
            metadata=document.metadata,
        )