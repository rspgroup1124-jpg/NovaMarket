"""Exceptions for the validator framework."""

from __future__ import annotations


class ValidationError(Exception):
    """Base exception for all validator-related errors."""


class ValidatorNotFoundError(ValidationError):
    """Raised when a requested validator is not registered."""


class DuplicateValidatorError(ValidationError):
    """Raised when attempting to register a validator twice."""
