"""Command-line interface for the NovaMarket Toolkit."""

from importlib.metadata import version

import typer

app = typer.Typer(
    help="Automation toolkit for Business/System Analysts.",
    no_args_is_help=True,
)


@app.command()
def doctor() -> None:
    """Check that the toolkit is installed correctly."""
    typer.echo("✅ NovaMarket Toolkit is installed and ready to use.")


@app.command("version")
def version_command() -> None:
    """Show toolkit version."""
    typer.echo(f"NovaMarket Toolkit v{version('novamarket-toolkit')}")


@app.callback()
def callback() -> None:
    """NovaMarket Toolkit."""
    pass


def main() -> None:
    """Entry point for the toolkit."""
    app()


if __name__ == "__main__":
    main()
