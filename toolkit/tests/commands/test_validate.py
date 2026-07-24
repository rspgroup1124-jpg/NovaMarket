"""Tests for the validate command."""

from __future__ import annotations

from typer.testing import CliRunner

from novamarket_toolkit.cli import app

runner = CliRunner()


def test_validate_command() -> None:
    """Validate command should complete successfully."""
    result = runner.invoke(app, ["validate"])

    assert result.exit_code == 0
    assert "Validation functionality" in result.stdout
