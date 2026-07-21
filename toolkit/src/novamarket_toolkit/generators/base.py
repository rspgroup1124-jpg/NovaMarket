"""Base classes for artifact generators."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import ClassVar, Generic, TypeVar

T = TypeVar("T")


class BaseGenerator(ABC, Generic[T]):
    """Base class for all artifact generators."""

    artifact_name: ClassVar[str]

    @abstractmethod
    def generate(self, data: T) -> str:
        """
        Generate an artifact.

        Parameters
        ----------
        data
            Domain model used to generate the artifact.

        Returns
        -------
        str
            Generated artifact.
        """
        raise NotImplementedError
