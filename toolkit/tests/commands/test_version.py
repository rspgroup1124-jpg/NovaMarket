"""Tests for the version command."""

from __future__ import annotations

from typer.testing import CliRunner

from novamarket_toolkit.cli import app

runner = CliRunner()


def test_version_command() -> None:
    """Version command should complete successfully."""
    result = runner.invoke(app, ["version"])

    assert result.exit_code == 0
    assert "NovaMarket Toolkit v" in result.stdout
