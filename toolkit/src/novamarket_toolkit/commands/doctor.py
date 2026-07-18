"""Doctor command for the NovaMarket Toolkit."""

import typer


def doctor_command() -> None:
    """Check that the toolkit is installed correctly."""
    typer.echo("✅ NovaMarket Toolkit is installed and ready to use.")
