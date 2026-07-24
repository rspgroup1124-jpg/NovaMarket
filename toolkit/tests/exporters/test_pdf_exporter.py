"""Tests for the PDF exporter."""

from __future__ import annotations

from novamarket_toolkit.exporters.implementations.pdf import PdfExporter


def test_format_name() -> None:
    """PDF exporter defines the correct format name."""
    assert PdfExporter.format_name == "pdf"


def test_export_returns_bytes() -> None:
    """PDF exporter returns bytes."""
    exporter = PdfExporter()

    result = exporter.export("NovaMarket Toolkit")

    assert isinstance(result, bytes)


def test_export_returns_non_empty_pdf() -> None:
    """PDF exporter returns a non-empty PDF document."""
    exporter = PdfExporter()

    result = exporter.export("NovaMarket Toolkit")

    assert len(result) > 0


def test_export_creates_valid_pdf_header() -> None:
    """PDF exporter creates a valid PDF document."""
    exporter = PdfExporter()

    result = exporter.export("NovaMarket Toolkit")

    assert result.startswith(b"%PDF")
