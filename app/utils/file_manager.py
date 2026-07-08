"""
File management utilities.
"""

from pathlib import Path


class FileManager:
    """
    Handles document discovery.
    """

    @staticmethod
    def get_pdf_files(directory: str) -> list[Path]:
        """
        Return all PDF files inside a directory.
        """
        return sorted(Path(directory).glob("*.pdf"))