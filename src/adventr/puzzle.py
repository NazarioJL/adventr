from io import IOBase
from typing import TypeAlias
from typing import Union

from attrs import field
from attrs import frozen
from attrs import validators

from adventr.parsers import InputParser
from adventr.parsers import ParserFuncTypeDef
from adventr.parsers import TParsedInput
from adventr.puzzleinfo import CachePuzzleDataProvider
from adventr.puzzleinfo import PuzzleDataProvider

AnswerType: TypeAlias = int | float | str | None

FIRST_YEAR = 2015


@frozen
class Solution:
    pass


@frozen(kw_only=True)
class Puzzle:
    year: int = field(validator=[validators.instance_of(int), validators.ge(2015)])
    day: int = field(
        validator=[validators.instance_of(int), validators.ge(1), validators.le(25)]
    )

    def get_input(
        self,
        parser: ParserFuncTypeDef | InputParser[TParsedInput],
        data: Union[
            str, IOBase, PuzzleDataProvider, type[PuzzleDataProvider]
        ] = CachePuzzleDataProvider,
    ) -> TParsedInput:
        if isinstance(data, IOBase):
            input_data = data.read()
        elif isinstance(data, str):
            input_data = data
        elif isinstance(data, PuzzleDataProvider):
            input_data = data.get_data(self)
        elif issubclass(data, PuzzleDataProvider):
            # Makes assumption that it can initialize the type
            try:
                input_data = (data()).get_data(self)
            except TypeError as e:
                raise ValueError(
                    f"Unable to instantiate {data.__class__}. This invokes the type without any parameters."
                ) from e
        else:
            raise ValueError(
                "'data' parameter must be either a string, file-like object, or an implementation of 'PuzzleDataProvider'."
            )

        if callable(parser):
            return parser(input_data)
        return parser.parse(input_data)

    def submit(self, solution: Solution):
        raise NotImplementedError
