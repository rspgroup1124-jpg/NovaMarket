"""Shared helper classes for tests."""

from __future__ import annotations

from novamarket_toolkit.generators.base import BaseGenerator


class DummyGenerator(BaseGenerator):
    """Simple generator used in framework tests."""

    artifact_name = "dummy"

    def generate(self, **kwargs) -> str:
        """Return a predictable artifact."""
        return "dummy artifact"
