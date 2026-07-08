"""
PDF document loader.
"""

from pathlib import Path

from pypdf import PdfReader

from app.loaders.base_loader import BaseLoader
from app.models.document import Document


class PDFLoader(BaseLoader):
    """
    Loads PDF documents.
    """

    def load(self, file_path: str) -> Document:
        """
        Load a PDF file and return a Document object.
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        if path.suffix.lower() != ".pdf":
            raise ValueError(f"{file_path} is not a PDF file.")

        reader = PdfReader(path)

        pages = []

        for page in reader.pages:
            text = page.extract_text()

            if text:
                pages.append(text)

        content = "\n".join(pages)

        return Document(
            content=content,
            source=path.name,
            file_type="pdf",
            metadata={
                "pages": len(reader.pages)
            }
        )