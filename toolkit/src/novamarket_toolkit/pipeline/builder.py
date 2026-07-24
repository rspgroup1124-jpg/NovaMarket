"""Pipeline builder."""

from __future__ import annotations

from novamarket_toolkit.generators.factory import GeneratorFactory
from novamarket_toolkit.generators.registry import GeneratorRegistry
from novamarket_toolkit.pipeline.pipeline import Pipeline
from novamarket_toolkit.validators.factory import ValidatorFactory
from novamarket_toolkit.validators.registry import ValidatorRegistry


class PipelineBuilder:
    """Build configured pipeline instances."""

    def __init__(self) -> None:
        """Initialize the pipeline builder."""
        self._validator_registry: ValidatorRegistry | None = None
        self._generator_registry: GeneratorRegistry | None = None

    def with_validator_registry(
        self,
        registry: ValidatorRegistry,
    ) -> PipelineBuilder:
        """
        Configure the validator registry.

        Parameters
        ----------
        registry
            Registry containing available validators.

        Returns
        -------
        PipelineBuilder
            Current builder instance.
        """
        self._validator_registry = registry
        return self

    def with_generator_registry(
        self,
        registry: GeneratorRegistry,
    ) -> PipelineBuilder:
        """
        Configure the generator registry.

        Parameters
        ----------
        registry
            Registry containing available generators.

        Returns
        -------
        PipelineBuilder
            Current builder instance.
        """
        self._generator_registry = registry
        return self

    def build(self) -> Pipeline:
        """
        Build a configured pipeline instance.

        Returns
        -------
        Pipeline
            Configured pipeline instance.
        """
        validator_factory = (
            ValidatorFactory(self._validator_registry)
            if self._validator_registry is not None
            else None
        )

        generator_factory = (
            GeneratorFactory(self._generator_registry)
            if self._generator_registry is not None
            else None
        )

        return Pipeline(
            validator_factory=validator_factory,
            generator_factory=generator_factory,
        )
