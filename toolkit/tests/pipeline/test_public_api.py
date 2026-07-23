"""Tests for the public Pipeline API."""

from __future__ import annotations


def test_pipeline_public_api_imports() -> None:
    """Public Pipeline API should expose the expected classes."""
    from novamarket_toolkit.pipeline import (
        Pipeline,
        PipelineBuilder,
        PipelineConfigurationError,
        PipelineContext,
        PipelineError,
        PipelineExecutionError,
        PipelineResult,
    )

    assert Pipeline is not None
    assert PipelineBuilder is not None
    assert PipelineContext is not None
    assert PipelineResult is not None
    assert PipelineError is not None
    assert PipelineConfigurationError is not None
    assert PipelineExecutionError is not None
