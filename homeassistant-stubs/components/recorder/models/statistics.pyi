from datetime import datetime, timedelta
from typing import Literal, TypedDict

class StatisticResult(TypedDict):
    meta: StatisticMetaData
    stat: StatisticData

class StatisticDataTimestampBase(TypedDict):
    start_ts: float

class StatisticDataBase(TypedDict):
    start: datetime

class StatisticMixIn(TypedDict):
    state: float
    sum: float
    min: float
    max: float
    mean: float

class StatisticData(StatisticDataBase, StatisticMixIn):
    last_reset: Union[datetime, None]

class StatisticDataTimestamp(StatisticDataTimestampBase, StatisticMixIn):
    last_reset_ts: Union[float, None]

class StatisticMetaData(TypedDict):
    has_mean: bool
    has_sum: bool
    name: Union[str, None]
    source: str
    statistic_id: str
    unit_of_measurement: Union[str, None]

class CalendarStatisticPeriod(TypedDict):
    period: Literal['hour', 'day', 'week', 'month', 'year']
    offset: int

class FixedStatisticPeriod(TypedDict):
    end_time: datetime
    start_time: datetime

class RollingWindowStatisticPeriod(TypedDict):
    duration: timedelta
    offset: timedelta

class StatisticPeriod(TypedDict):
    calendar: CalendarStatisticPeriod
    fixed_period: FixedStatisticPeriod
    rolling_window: RollingWindowStatisticPeriod
