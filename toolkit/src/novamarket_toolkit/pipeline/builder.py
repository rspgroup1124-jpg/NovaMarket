"""Pipeline builder."""

from __future__ import annotations

from novamarket_toolkit.pipeline.pipeline import Pipeline


class PipelineBuilder:
    """Build pipeline instances."""

    def build(self) -> Pipeline:
        """
        Build a pipeline instance.

        Returns
        -------
        Pipeline
            Configured pipeline instance.
        """
        return Pipeline()
