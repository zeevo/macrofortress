import logging

import click

from src.commands.hello_world import hello_world

logger = logging.getLogger(__name__)


@click.group()
def cli():
    pass


cli.add_command(hello_world, "hello")
