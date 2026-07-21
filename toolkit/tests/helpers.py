"""Shared helper classes for tests."""

from __future__ import annotations

from novamarket_toolkit.generators.base import BaseGenerator


class DummyGenerator(BaseGenerator[str]):
    """Simple generator used in framework tests."""

    artifact_name = "dummy"

    def generate(self, data: str) -> str:
        """
        Return the provided data.

        Parameters
        ----------
        data:
            Input data used for testing.

        Returns
        -------
        str
            The same string that was provided.
        """
        return data
