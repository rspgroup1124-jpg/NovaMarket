"""Tests for the base generator."""

from __future__ import annotations

import pytest

from novamarket_toolkit.generators.base import BaseGenerator


def test_base_generator_is_abstract() -> None:
    """
    Verify that BaseGenerator cannot be instantiated.
    """
    with pytest.raises(TypeError):
        BaseGenerator()
