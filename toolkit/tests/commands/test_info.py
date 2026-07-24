"""Tests for the info command."""

from __future__ import annotations

from typer.testing import CliRunner

from novamarket_toolkit.cli import app

runner = CliRunner()


def test_info_command() -> None:
    """Info command should complete successfully."""
    result = runner.invoke(app, ["info"])

    assert result.exit_code == 0
    assert "NovaMarket Toolkit" in result.stdout
