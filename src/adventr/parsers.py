from typing import Callable
from typing import Protocol
from typing import TypeVar

TParsedInput = TypeVar("TParsedInput", covariant=True)


ParserFuncTypeDef = Callable[[str], TParsedInput]


class InputParser(Protocol[TParsedInput]):
    def parse(self, input_: str) -> TParsedInput:
        pass


def list_of_nums_parser(data: str) -> list[int]:
    return [int(line) for line in data.splitlines()]
