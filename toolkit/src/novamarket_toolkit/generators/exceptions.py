"""Exceptions for the generator framework."""

from __future__ import annotations


class GeneratorError(Exception):
    """Base exception for all generator-related errors."""


class GeneratorNotFoundError(GeneratorError):
    """Raised when a requested generator is not registered."""


class DuplicateGeneratorError(GeneratorError):
    """Raised when attempting to register a generator twice."""
