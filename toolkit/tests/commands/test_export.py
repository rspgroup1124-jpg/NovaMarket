"""Tests for the export command."""

from __future__ import annotations

from typer.testing import CliRunner

from novamarket_toolkit.cli import app

runner = CliRunner()


def test_export_command() -> None:
    """Export command should complete successfully."""
    result = runner.invoke(app, ["export"])

    assert result.exit_code == 0
    assert "Export functionality" in result.stdout
