"""Tests for the base validator."""

from __future__ import annotations

import pytest

from novamarket_toolkit.validators.base import BaseValidator


def test_base_validator_is_abstract() -> None:
    """
    Verify that BaseValidator cannot be instantiated.
    """
    with pytest.raises(TypeError):
        BaseValidator()
