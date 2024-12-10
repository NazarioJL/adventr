import time

from typing import Optional

import typer

from rich.console import Console
from rich.live import Live

from adventr.timeinfo import EventHappening
from adventr.timeinfo import TimeInfo
from adventr.ui.info import InfoViewModel

app = typer.Typer(name="adventr", help="CLI tool for Adventure of Code")

console = Console()


@app.command(name="info")
def info(
    alive: bool = typer.Option(
        False, "--alive", "-a", help="Keeps console alive updating information..."
    ),
) -> None:
    info_view_model = InfoViewModel()
    with Live(info_view_model, refresh_per_second=1) as live:
        if alive:
            while True:
                live.update(info_view_model)
                time.sleep(1)
        else:
            pass


@app.command(name="scaffold")
def scaffold(
    year: Optional[int] = typer.Option(None, "--year", "-y", help="Year to scaffold"),
    day: Optional[int] = typer.Option(None, "--day", "-d", help="Day to scaffold"),
) -> None:
    def validate_day_and_year(y, d) -> tuple[int, int]:
        time_info = TimeInfo()
        if d is None or y is None:
            if time_info.happening != EventHappening.CURRENT:
                console.print(
                    "Advent of code is not currently happening, '--year' and '--day' are required."
                )
                raise SystemExit(1)
            if d is None:
                d = time_info.now_aoc.day
                console.print(f"Day was not provided, using day: '{d}'")
            if y is None:
                y = time_info.now_aoc.year
                console.print(f"Year was not provided, using year: '{y}'")

        if d <= 0 or d > 25:
            console.print(f"Day {d} is out of range (1-25)")
        if y < 2015 or y > time_info.now_aoc.year:
            console.print(f"Day {d} is out of range (2015-{time_info.now_aoc.year})")

        return y, d

    year, day = validate_day_and_year(year, day)
    console.print(f"Generating scaffold for year: {year} and day: {day}")


if __name__ == "__main__":
    app()
