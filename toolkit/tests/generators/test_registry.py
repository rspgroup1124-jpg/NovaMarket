"""Tests for the generator registry."""

from __future__ import annotations

import pytest

from novamarket_toolkit.generators.exceptions import (
    DuplicateGeneratorError,
    GeneratorNotFoundError,
)
from novamarket_toolkit.generators.registry import GeneratorRegistry
from tests.helpers import DummyGenerator


def test_register_generator() -> None:
    """Register a generator successfully."""
    registry = GeneratorRegistry()

    registry.register(DummyGenerator)

    assert registry.is_registered("dummy")


def test_get_registered_generator() -> None:
    """Return a registered generator class."""
    registry = GeneratorRegistry()

    registry.register(DummyGenerator)

    assert registry.get("dummy") is DummyGenerator


def test_register_duplicate_generator() -> None:
    """Reject duplicate generator registration."""
    registry = GeneratorRegistry()

    registry.register(DummyGenerator)

    with pytest.raises(DuplicateGeneratorError):
        registry.register(DummyGenerator)


def test_get_unknown_generator() -> None:
    """Raise an error for an unknown generator."""
    registry = GeneratorRegistry()

    with pytest.raises(GeneratorNotFoundError):
        registry.get("unknown")


def test_registered_generators_returns_sorted_names() -> None:
    """Return registered generator names."""
    registry = GeneratorRegistry()

    registry.register(DummyGenerator)

    assert registry.registered_generators() == ("dummy",)
