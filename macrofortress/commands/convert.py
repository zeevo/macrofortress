import logging
from os import path
from typing import Annotated

import cv2
import typer

from constants.help import GREYSCALE_HELP_MESSAGE
from constants.logging import LOG_FORMAT
from constants.macro import (
    CURSOR_DOWN,
    CURSOR_LEFT,
    CURSOR_RIGHT,
    CURSOR_UP,
    MINE,
)

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

logger = logging.getLogger(__name__)


def convert(map: str, output: Annotated[str, typer.Option()] = ""):
    if not path.exists(map):
        logger.info(map + " does not appear to be a valid path")
        logger.info("Exiting...")
        exit()

    if not output:
        formatted_output = map.rsplit(".", 1)[0] + ".mak"
    else:
        formatted_output = output

    cv_image = cv2.imread(map, 0)

    PICTURE_COLUMNS = cv_image.shape[1]
    PICTURE_ROWS = cv_image.shape[0]

    with open(formatted_output, "a") as file_object:
        file_object.write(formatted_output)
        file_object.write("\n")
        file_object.close()

    start_pos = None

    for column in range(PICTURE_COLUMNS):
        for row in range(PICTURE_ROWS):
            if cv_image[row][column] == 143:
                start_pos = [row, column]

    if not start_pos:
        logger.info(GREYSCALE_HELP_MESSAGE)
        exit(1)

    start_pos_row = start_pos[0]
    start_pos_column = start_pos[1]

    for _ in range(start_pos_column):
        with open(formatted_output, "a") as file_object:
            file_object.write(CURSOR_LEFT)
            file_object.close()

    for _ in range(start_pos_row):
        with open(formatted_output, "a") as file_object:
            file_object.write(CURSOR_UP)
            file_object.close()

    for row in range(PICTURE_ROWS):
        for column in range(PICTURE_COLUMNS):
            if cv_image[row][column] != 0:
                with open(formatted_output, "a") as file_object:
                    file_object.write(CURSOR_RIGHT)
                    file_object.close()
            else:
                with open(formatted_output, "a") as file_object:
                    file_object.write(CURSOR_RIGHT)
                    file_object.write(MINE)
                    file_object.close()

            if column == (PICTURE_COLUMNS - 1):
                with open(formatted_output, "a") as file_object:
                    file_object.write(CURSOR_DOWN)
                    file_object.close()
                    for _ in range(PICTURE_COLUMNS):
                        with open(formatted_output, "a") as file_object:
                            file_object.write(CURSOR_LEFT)
                            file_object.close()
                    file_object.close()

    with open(formatted_output, "a") as file_object:
        file_object.write("End of macro\n")
        file_object.close()
        logger.info(f"`{formatted_output}` Macro written.")
