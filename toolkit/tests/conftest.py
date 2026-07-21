"""Shared pytest fixtures."""

from __future__ import annotations

import pytest

from novamarket_toolkit.generators.registry import GeneratorRegistry
from tests.helpers import DummyGenerator


@pytest.fixture
def registry() -> GeneratorRegistry:
    """
    Return a registry with DummyGenerator registered.
    """
    registry = GeneratorRegistry()
    registry.register(DummyGenerator)
    return registry


@pytest.fixture
def dummy_generator() -> DummyGenerator:
    """
    Return a DummyGenerator instance.
    """
    return DummyGenerator()
