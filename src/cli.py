import logging

import click

from src.commands.cmd_map import cmd_map

logger = logging.getLogger(__name__)


@click.group()
def cli():
    pass


cli.add_command(cmd_map, "map")
