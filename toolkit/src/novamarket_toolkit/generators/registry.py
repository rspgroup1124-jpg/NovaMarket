"""Registry for artifact generators."""

from __future__ import annotations

from typing import Type

from novamarket_toolkit.generators.base import BaseGenerator
from novamarket_toolkit.generators.exceptions import (
    DuplicateGeneratorError,
    GeneratorNotFoundError,
)


class GeneratorRegistry:
    """Store and manage registered generator classes."""

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._generators: dict[str, Type[BaseGenerator]] = {}

    def register(self, generator_class: Type[BaseGenerator]) -> None:
        """
        Register a generator class.

        Parameters
        ----------
        generator_class
            Generator class to register.

        Raises
        ------
        ValueError
            If the generator does not define an artifact name.

        DuplicateGeneratorError
            If the generator is already registered.
        """
        artifact_name = getattr(generator_class, "artifact_name", "").strip()

        if not artifact_name:
            raise ValueError("Generator class must define a non-empty 'artifact_name'.")

        if artifact_name in self._generators:
            raise DuplicateGeneratorError(f"Generator '{artifact_name}' is already registered.")

        self._generators[artifact_name] = generator_class

    def get(self, artifact_name: str) -> Type[BaseGenerator]:
        """
        Return a registered generator class.

        Parameters
        ----------
        artifact_name
            Artifact identifier.

        Raises
        ------
        GeneratorNotFoundError
            If the generator is not registered.
        """
        try:
            return self._generators[artifact_name]
        except KeyError as error:
            raise GeneratorNotFoundError(
                f"Generator '{artifact_name}' is not registered."
            ) from error

    def is_registered(self, artifact_name: str) -> bool:
        """
        Return True if the generator is registered.
        """
        return artifact_name in self._generators

    def registered_generators(self) -> tuple[str, ...]:
        """
        Return names of all registered generators.

        Returns
        -------
        tuple[str, ...]
            Registered artifact names sorted alphabetically.
        """
        return tuple(sorted(self._generators))
