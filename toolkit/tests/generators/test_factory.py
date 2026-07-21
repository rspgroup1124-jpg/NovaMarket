"""Tests for the generator factory."""

from __future__ import annotations

from novamarket_toolkit.generators.factory import GeneratorFactory
from tests.helpers import DummyGenerator


def test_create_generator(registry) -> None:
    """
    Verify that the factory creates the correct generator instance.
    """
    factory = GeneratorFactory(registry)

    generator = factory.create("dummy")

    assert isinstance(generator, DummyGenerator)
