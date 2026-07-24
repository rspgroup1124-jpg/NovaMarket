"""Exceptions for the exporter framework."""

from __future__ import annotations


class ExporterError(Exception):
    """Base exception for exporter-related errors."""


class DuplicateExporterError(ExporterError):
    """Raised when attempting to register an exporter twice."""


class ExporterNotFoundError(ExporterError):
    """Raised when a requested exporter is not registered."""
