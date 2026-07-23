"""Pipeline execution result."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class PipelineResult:
    """
    Result of pipeline execution.

    Parameters
    ----------
    success
        Whether the pipeline completed successfully.
    artifact
        Generated artifact.
    """

    success: bool
    artifact: Any | None = None
