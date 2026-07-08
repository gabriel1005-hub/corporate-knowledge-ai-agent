"""
Document management service.
"""

from datetime import datetime
from pathlib import Path

from app.config.settings import settings


class DocumentService:
    """
    Handles document management.
    """

    def __init__(self):

        self.documents_path = Path(
            settings.DOCUMENTS_PATH
        )

    def list_documents(self):

        documents = []

        if not self.documents_path.exists():
            return documents

        pdfs = sorted(
            self.documents_path.glob("*.pdf"),
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )

        for pdf in pdfs:

            stat = pdf.stat()

            documents.append(
                {
                    "name": pdf.name,
                    "path": pdf,
                    "size_mb": round(
                        stat.st_size / (1024 * 1024),
                        2,
                    ),
                    "uploaded": datetime.fromtimestamp(
                        stat.st_mtime
                    ).strftime("%d %b %Y"),
                    "status": "Indexed",
                    "type": "PDF",
                }
            )

        return documents

    def exists(
        self,
        filename: str,
    ):

        return (
            self.documents_path / filename
        ).exists()

    def save_document(
        self,
        uploaded_file,
    ):

        destination = (
            self.documents_path
            / uploaded_file.name
        )

        with open(destination, "wb") as f:

            f.write(
                uploaded_file.getbuffer()
            )

        return destination

    def delete_document(
        self,
        filename: str,
    ):

        path = (
            self.documents_path / filename
        )

        if path.exists():

            path.unlink()

            return True

        return False

    def get_document(
        self,
        filename: str,
    ):

        for document in self.list_documents():

            if document["name"] == filename:

                return document

        return None