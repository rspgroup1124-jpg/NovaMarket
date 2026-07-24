"""Info command for the NovaMarket Toolkit."""

import typer


def info_command() -> None:
    """Show information about the toolkit."""
    typer.echo("NovaMarket Toolkit")
    typer.echo("Automation toolkit for Business/System Analysts.")
