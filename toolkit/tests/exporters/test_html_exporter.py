"""Tests for the HTML exporter."""

from __future__ import annotations

from novamarket_toolkit.exporters.implementations.html import HtmlExporter


def test_format_name() -> None:
    """HTML exporter defines the correct format name."""
    assert HtmlExporter.format_name == "html"


def test_export_wraps_content_in_html() -> None:
    """HTML exporter wraps content in a complete HTML document."""
    exporter = HtmlExporter()

    content = "Hello, NovaMarket!"

    result = exporter.export(content)

    assert "<!DOCTYPE html>" in result
    assert "<html>" in result
    assert "<body>" in result
    assert "<pre>Hello, NovaMarket!</pre>" in result
    assert "</html>" in result


def test_export_escapes_html_characters() -> None:
    """HTML exporter escapes HTML special characters."""
    exporter = HtmlExporter()

    content = "<user>"

    result = exporter.export(content)

    assert "&lt;user&gt;" in result


def test_export_empty_content() -> None:
    """HTML exporter handles empty content."""
    exporter = HtmlExporter()

    result = exporter.export("")

    assert "<pre></pre>" in result
