from .const import ALL_DOMAIN_EXCLUDE_ATTRS as ALL_DOMAIN_EXCLUDE_ATTRS, SupportedDialect as SupportedDialect
from .models import StatisticData as StatisticData, StatisticDataTimestamp as StatisticDataTimestamp, StatisticMetaData as StatisticMetaData, datetime_to_timestamp_or_none as datetime_to_timestamp_or_none, process_timestamp as process_timestamp
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime, timedelta
from homeassistant.const import MAX_LENGTH_EVENT_CONTEXT_ID as MAX_LENGTH_EVENT_CONTEXT_ID, MAX_LENGTH_EVENT_EVENT_TYPE as MAX_LENGTH_EVENT_EVENT_TYPE, MAX_LENGTH_EVENT_ORIGIN as MAX_LENGTH_EVENT_ORIGIN, MAX_LENGTH_STATE_ENTITY_ID as MAX_LENGTH_STATE_ENTITY_ID, MAX_LENGTH_STATE_STATE as MAX_LENGTH_STATE_STATE
from homeassistant.core import Context as Context, Event as Event, EventOrigin as EventOrigin, State as State, split_entity_id as split_entity_id
from homeassistant.helpers.json import JSON_DUMP as JSON_DUMP, json_bytes as json_bytes, json_bytes_strip_null as json_bytes_strip_null
from homeassistant.util.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, json_loads as json_loads, json_loads_object as json_loads_object
from sqlalchemy import ColumnElement as ColumnElement, JSON
from sqlalchemy.dialects import sqlite
from sqlalchemy.engine.interfaces import Dialect as Dialect
from sqlalchemy.orm import DeclarativeBase, Mapped as Mapped
from sqlalchemy.orm.query import RowReturningQuery as RowReturningQuery
from typing import Any
from typing_extensions import Self

class Base(DeclarativeBase): ...

SCHEMA_VERSION: int
_LOGGER: Incomplete
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
STATISTICS_TABLES: Incomplete
MAX_STATE_ATTRS_BYTES: int
PSQL_DIALECT: Incomplete
ALL_TABLES: Incomplete
TABLES_TO_CHECK: Incomplete
LAST_UPDATED_INDEX_TS: str
ENTITY_ID_LAST_UPDATED_INDEX_TS: str
EVENTS_CONTEXT_ID_INDEX: str
STATES_CONTEXT_ID_INDEX: str
_DEFAULT_TABLE_ARGS: Incomplete

class FAST_PYSQLITE_DATETIME(sqlite.DATETIME):
    def result_processor(self, dialect, coltype): ...

JSON_VARIANT_CAST: Incomplete
JSONB_VARIANT_CAST: Incomplete
DATETIME_TYPE: Incomplete
DOUBLE_TYPE: Incomplete
TIMESTAMP_TYPE = DOUBLE_TYPE

class JSONLiteral(JSON):
    def literal_processor(self, dialect: Dialect) -> Callable[[Any], str]: ...

EVENT_ORIGIN_ORDER: Incomplete
EVENT_ORIGIN_TO_IDX: Incomplete

class Events(Base):
    __table_args__: Incomplete
    __tablename__: Incomplete
    event_id: Mapped[int]
    event_type: Mapped[Union[str, None]]
    event_data: Mapped[Union[str, None]]
    origin: Mapped[Union[str, None]]
    origin_idx: Mapped[Union[int, None]]
    time_fired: Mapped[Union[datetime, None]]
    time_fired_ts: Mapped[Union[float, None]]
    context_id: Mapped[Union[str, None]]
    context_user_id: Mapped[Union[str, None]]
    context_parent_id: Mapped[Union[str, None]]
    data_id: Mapped[Union[int, None]]
    event_data_rel: Mapped[Union[EventData, None]]
    def __repr__(self) -> str: ...
    @property
    def _time_fired_isotime(self) -> Union[str, None]: ...
    @staticmethod
    def from_event(event: Event) -> Events: ...
    def to_native(self, validate_entity_id: bool = ...) -> Union[Event, None]: ...

class EventData(Base):
    __table_args__: Incomplete
    __tablename__: Incomplete
    data_id: Mapped[int]
    hash: Mapped[Union[int, None]]
    shared_data: Mapped[Union[str, None]]
    def __repr__(self) -> str: ...
    @staticmethod
    def shared_data_bytes_from_event(event: Event, dialect: Union[SupportedDialect, None]) -> bytes: ...
    @staticmethod
    def hash_shared_data_bytes(shared_data_bytes: bytes) -> int: ...
    def to_native(self) -> dict[str, Any]: ...

class States(Base):
    __table_args__: Incomplete
    __tablename__: Incomplete
    state_id: Mapped[int]
    entity_id: Mapped[Union[str, None]]
    state: Mapped[Union[str, None]]
    attributes: Mapped[Union[str, None]]
    event_id: Mapped[Union[int, None]]
    last_changed: Mapped[Union[datetime, None]]
    last_changed_ts: Mapped[Union[float, None]]
    last_updated: Mapped[Union[datetime, None]]
    last_updated_ts: Mapped[Union[float, None]]
    old_state_id: Mapped[Union[int, None]]
    attributes_id: Mapped[Union[int, None]]
    context_id: Mapped[Union[str, None]]
    context_user_id: Mapped[Union[str, None]]
    context_parent_id: Mapped[Union[str, None]]
    origin_idx: Mapped[Union[int, None]]
    old_state: Mapped[Union[States, None]]
    state_attributes: Mapped[Union[StateAttributes, None]]
    def __repr__(self) -> str: ...
    @property
    def _last_updated_isotime(self) -> Union[str, None]: ...
    @staticmethod
    def from_event(event: Event) -> States: ...
    def to_native(self, validate_entity_id: bool = ...) -> Union[State, None]: ...

class StateAttributes(Base):
    __table_args__: Incomplete
    __tablename__: Incomplete
    attributes_id: Mapped[int]
    hash: Mapped[Union[int, None]]
    shared_attrs: Mapped[Union[str, None]]
    def __repr__(self) -> str: ...
    @staticmethod
    def shared_attrs_bytes_from_event(event: Event, entity_sources: dict[str, dict[str, str]], exclude_attrs_by_domain: dict[str, set[str]], dialect: Union[SupportedDialect, None]) -> bytes: ...
    @staticmethod
    def hash_shared_attrs_bytes(shared_attrs_bytes: bytes) -> int: ...
    def to_native(self) -> dict[str, Any]: ...

class StatisticsBase:
    id: Mapped[int]
    created: Mapped[Union[datetime, None]]
    created_ts: Mapped[Union[float, None]]
    metadata_id: Mapped[Union[int, None]]
    start: Mapped[Union[datetime, None]]
    start_ts: Mapped[Union[float, None]]
    mean: Mapped[Union[float, None]]
    min: Mapped[Union[float, None]]
    max: Mapped[Union[float, None]]
    last_reset: Mapped[Union[datetime, None]]
    last_reset_ts: Mapped[Union[float, None]]
    state: Mapped[Union[float, None]]
    sum: Mapped[Union[float, None]]
    duration: timedelta
    @classmethod
    def from_stats(cls, metadata_id: int, stats: StatisticData) -> Self: ...
    @classmethod
    def from_stats_ts(cls, metadata_id: int, stats: StatisticDataTimestamp) -> Self: ...

class Statistics(Base, StatisticsBase):
    duration: Incomplete
    __table_args__: Incomplete
    __tablename__: Incomplete

class StatisticsShortTerm(Base, StatisticsBase):
    duration: Incomplete
    __table_args__: Incomplete
    __tablename__: Incomplete

class StatisticsMeta(Base):
    __table_args__: Incomplete
    __tablename__: Incomplete
    id: Mapped[int]
    statistic_id: Mapped[Union[str, None]]
    source: Mapped[Union[str, None]]
    unit_of_measurement: Mapped[Union[str, None]]
    has_mean: Mapped[Union[bool, None]]
    has_sum: Mapped[Union[bool, None]]
    name: Mapped[Union[str, None]]
    @staticmethod
    def from_meta(meta: StatisticMetaData) -> StatisticsMeta: ...

class RecorderRuns(Base):
    __table_args__: Incomplete
    __tablename__: Incomplete
    run_id: Mapped[int]
    start: Mapped[datetime]
    end: Mapped[Union[datetime, None]]
    closed_incorrect: Mapped[bool]
    created: Mapped[datetime]
    def __repr__(self) -> str: ...
    def entity_ids(self, point_in_time: Union[datetime, None] = ...) -> list[str]: ...
    def to_native(self, validate_entity_id: bool = ...) -> Self: ...

class SchemaChanges(Base):
    __tablename__: Incomplete
    change_id: Mapped[int]
    schema_version: Mapped[Union[int, None]]
    changed: Mapped[datetime]
    def __repr__(self) -> str: ...

class StatisticsRuns(Base):
    __tablename__: Incomplete
    run_id: Mapped[int]
    start: Mapped[datetime]
    def __repr__(self) -> str: ...

EVENT_DATA_JSON: Incomplete
OLD_FORMAT_EVENT_DATA_JSON: Incomplete
SHARED_ATTRS_JSON: Incomplete
OLD_FORMAT_ATTRS_JSON: Incomplete
ENTITY_ID_IN_EVENT: ColumnElement
OLD_ENTITY_ID_IN_EVENT: ColumnElement
DEVICE_ID_IN_EVENT: ColumnElement
OLD_STATE: Incomplete
