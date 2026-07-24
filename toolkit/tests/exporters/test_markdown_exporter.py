"""Tests for the Markdown exporter."""

from __future__ import annotations

from novamarket_toolkit.exporters.implementations.markdown import MarkdownExporter


def test_format_name() -> None:
    """Markdown exporter defines the correct format name."""
    assert MarkdownExporter.format_name == "markdown"


def test_export_returns_original_content() -> None:
    """Markdown exporter returns the original content."""
    exporter = MarkdownExporter()

    content = "# User Story\n\nAs a customer..."

    assert exporter.export(content) == content


def test_export_empty_content() -> None:
    """Markdown exporter handles empty content."""
    exporter = MarkdownExporter()

    assert exporter.export("") == ""
