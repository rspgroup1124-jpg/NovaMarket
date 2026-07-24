"""Tests for the list command."""

from __future__ import annotations

from typer.testing import CliRunner

from novamarket_toolkit.cli import app

runner = CliRunner()


def test_list_command() -> None:
    """List command should complete successfully."""
    result = runner.invoke(app, ["list"])

    assert result.exit_code == 0
    assert "Listing functionality" in result.stdout
