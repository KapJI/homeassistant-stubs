from .const import ALL_DOMAIN_EXCLUDE_ATTRS as ALL_DOMAIN_EXCLUDE_ATTRS, JSON_DUMP as JSON_DUMP
from datetime import datetime
from homeassistant.const import MAX_LENGTH_EVENT_CONTEXT_ID as MAX_LENGTH_EVENT_CONTEXT_ID, MAX_LENGTH_EVENT_EVENT_TYPE as MAX_LENGTH_EVENT_EVENT_TYPE, MAX_LENGTH_EVENT_ORIGIN as MAX_LENGTH_EVENT_ORIGIN, MAX_LENGTH_STATE_ENTITY_ID as MAX_LENGTH_STATE_ENTITY_ID, MAX_LENGTH_STATE_STATE as MAX_LENGTH_STATE_STATE
from homeassistant.core import Context as Context, Event as Event, EventOrigin as EventOrigin, State as State, split_entity_id as split_entity_id
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from sqlalchemy import Column
from sqlalchemy.engine.row import Row as Row
from typing import Any, TypedDict, overload

Base: Any
SCHEMA_VERSION: int
_LOGGER: Any
DB_TIMEZONE: str
TABLE_EVENTS: str
TABLE_STATES: str
TABLE_STATE_ATTRIBUTES: str
TABLE_RECORDER_RUNS: str
TABLE_SCHEMA_CHANGES: str
TABLE_STATISTICS: str
TABLE_STATISTICS_META: str
TABLE_STATISTICS_RUNS: str
TABLE_STATISTICS_SHORT_TERM: str
ALL_TABLES: Any
EMPTY_JSON_OBJECT: str
DATETIME_TYPE: Any
DOUBLE_TYPE: Any

class Events(Base):
    __table_args__: Any
    __tablename__: Any
    event_id: Any
    event_type: Any
    event_data: Any
    origin: Any
    time_fired: Any
    context_id: Any
    context_user_id: Any
    context_parent_id: Any
    def __repr__(self) -> str: ...
    @staticmethod
    def from_event(event: Event, event_data: Union[UndefinedType, None] = ...) -> Events: ...
    def to_native(self, validate_entity_id: bool = ...) -> Union[Event, None]: ...

class States(Base):
    __table_args__: Any
    __tablename__: Any
    state_id: Any
    entity_id: Any
    state: Any
    attributes: Any
    event_id: Any
    last_changed: Any
    last_updated: Any
    old_state_id: Any
    attributes_id: Any
    event: Any
    old_state: Any
    state_attributes: Any
    def __repr__(self) -> str: ...
    @staticmethod
    def from_event(event: Event) -> States: ...
    def to_native(self, validate_entity_id: bool = ...) -> Union[State, None]: ...

class StateAttributes(Base):
    __table_args__: Any
    __tablename__: Any
    attributes_id: Any
    hash: Any
    shared_attrs: Any
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
    id: Any
    created: Any
    def metadata_id(self) -> Column: ...
    start: Any
    mean: Any
    min: Any
    max: Any
    last_reset: Any
    state: Any
    sum: Any
    @classmethod
    def from_stats(cls, metadata_id: int, stats: StatisticData) -> StatisticsBase: ...

class Statistics(Base, StatisticsBase):
    duration: Any
    __table_args__: Any
    __tablename__: Any

class StatisticsShortTerm(Base, StatisticsBase):
    duration: Any
    __table_args__: Any
    __tablename__: Any

class StatisticMetaData(TypedDict):
    has_mean: bool
    has_sum: bool
    name: Union[str, None]
    source: str
    statistic_id: str
    unit_of_measurement: Union[str, None]

class StatisticsMeta(Base):
    __table_args__: Any
    __tablename__: Any
    id: Any
    statistic_id: Any
    source: Any
    unit_of_measurement: Any
    has_mean: Any
    has_sum: Any
    name: Any
    @staticmethod
    def from_meta(meta: StatisticMetaData) -> StatisticsMeta: ...

class RecorderRuns(Base):
    __table_args__: Any
    __tablename__: Any
    run_id: Any
    start: Any
    end: Any
    closed_incorrect: Any
    created: Any
    def __repr__(self) -> str: ...
    def entity_ids(self, point_in_time: Union[datetime, None] = ...) -> list[str]: ...
    def to_native(self, validate_entity_id: bool = ...) -> RecorderRuns: ...

class SchemaChanges(Base):
    __tablename__: Any
    change_id: Any
    schema_version: Any
    changed: Any
    def __repr__(self) -> str: ...

class StatisticsRuns(Base):
    __tablename__: Any
    run_id: Any
    start: Any
    def __repr__(self) -> str: ...


@overload
def process_timestamp(ts: None) -> None: ...
@overload
def process_timestamp(ts: datetime) -> datetime: ...
@overload
def process_timestamp_to_utc_isoformat(ts: None) -> None: ...
@overload
def process_timestamp_to_utc_isoformat(ts: datetime) -> str: ...

class LazyState(State):
    __slots__: Any
    _row: Any
    entity_id: Any
    state: Any
    _attributes: Any
    _last_changed: Any
    _last_updated: Any
    _context: Any
    _attr_cache: Any
    def __init__(self, row: Row, attr_cache: Union[dict[str, dict[str, Any]], None] = ...) -> None: ...
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
