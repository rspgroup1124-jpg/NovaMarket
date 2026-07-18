"""Command-line interface for the NovaMarket Toolkit."""

import typer

from novamarket_toolkit.commands.doctor import doctor_command
from novamarket_toolkit.commands.version import version_command

app = typer.Typer(
    help="Automation toolkit for Business/System Analysts.",
    no_args_is_help=True,
)

app.command("doctor")(doctor_command)
app.command("version")(version_command)


@app.callback()
def callback() -> None:
    """NovaMarket Toolkit."""
    pass


def main() -> None:
    """Entry point for the toolkit."""
    app()


if __name__ == "__main__":
    main()
