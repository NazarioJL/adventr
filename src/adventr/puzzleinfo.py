from typing import Protocol
from typing import runtime_checkable

from adventr.puzzle import Puzzle


@runtime_checkable
class PuzzleDataProvider(Protocol):
    def get_data(self, puzzle: Puzzle) -> str:
        pass


class CachePuzzleDataProvider(PuzzleDataProvider):
    def get_data(self, puzzle: Puzzle) -> str:
        return ""
