"""Tests for the validator factory."""

from __future__ import annotations

from novamarket_toolkit.validators.factory import ValidatorFactory
from tests.helpers import DummyValidator


def test_create_validator(validator_registry) -> None:
    """
    Verify that the factory creates the correct validator instance.
    """
    factory = ValidatorFactory(validator_registry)

    validator = factory.create("dummy")

    assert isinstance(validator, DummyValidator)
