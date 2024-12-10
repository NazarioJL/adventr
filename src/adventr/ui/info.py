from datetime import datetime

from rich.console import Group
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text

from adventr.timeinfo import EventHappening
from adventr.timeinfo import TimeInfo


class TimeInfoViewModel:
    def __init__(self, now: datetime | None = None):
        time_info = TimeInfo(now)
        match time_info.happening:
            case EventHappening.THIS_YEAR:
                message = "Advent of Code has not happened yet this year..."
                wait = f"The event will open in {time_info.time_to_next.days} days, {time_info.time_to_next.hours} hours, {time_info.time_to_next.minutes} minutes and {time_info.time_to_next.seconds} seconds."
            case EventHappening.CURRENT:
                message = f"You are on day {time_info.now_aoc.day} of this year's Advent of Code calendar"
                if time_info.now_aoc.day < 25:
                    wait = f"The puzzle will open today in {time_info.time_to_next.hours} hours, {time_info.time_to_next.minutes} minutes and {time_info.time_to_next.seconds} seconds."
                else:
                    wait = "Today is the last puzzle until next year!"
            case EventHappening.NEXT_YEAR:
                message = "Advent of code has finished this year!"
                wait = f"Only {time_info.time_to_next.days} until next event!"
            case _:
                raise ValueError(
                    f"Unexpected {EventHappening} of '{time_info.happening}'"
                )

        self._message = Text(message, justify="center")
        self._wait = Text(wait, justify="center")

    def __rich__(self):
        return Panel(
            renderable=Group(self._message, self._wait),
        )


class InfoViewModel:
    def __init__(self):
        pass

    def __rich__(self) -> Panel:
        return Panel(
            title="Advent of Code",
            renderable=Group(
                Markdown(
                    "Welcome to `adventr` your console for working with _[Advent of Code](https://adventofcode.com/)_ 🎄"
                ),
                TimeInfoViewModel(),
            ),
        )
