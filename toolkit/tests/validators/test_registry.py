"""Tests for the validator registry."""

from __future__ import annotations

import pytest

from novamarket_toolkit.validators.exceptions import (
    DuplicateValidatorError,
    ValidatorNotFoundError,
)
from novamarket_toolkit.validators.registry import ValidatorRegistry
from tests.helpers import DummyValidator


def test_register_validator() -> None:
    """Register a validator successfully."""
    registry = ValidatorRegistry()

    registry.register(DummyValidator)

    assert registry.is_registered("dummy")


def test_get_registered_validator() -> None:
    """Return a registered validator class."""
    registry = ValidatorRegistry()

    registry.register(DummyValidator)

    assert registry.get("dummy") is DummyValidator


def test_register_duplicate_validator() -> None:
    """Reject duplicate validator registration."""
    registry = ValidatorRegistry()

    registry.register(DummyValidator)

    with pytest.raises(DuplicateValidatorError):
        registry.register(DummyValidator)


def test_get_unknown_validator() -> None:
    """Raise an error for an unknown validator."""
    registry = ValidatorRegistry()

    with pytest.raises(ValidatorNotFoundError):
        registry.get("unknown")


def test_registered_validators_returns_sorted_names() -> None:
    """Return registered validator names."""
    registry = ValidatorRegistry()

    registry.register(DummyValidator)

    assert registry.registered_validators() == ("dummy",)
