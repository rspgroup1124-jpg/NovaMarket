"""Exceptions for the template engine."""

from __future__ import annotations


class TemplateEngineError(Exception):
    """Base exception for all template engine errors."""


class TemplateNotFoundError(TemplateEngineError):
    """Raised when a template cannot be found."""


class TemplateRenderError(TemplateEngineError):
    """Raised when template rendering fails."""
