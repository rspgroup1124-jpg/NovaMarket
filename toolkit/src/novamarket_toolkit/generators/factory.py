"""Factory for creating artifact generators."""

from __future__ import annotations

from novamarket_toolkit.generators.base import BaseGenerator
from novamarket_toolkit.generators.registry import GeneratorRegistry


class GeneratorFactory:
    """Create generator instances from the registry."""

    def __init__(self, registry: GeneratorRegistry) -> None:
        """
        Initialize the generator factory.

        Parameters
        ----------
        registry
            Registry containing available generators.
        """
        self._registry = registry

    def create(self, artifact_name: str) -> BaseGenerator:
        """
        Create a generator instance.

        Parameters
        ----------
        artifact_name
            Artifact identifier.

        Returns
        -------
        BaseGenerator
            Generator instance.
        """
        generator_class = self._registry.get(artifact_name)
        return generator_class()
