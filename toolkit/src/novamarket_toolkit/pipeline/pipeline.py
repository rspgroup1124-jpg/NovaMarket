"""Pipeline orchestration."""

from __future__ import annotations

from novamarket_toolkit.pipeline.context import PipelineContext
from novamarket_toolkit.pipeline.result import PipelineResult


class Pipeline:
    """Orchestrate artifact generation workflow."""

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
        return PipelineResult(
            success=True,
            artifact=context.model,
        )
