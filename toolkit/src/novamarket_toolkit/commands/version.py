"""Version command for the NovaMarket Toolkit."""

from importlib.metadata import version

import typer


def version_command() -> None:
    """Show toolkit version."""
    typer.echo(f"NovaMarket Toolkit v{version('novamarket-toolkit')}")
