"""Registry for artifact exporters."""

from __future__ import annotations

from typing import Type

from novamarket_toolkit.exporters.base import BaseExporter
from novamarket_toolkit.exporters.exceptions import (
    DuplicateExporterError,
    ExporterNotFoundError,
)


class ExportRegistry:
    """Store and manage registered exporter classes."""

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._exporters: dict[str, Type[BaseExporter]] = {}

    def register(self, exporter_class: Type[BaseExporter]) -> None:
        """
        Register an exporter class.

        Parameters
        ----------
        exporter_class
            Exporter class to register.

        Raises
        ------
        ValueError
            If the exporter does not define a format name.

        DuplicateExporterError
            If the exporter is already registered.
        """
        format_name = getattr(exporter_class, "format_name", "").strip()

        if not format_name:
            raise ValueError("Exporter class must define a non-empty 'format_name'.")

        if format_name in self._exporters:
            raise DuplicateExporterError(f"Exporter '{format_name}' is already registered.")

        self._exporters[format_name] = exporter_class

    def get(self, format_name: str) -> Type[BaseExporter]:
        """
        Return a registered exporter class.

        Parameters
        ----------
        format_name
            Export format identifier.

        Raises
        ------
        ExporterNotFoundError
            If the exporter is not registered.
        """
        try:
            return self._exporters[format_name]
        except KeyError as error:
            raise ExporterNotFoundError(f"Exporter '{format_name}' is not registered.") from error

    def is_registered(self, format_name: str) -> bool:
        """
        Return True if the exporter is registered.
        """
        return format_name in self._exporters

    def registered_exporters(self) -> tuple[str, ...]:
        """
        Return names of all registered exporters.

        Returns
        -------
        tuple[str, ...]
            Registered exporter names sorted alphabetically.
        """
        return tuple(sorted(self._exporters))
