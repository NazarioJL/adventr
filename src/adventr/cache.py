import os

from adventr.logger import get_logger

logger = get_logger(__name__)


class Cache:
    def __init__(self, path: str | None = None):
        if path is None:
            self._path = os.path.join(os.getcwd(), ".cache")
            logger.info(f"Using default cache location: '{self._path}'")
        else:
            self._path = path
            logger.info(f"Using user specified cache location: '{path}'")

        if not os.path.exists(self._path):
            logger.info(f"Creating cache directory at: '{self._path}'")
            os.makedirs(self._path)
        else:
            logger.info(f"Cache directory found at: '{self._path}'")
            pass

    @property
    def path(self):
        return self._path
