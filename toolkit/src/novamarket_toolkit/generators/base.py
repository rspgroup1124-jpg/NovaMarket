"""Base classes for artifact generators."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import ClassVar


class BaseGenerator(ABC):
    """Base class for all artifact generators."""

    artifact_name: ClassVar[str]

    @abstractmethod
    def generate(self, **kwargs) -> str:
        """
        Generate an artifact.

        Parameters
        ----------
        **kwargs
            Generator-specific parameters.

        Returns
        -------
        str
            Generated artifact.
        """
