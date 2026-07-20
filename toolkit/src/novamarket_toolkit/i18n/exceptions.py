"""Custom exceptions for the localization subsystem."""

from __future__ import annotations


class LocalizationError(Exception):
    """Base exception for all localization errors."""


class LocaleNotFoundError(LocalizationError):
    """Raised when a locale file cannot be found."""


class GlossaryNotFoundError(LocalizationError):
    """Raised when the glossary file cannot be found."""


class InvalidLocalizationFileError(LocalizationError):
    """Raised when a localization file contains invalid JSON."""
