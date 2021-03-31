import datetime as dt
from homeassistant.const import MATCH_ALL as MATCH_ALL
from typing import Any

DATE_STR_FORMAT: str
NATIVE_UTC: Any
UTC: Any
DEFAULT_TIME_ZONE: dt.tzinfo
DATETIME_RE: Any

def set_default_time_zone(time_zone: dt.tzinfo) -> None: ...
def get_time_zone(time_zone_str: str) -> Union[dt.tzinfo, None]: ...
def utcnow() -> dt.datetime: ...
def now(time_zone: Union[dt.tzinfo, None]=...) -> dt.datetime: ...
def as_utc(dattim: dt.datetime) -> dt.datetime: ...
def as_timestamp(dt_value: dt.datetime) -> float: ...
def as_local(dattim: dt.datetime) -> dt.datetime: ...
def utc_from_timestamp(timestamp: float) -> dt.datetime: ...
def start_of_local_day(dt_or_d: Union[dt.date, dt.datetime, None]=...) -> dt.datetime: ...
def parse_datetime(dt_str: str) -> Union[dt.datetime, None]: ...
def parse_date(dt_str: str) -> Union[dt.date, None]: ...
def parse_time(time_str: str) -> Union[dt.time, None]: ...
def get_age(date: dt.datetime) -> str: ...
def parse_time_expression(parameter: Any, min_value: int, max_value: int) -> list[int]: ...
def find_next_time_expression_time(now: dt.datetime, seconds: list[int], minutes: list[int], hours: list[int]) -> dt.datetime: ...
