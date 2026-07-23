"""Exceptions for the Pipeline Framework."""

from __future__ import annotations


class PipelineError(Exception):
    """Base exception for all pipeline-related errors."""


class PipelineConfigurationError(PipelineError):
    """Raised when the pipeline configuration is invalid."""


class PipelineExecutionError(PipelineError):
    """Raised when pipeline execution fails."""
