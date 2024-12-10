from unittest.mock import MagicMock

import pytest

from adventr.puzzle import Puzzle


def test_puzzle__init__():
    puzzle = Puzzle(year=2024, day=1)

    assert puzzle.year == 2024
    assert puzzle.day == 1


def test_puzzle__init__bad_input():
    with pytest.raises(ValueError):  # noqa: PT011
        Puzzle(year=2024, day=100)


def test_puzzle__init__bad_year():
    puzzle = Puzzle(year=2024, day=1)

    parser = MagicMock()
    parser.return_value = "PARSED_TEST_DATA"
    actual = puzzle.get_input(data="TEST_DATA", parser=parser)

    assert actual == "PARSED_TEST_DATA"
    parser.assert_called_once_with("TEST_DATA")
