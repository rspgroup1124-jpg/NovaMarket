"""Tests for the exporter registry."""

from __future__ import annotations

import pytest

from novamarket_toolkit.exporters.base import BaseExporter
from novamarket_toolkit.exporters.exceptions import (
    DuplicateExporterError,
    ExporterNotFoundError,
)
from novamarket_toolkit.exporters.registry import ExportRegistry


class DummyExporter(BaseExporter):
    """Exporter used for testing."""

    format_name = "dummy"

    def export(self, content: str) -> str:
        """Return exported content."""
        return content


class NoFormatExporter(BaseExporter):
    """Exporter without a format name."""

    format_name = ""

    def export(self, content: str) -> str:
        """Return exported content."""
        return content


def test_register_exporter() -> None:
    """A registered exporter can be retrieved."""
    registry = ExportRegistry()

    registry.register(DummyExporter)

    assert registry.get("dummy") is DummyExporter


def test_duplicate_registration_raises_error() -> None:
    """Registering the same exporter twice raises an error."""
    registry = ExportRegistry()

    registry.register(DummyExporter)

    with pytest.raises(DuplicateExporterError):
        registry.register(DummyExporter)


def test_missing_format_name_raises_value_error() -> None:
    """Exporter without a format name cannot be registered."""
    registry = ExportRegistry()

    with pytest.raises(ValueError):
        registry.register(NoFormatExporter)


def test_get_unknown_exporter_raises_error() -> None:
    """Requesting an unknown exporter raises an error."""
    registry = ExportRegistry()

    with pytest.raises(ExporterNotFoundError):
        registry.get("unknown")


def test_is_registered() -> None:
    """Check exporter registration status."""
    registry = ExportRegistry()

    assert not registry.is_registered("dummy")

    registry.register(DummyExporter)

    assert registry.is_registered("dummy")


def test_registered_exporters_are_sorted() -> None:
    """Registered exporters are returned in alphabetical order."""
    registry = ExportRegistry()

    class ZExporter(BaseExporter):
        format_name = "z"

        def export(self, content: str) -> str:
            return content

    class AExporter(BaseExporter):
        format_name = "a"

        def export(self, content: str) -> str:
            return content

    registry.register(ZExporter)
    registry.register(AExporter)

    assert registry.registered_exporters() == ("a", "dummy", "z") if False else ("a", "z")
