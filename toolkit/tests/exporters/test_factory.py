"""Tests for the exporter factory."""

from __future__ import annotations

import pytest

from novamarket_toolkit.exporters.base import BaseExporter
from novamarket_toolkit.exporters.exceptions import ExporterNotFoundError
from novamarket_toolkit.exporters.factory import ExportFactory
from novamarket_toolkit.exporters.registry import ExportRegistry


class DummyExporter(BaseExporter):
    """Exporter used for testing."""

    format_name = "dummy"

    def export(self, content: str) -> str:
        """Return exported content."""
        return content


def test_create_exporter() -> None:
    """Factory creates an exporter instance."""
    registry = ExportRegistry()
    registry.register(DummyExporter)

    factory = ExportFactory(registry)

    exporter = factory.create("dummy")

    assert isinstance(exporter, DummyExporter)


def test_create_unknown_exporter_raises_error() -> None:
    """Creating an unknown exporter raises an error."""
    registry = ExportRegistry()
    factory = ExportFactory(registry)

    with pytest.raises(ExporterNotFoundError):
        factory.create("unknown")
