"""Base classes for artifact exporters."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import ClassVar


class BaseExporter(ABC):
    """Base class for all artifact exporters."""

    format_name: ClassVar[str]

    @abstractmethod
    def export(self, content: str) -> str | bytes:
        """
        Export an artifact.

        Parameters
        ----------
        content
            Generated artifact content.

        Returns
        -------
        str | bytes
            Exported artifact.
        """
        raise NotImplementedError
