"""Tests for the generate command."""

from __future__ import annotations

from typer.testing import CliRunner

from novamarket_toolkit.cli import app

runner = CliRunner()


def test_generate_command() -> None:
    """Generate command should complete successfully."""
    result = runner.invoke(app, ["generate"])

    assert result.exit_code == 0
    assert "Generation functionality" in result.stdout
