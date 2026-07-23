"""Factory for creating artifact validators."""

from __future__ import annotations

from novamarket_toolkit.validators.base import BaseValidator
from novamarket_toolkit.validators.registry import ValidatorRegistry


class ValidatorFactory:
    """Create validator instances from the registry."""

    def __init__(self, registry: ValidatorRegistry) -> None:
        """
        Initialize the validator factory.

        Parameters
        ----------
        registry
            Registry containing available validators.
        """
        self._registry = registry

    def create(self, artifact_name: str) -> BaseValidator:
        """
        Create a validator instance.

        Parameters
        ----------
        artifact_name
            Artifact identifier.

        Returns
        -------
        BaseValidator
            Validator instance.
        """
        validator_class = self._registry.get(artifact_name)
        return validator_class()
