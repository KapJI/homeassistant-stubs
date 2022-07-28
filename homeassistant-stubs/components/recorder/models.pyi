import asyncio
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.websocket_api.const import COMPRESSED_STATE_ATTRIBUTES as COMPRESSED_STATE_ATTRIBUTES, COMPRESSED_STATE_LAST_CHANGED as COMPRESSED_STATE_LAST_CHANGED, COMPRESSED_STATE_LAST_UPDATED as COMPRESSED_STATE_LAST_UPDATED, COMPRESSED_STATE_STATE as COMPRESSED_STATE_STATE
from homeassistant.core import Context as Context, State as State
from homeassistant.helpers.json import json_loads as json_loads
from sqlalchemy.engine.row import Row as Row
from typing import Any, TypedDict, overload

_LOGGER: Incomplete
DB_TIMEZONE: str
EMPTY_JSON_OBJECT: str

class UnsupportedDialect(Exception): ...

class RecorderData:
    recorder_platforms: dict[str, Any]
    db_connected: asyncio.Future
    def __init__(self, recorder_platforms, db_connected) -> None: ...

class StatisticResult(TypedDict):
    meta: StatisticMetaData
    stat: StatisticData

class StatisticDataBase(TypedDict):
    start: datetime

class StatisticData(StatisticDataBase):
    mean: float
    min: float
    max: float
    last_reset: Union[datetime, None]
    state: float
    sum: float

class StatisticMetaData(TypedDict):
    has_mean: bool
    has_sum: bool
    name: Union[str, None]
    source: str
    statistic_id: str
    unit_of_measurement: Union[str, None]


@overload
def process_timestamp(ts: None) -> None: ...
@overload
def process_timestamp(ts: datetime) -> datetime: ...
@overload
def process_timestamp_to_utc_isoformat(ts: None) -> None: ...
@overload
def process_timestamp_to_utc_isoformat(ts: datetime) -> str: ...
def process_datetime_to_timestamp(ts: datetime) -> float: ...

class LazyState(State):
    __slots__: Incomplete
    _row: Incomplete
    entity_id: Incomplete
    state: Incomplete
    _attributes: Incomplete
    _last_changed: Incomplete
    _last_updated: Incomplete
    _context: Incomplete
    attr_cache: Incomplete
    def __init__(self, row: Row, attr_cache: dict[str, dict[str, Any]], start_time: Union[datetime, None] = ...) -> None: ...
    @property
    def attributes(self) -> dict[str, Any]: ...
    @attributes.setter
    def attributes(self, value: dict[str, Any]) -> None: ...
    @property
    def context(self) -> Context: ...
    @context.setter
    def context(self, value: Context) -> None: ...
    @property
    def last_changed(self) -> datetime: ...
    @last_changed.setter
    def last_changed(self, value: datetime) -> None: ...
    @property
    def last_updated(self) -> datetime: ...
    @last_updated.setter
    def last_updated(self, value: datetime) -> None: ...
    def as_dict(self) -> dict[str, Any]: ...
    def __eq__(self, other: Any) -> bool: ...

def decode_attributes_from_row(row: Row, attr_cache: dict[str, dict[str, Any]]) -> dict[str, Any]: ...
def row_to_compressed_state(row: Row, attr_cache: dict[str, dict[str, Any]], start_time: Union[datetime, None] = ...) -> dict[str, Any]: ...
