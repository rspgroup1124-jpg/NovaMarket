"""Tests for the doctor command."""

from __future__ import annotations

from typer.testing import CliRunner

from novamarket_toolkit.cli import app

runner = CliRunner()


def test_doctor_command() -> None:
    """Doctor command should complete successfully."""
    result = runner.invoke(app, ["doctor"])

    assert result.exit_code == 0
    assert "NovaMarket Toolkit is installed and ready to use." in result.stdout
