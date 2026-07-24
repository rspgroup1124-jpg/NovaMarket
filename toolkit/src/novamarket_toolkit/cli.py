"""Command-line interface for the NovaMarket Toolkit."""

import typer

from novamarket_toolkit.commands import (
    doctor_command,
    export_command,
    generate_command,
    info_command,
    list_command,
    validate_command,
    version_command,
)

app = typer.Typer(
    help="Automation toolkit for Business/System Analysts.",
    no_args_is_help=True,
)

app.command("doctor")(doctor_command)
app.command("generate")(generate_command)
app.command("validate")(validate_command)
app.command("export")(export_command)
app.command("list")(list_command)
app.command("info")(info_command)
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
