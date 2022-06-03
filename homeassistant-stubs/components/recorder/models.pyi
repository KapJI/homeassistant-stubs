from .const import ALL_DOMAIN_EXCLUDE_ATTRS as ALL_DOMAIN_EXCLUDE_ATTRS, JSON_DUMP as JSON_DUMP
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.websocket_api.const import COMPRESSED_STATE_ATTRIBUTES as COMPRESSED_STATE_ATTRIBUTES, COMPRESSED_STATE_LAST_CHANGED as COMPRESSED_STATE_LAST_CHANGED, COMPRESSED_STATE_LAST_UPDATED as COMPRESSED_STATE_LAST_UPDATED, COMPRESSED_STATE_STATE as COMPRESSED_STATE_STATE
from homeassistant.const import MAX_LENGTH_EVENT_CONTEXT_ID as MAX_LENGTH_EVENT_CONTEXT_ID, MAX_LENGTH_EVENT_EVENT_TYPE as MAX_LENGTH_EVENT_EVENT_TYPE, MAX_LENGTH_EVENT_ORIGIN as MAX_LENGTH_EVENT_ORIGIN, MAX_LENGTH_STATE_ENTITY_ID as MAX_LENGTH_STATE_ENTITY_ID, MAX_LENGTH_STATE_STATE as MAX_LENGTH_STATE_STATE
from homeassistant.core import Context as Context, Event as Event, EventOrigin as EventOrigin, State as State, split_entity_id as split_entity_id
from sqlalchemy import Column, JSON
from sqlalchemy.dialects import sqlite
from sqlalchemy.engine.row import Row as Row
from typing import Any, TypedDict, overload

Base: Incomplete
SCHEMA_VERSION: int
_LOGGER: Incomplete
DB_TIMEZONE: str
TABLE_EVENTS: str
TABLE_EVENT_DATA: str
TABLE_STATES: str
TABLE_STATE_ATTRIBUTES: str
TABLE_RECORDER_RUNS: str
TABLE_SCHEMA_CHANGES: str
TABLE_STATISTICS: str
TABLE_STATISTICS_META: str
TABLE_STATISTICS_RUNS: str
TABLE_STATISTICS_SHORT_TERM: str
ALL_TABLES: Incomplete
TABLES_TO_CHECK: Incomplete
LAST_UPDATED_INDEX: str
ENTITY_ID_LAST_UPDATED_INDEX: str
EVENTS_CONTEXT_ID_INDEX: str
STATES_CONTEXT_ID_INDEX: str
EMPTY_JSON_OBJECT: str

class FAST_PYSQLITE_DATETIME(sqlite.DATETIME):
    def result_processor(self, dialect, coltype): ...

JSON_VARIENT_CAST: Incomplete
JSONB_VARIENT_CAST: Incomplete
DATETIME_TYPE: Incomplete
DOUBLE_TYPE: Incomplete

class JSONLiteral(JSON):
    def literal_processor(self, dialect: str) -> Callable[[Any], str]: ...

EVENT_ORIGIN_ORDER: Incomplete
EVENT_ORIGIN_TO_IDX: Incomplete

class UnsupportedDialect(Exception): ...

class Events(Base):
    __table_args__: Incomplete
    __tablename__: Incomplete
    event_id: Incomplete
    event_type: Incomplete
    event_data: Incomplete
    origin: Incomplete
    origin_idx: Incomplete
    time_fired: Incomplete
    context_id: Incomplete
    context_user_id: Incomplete
    context_parent_id: Incomplete
    data_id: Incomplete
    event_data_rel: Incomplete
    def __repr__(self) -> str: ...
    @staticmethod
    def from_event(event: Event) -> Events: ...
    def to_native(self, validate_entity_id: bool = ...) -> Union[Event, None]: ...

class EventData(Base):
    __table_args__: Incomplete
    __tablename__: Incomplete
    data_id: Incomplete
    hash: Incomplete
    shared_data: Incomplete
    def __repr__(self) -> str: ...
    @staticmethod
    def from_event(event: Event) -> EventData: ...
    @staticmethod
    def shared_data_from_event(event: Event) -> str: ...
    @staticmethod
    def hash_shared_data(shared_data: str) -> int: ...
    def to_native(self) -> dict[str, Any]: ...

class States(Base):
    __table_args__: Incomplete
    __tablename__: Incomplete
    state_id: Incomplete
    entity_id: Incomplete
    state: Incomplete
    attributes: Incomplete
    event_id: Incomplete
    last_changed: Incomplete
    last_updated: Incomplete
    old_state_id: Incomplete
    attributes_id: Incomplete
    context_id: Incomplete
    context_user_id: Incomplete
    context_parent_id: Incomplete
    origin_idx: Incomplete
    old_state: Incomplete
    state_attributes: Incomplete
    def __repr__(self) -> str: ...
    @staticmethod
    def from_event(event: Event) -> States: ...
    def to_native(self, validate_entity_id: bool = ...) -> Union[State, None]: ...

class StateAttributes(Base):
    __table_args__: Incomplete
    __tablename__: Incomplete
    attributes_id: Incomplete
    hash: Incomplete
    shared_attrs: Incomplete
    def __repr__(self) -> str: ...
    @staticmethod
    def from_event(event: Event) -> StateAttributes: ...
    @staticmethod
    def shared_attrs_from_event(event: Event, exclude_attrs_by_domain: dict[str, set[str]]) -> str: ...
    @staticmethod
    def hash_shared_attrs(shared_attrs: str) -> int: ...
    def to_native(self) -> dict[str, Any]: ...

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

class StatisticsBase:
    id: Incomplete
    created: Incomplete
    def metadata_id(self) -> Column: ...
    start: Incomplete
    mean: Incomplete
    min: Incomplete
    max: Incomplete
    last_reset: Incomplete
    state: Incomplete
    sum: Incomplete
    @classmethod
    def from_stats(cls, metadata_id: int, stats: StatisticData) -> StatisticsBase: ...

class Statistics(Base, StatisticsBase):
    duration: Incomplete
    __table_args__: Incomplete
    __tablename__: Incomplete

class StatisticsShortTerm(Base, StatisticsBase):
    duration: Incomplete
    __table_args__: Incomplete
    __tablename__: Incomplete

class StatisticMetaData(TypedDict):
    has_mean: bool
    has_sum: bool
    name: Union[str, None]
    source: str
    statistic_id: str
    unit_of_measurement: Union[str, None]

class StatisticsMeta(Base):
    __table_args__: Incomplete
    __tablename__: Incomplete
    id: Incomplete
    statistic_id: Incomplete
    source: Incomplete
    unit_of_measurement: Incomplete
    has_mean: Incomplete
    has_sum: Incomplete
    name: Incomplete
    @staticmethod
    def from_meta(meta: StatisticMetaData) -> StatisticsMeta: ...

class RecorderRuns(Base):
    __table_args__: Incomplete
    __tablename__: Incomplete
    run_id: Incomplete
    start: Incomplete
    end: Incomplete
    closed_incorrect: Incomplete
    created: Incomplete
    def __repr__(self) -> str: ...
    def entity_ids(self, point_in_time: Union[datetime, None] = ...) -> list[str]: ...
    def to_native(self, validate_entity_id: bool = ...) -> RecorderRuns: ...

class SchemaChanges(Base):
    __tablename__: Incomplete
    change_id: Incomplete
    schema_version: Incomplete
    changed: Incomplete
    def __repr__(self) -> str: ...

class StatisticsRuns(Base):
    __tablename__: Incomplete
    run_id: Incomplete
    start: Incomplete
    def __repr__(self) -> str: ...

EVENT_DATA_JSON: Incomplete
OLD_FORMAT_EVENT_DATA_JSON: Incomplete
SHARED_ATTRS_JSON: Incomplete
OLD_FORMAT_ATTRS_JSON: Incomplete
ENTITY_ID_IN_EVENT: Column
OLD_ENTITY_ID_IN_EVENT: Column
DEVICE_ID_IN_EVENT: Column
OLD_STATE: Incomplete


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
