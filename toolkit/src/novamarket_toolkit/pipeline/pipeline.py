"""Pipeline orchestration."""

from __future__ import annotations

from typing import Any

from novamarket_toolkit.generators.factory import GeneratorFactory
from novamarket_toolkit.pipeline.context import PipelineContext
from novamarket_toolkit.pipeline.result import PipelineResult
from novamarket_toolkit.validators.factory import ValidatorFactory


class Pipeline:
    """Orchestrate artifact generation workflow."""

    def __init__(
        self,
        validator_factory: ValidatorFactory | None = None,
        generator_factory: GeneratorFactory | None = None,
    ) -> None:
        """
        Initialize the pipeline.

        Parameters
        ----------
        validator_factory
            Factory responsible for creating validators.
        generator_factory
            Factory responsible for creating generators.
        """
        self._validator_factory = validator_factory
        self._generator_factory = generator_factory

    def generate(
        self,
        artifact_type: str,
        model: Any,
        locale: str = "en",
    ) -> PipelineResult:
        """
        Generate an artifact using the configured pipeline.

        Parameters
        ----------
        artifact_type
            Artifact identifier.
        model
            Domain model used during pipeline execution.
        locale
            Target localization.

        Returns
        -------
        PipelineResult
            Pipeline execution result.
        """
        context = PipelineContext(
            artifact_type=artifact_type,
            model=model,
            locale=locale,
        )

        return self.run(context)

    def run(self, context: PipelineContext) -> PipelineResult:
        """
        Execute the pipeline.

        Parameters
        ----------
        context
            Pipeline execution context.

        Returns
        -------
        PipelineResult
            Pipeline execution result.
        """
        if self._validator_factory is not None:
            validator = self._validator_factory.create(context.artifact_type)
            validator.validate(context.model)

        artifact = context.model

        if self._generator_factory is not None:
            generator = self._generator_factory.create(context.artifact_type)
            artifact = generator.generate(context.model)

        return PipelineResult(
            success=True,
            artifact=artifact,
        )
