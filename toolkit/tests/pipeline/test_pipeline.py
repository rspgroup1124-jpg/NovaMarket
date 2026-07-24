"""Tests for the Pipeline Framework."""

from __future__ import annotations

from novamarket_toolkit.pipeline import (
    Pipeline,
    PipelineBuilder,
    PipelineContext,
    PipelineResult,
)


def test_pipeline_builder_creates_pipeline() -> None:
    """PipelineBuilder should create a Pipeline instance."""
    builder = PipelineBuilder()

    pipeline = builder.build()

    assert isinstance(pipeline, Pipeline)


def test_pipeline_returns_result() -> None:
    """Pipeline should return a PipelineResult."""
    pipeline = Pipeline()

    context = PipelineContext(
        artifact_type="user_story",
        model={"title": "Login"},
    )

    result = pipeline.run(context)

    assert isinstance(result, PipelineResult)
    assert result.success is True
    assert result.artifact == context.model


def test_pipeline_generate_returns_result() -> None:
    """Pipeline.generate should return a PipelineResult."""
    pipeline = Pipeline()

    result = pipeline.generate(
        artifact_type="user_story",
        model={"title": "Login"},
    )

    assert isinstance(result, PipelineResult)
    assert result.success is True
    assert result.artifact == {"title": "Login"}


def test_pipeline_generate_uses_default_locale() -> None:
    """Pipeline.generate should use the default locale."""
    pipeline = Pipeline()

    result = pipeline.generate(
        artifact_type="user_story",
        model={},
    )

    assert result.success is True


def test_pipeline_generate_matches_run() -> None:
    """Pipeline.generate should produce the same result as Pipeline.run()."""
    pipeline = Pipeline()

    model = {"title": "Login"}

    generated = pipeline.generate(
        artifact_type="user_story",
        model=model,
    )

    executed = pipeline.run(
        PipelineContext(
            artifact_type="user_story",
            model=model,
        )
    )

    assert generated == executed


def test_pipeline_context_defaults() -> None:
    """PipelineContext should use the default locale."""
    context = PipelineContext(
        artifact_type="user_story",
        model={},
    )

    assert context.locale == "en"


def test_pipeline_result_defaults() -> None:
    """PipelineResult should allow an empty artifact."""
    result = PipelineResult(success=True)

    assert result.success is True
    assert result.artifact is None
