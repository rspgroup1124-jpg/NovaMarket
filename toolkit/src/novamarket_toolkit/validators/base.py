"""Base classes for artifact validators."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import ClassVar, Generic, TypeVar

T = TypeVar("T")


class BaseValidator(ABC, Generic[T]):
    """Base class for all artifact validators."""

    artifact_name: ClassVar[str]

    @abstractmethod
    def validate(self, data: T) -> None:
        """
        Validate an artifact.

        Parameters
        ----------
        data
            Domain model to validate.

        Raises
        ------
        ValidationError
            If validation fails.
        """
        raise NotImplementedError
