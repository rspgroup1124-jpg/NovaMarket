"""Registry for artifact validators."""

from __future__ import annotations

from typing import Type

from novamarket_toolkit.validators.base import BaseValidator
from novamarket_toolkit.validators.exceptions import (
    DuplicateValidatorError,
    ValidatorNotFoundError,
)


class ValidatorRegistry:
    """Store and manage registered validator classes."""

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._validators: dict[str, Type[BaseValidator]] = {}

    def register(self, validator_class: Type[BaseValidator]) -> None:
        """
        Register a validator class.

        Parameters
        ----------
        validator_class
            Validator class to register.

        Raises
        ------
        ValueError
            If the validator does not define an artifact name.

        DuplicateValidatorError
            If the validator is already registered.
        """
        artifact_name = getattr(validator_class, "artifact_name", "").strip()

        if not artifact_name:
            raise ValueError("Validator class must define a non-empty 'artifact_name'.")

        if artifact_name in self._validators:
            raise DuplicateValidatorError(f"Validator '{artifact_name}' is already registered.")

        self._validators[artifact_name] = validator_class

    def get(self, artifact_name: str) -> Type[BaseValidator]:
        """
        Return a registered validator class.

        Parameters
        ----------
        artifact_name
            Artifact identifier.

        Raises
        ------
        ValidatorNotFoundError
            If the validator is not registered.
        """
        try:
            return self._validators[artifact_name]
        except KeyError as error:
            raise ValidatorNotFoundError(
                f"Validator '{artifact_name}' is not registered."
            ) from error

    def is_registered(self, artifact_name: str) -> bool:
        """
        Return True if the validator is registered.
        """
        return artifact_name in self._validators

    def registered_validators(self) -> tuple[str, ...]:
        """
        Return names of all registered validators.

        Returns
        -------
        tuple[str, ...]
            Registered artifact names sorted alphabetically.
        """
        return tuple(sorted(self._validators))
