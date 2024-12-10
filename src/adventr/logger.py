import logging

from rich.logging import RichHandler

logging.basicConfig(level=logging.INFO, handlers=[RichHandler()])


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
