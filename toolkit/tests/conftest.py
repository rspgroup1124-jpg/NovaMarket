"""Shared pytest fixtures."""

from __future__ import annotations

import pytest

from novamarket_toolkit.generators.registry import GeneratorRegistry
from novamarket_toolkit.validators.registry import ValidatorRegistry
from tests.helpers import DummyGenerator, DummyValidator


@pytest.fixture
def generator_registry() -> GeneratorRegistry:
    """
    Return a registry with DummyGenerator registered.
    """
    registry = GeneratorRegistry()
    registry.register(DummyGenerator)
    return registry


@pytest.fixture
def validator_registry() -> ValidatorRegistry:
    """
    Return a registry with DummyValidator registered.
    """
    registry = ValidatorRegistry()
    registry.register(DummyValidator)
    return registry


@pytest.fixture
def dummy_generator() -> DummyGenerator:
    """
    Return a DummyGenerator instance.
    """
    return DummyGenerator()


@pytest.fixture
def dummy_validator() -> DummyValidator:
    """
    Return a DummyValidator instance.
    """
    return DummyValidator()
