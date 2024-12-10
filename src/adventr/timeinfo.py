from datetime import datetime
from datetime import timedelta
from enum import Enum
from enum import auto
from typing import NamedTuple
from typing import Optional
from zoneinfo import ZoneInfo

AOC_TZ = ZoneInfo("EST")


class EventHappening(Enum):
    THIS_YEAR = auto()
    CURRENT = auto()
    NEXT_YEAR = auto()


class TimeToNext(NamedTuple):
    days: int
    hours: int
    minutes: int
    seconds: int

    @staticmethod
    def from_td(td: timedelta) -> "TimeToNext":
        return TimeToNext(
            days=td.days,
            hours=td.seconds // 3600,
            minutes=(td.seconds // 60) % 60,
            seconds=(td.seconds % 60),
        )


class TimeInfo:
    def __init__(self, now: Optional[datetime] = None):
        if now is None:
            self._now_local = datetime.now().astimezone()
        else:
            if now.tzinfo is None:
                raise ValueError("Provided time must be timezone-aware")
            self._now_local = now

        self._now_est = self._now_local.astimezone(AOC_TZ)

        if (self._now_est.year, self._now_est.month, self._now_est.day) < (
            self._now_est.year,
            12,
            1,
        ):
            self._next_start_event = datetime(
                self._now_est.year, 12, 1, hour=0, minute=0, second=0, tzinfo=AOC_TZ
            )
            self._happening = EventHappening.THIS_YEAR
        elif (self._now_est.year, self._now_est.month, self._now_est.day) <= (
            self._now_est.year,
            12,
            25,
        ):
            if self._now_est.day < 25:
                self._next_start_event = datetime(
                    self._now_est.year,
                    self._now_est.month,
                    self._now_est.day + 1,
                    hour=0,
                    minute=0,
                    second=0,
                    tzinfo=AOC_TZ,
                )
                self._happening = EventHappening.CURRENT
            else:
                self._next_start_event = datetime(
                    self._now_est.year + 1,
                    12,
                    1,
                    hour=0,
                    minute=0,
                    second=0,
                    tzinfo=AOC_TZ,
                )
                self._happening = EventHappening.NEXT_YEAR
        else:
            self._next_start_event = datetime(
                self._now_est.year + 1,
                12,
                1,
                hour=0,
                minute=0,
                second=0,
                tzinfo=AOC_TZ,
            )
            self._happening = EventHappening.NEXT_YEAR

        assert self._next_start_event >= self._now_local
        self._time_to_next = TimeToNext.from_td(
            self._next_start_event - self._now_local
        )

    @property
    def time_to_next(self) -> TimeToNext:
        return self._time_to_next

    @property
    def happening(self) -> EventHappening:
        return self._happening

    @property
    def next_start_event(self) -> datetime:
        return self._next_start_event

    @property
    def now_aoc(self) -> datetime:
        return self._now_est

    @property
    def now_local(self) -> datetime:
        return self._now_local
