"""Pipeline execution context."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class PipelineContext:
    """
    Immutable context for pipeline execution.

    Parameters
    ----------
    artifact_type
        Type of artifact to generate.
    model
        Domain model passed to the pipeline.
    locale
        Target localization.
    """

    artifact_type: str
    model: Any
    locale: str = "en"
