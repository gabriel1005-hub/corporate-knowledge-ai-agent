"""
Base loader interface.

Every document loader must inherit from this class.
"""

from abc import ABC, abstractmethod

from app.models.document import Document


class BaseLoader(ABC):
    """
    Abstract base class for all document loaders.
    """

    @abstractmethod
    def load(self, file_path: str) -> Document:
        """
        Load a document.

        Parameters
        ----------
        file_path : str
            Path to the input file.

        Returns
        -------
        Document
            Parsed document.
        """
        raise NotImplementedError