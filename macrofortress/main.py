import logging

import typer


from commands.convert import convert

app = typer.Typer()

app.command()(convert)


logger = logging.getLogger(__name__)


if __name__ == "__main__":
    app()
