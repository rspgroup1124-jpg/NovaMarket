"""Factory for creating artifact exporters."""

from __future__ import annotations

from novamarket_toolkit.exporters.base import BaseExporter
from novamarket_toolkit.exporters.registry import ExportRegistry


class ExportFactory:
    """Create exporter instances from the registry."""

    def __init__(self, registry: ExportRegistry) -> None:
        """
        Initialize the exporter factory.

        Parameters
        ----------
        registry
            Registry containing available exporters.
        """
        self._registry = registry

    def create(self, format_name: str) -> BaseExporter:
        """
        Create an exporter instance.

        Parameters
        ----------
        format_name
            Export format identifier.

        Returns
        -------
        BaseExporter
            Exporter instance.
        """
        exporter_class = self._registry.get(format_name)
        return exporter_class()
