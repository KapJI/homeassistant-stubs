from .const import ALL_DOMAIN_EXCLUDE_ATTRS as ALL_DOMAIN_EXCLUDE_ATTRS, SupportedDialect as SupportedDialect
from .models import StatisticData as StatisticData, StatisticDataTimestamp as StatisticDataTimestamp, StatisticMetaData as StatisticMetaData, bytes_to_ulid_or_none as bytes_to_ulid_or_none, bytes_to_uuid_hex_or_none as bytes_to_uuid_hex_or_none, datetime_to_timestamp_or_none as datetime_to_timestamp_or_none, process_timestamp as process_timestamp, ulid_to_bytes_or_none as ulid_to_bytes_or_none, uuid_hex_to_bytes_or_none as uuid_hex_to_bytes_or_none
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime, timedelta
from homeassistant.const import MAX_LENGTH_EVENT_EVENT_TYPE as MAX_LENGTH_EVENT_EVENT_TYPE, MAX_LENGTH_STATE_ENTITY_ID as MAX_LENGTH_STATE_ENTITY_ID, MAX_LENGTH_STATE_STATE as MAX_LENGTH_STATE_STATE
from homeassistant.core import Context as Context, Event as Event, EventOrigin as EventOrigin, State as State
from homeassistant.helpers.entity import EntityInfo as EntityInfo
from homeassistant.helpers.json import JSON_DUMP as JSON_DUMP, json_bytes as json_bytes, json_bytes_strip_null as json_bytes_strip_null
from homeassistant.util.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, json_loads as json_loads, json_loads_object as json_loads_object
from sqlalchemy import CHAR, ColumnElement as ColumnElement, DateTime, JSON, LargeBinary
from sqlalchemy.dialects import sqlite
from sqlalchemy.engine.interfaces import Dialect as Dialect
from sqlalchemy.orm import DeclarativeBase, Mapped as Mapped
from sqlalchemy.types import TypeDecorator as TypeDecorator
from typing import Any, Self

class Base(DeclarativeBase): ...

SCHEMA_VERSION: int
_LOGGER: Incomplete
TABLE_EVENTS: str
TABLE_EVENT_DATA: str
TABLE_EVENT_TYPES: str
TABLE_STATES: str
TABLE_STATE_ATTRIBUTES: str
TABLE_STATES_META: str
TABLE_RECORDER_RUNS: str
TABLE_SCHEMA_CHANGES: str
TABLE_STATISTICS: str
TABLE_STATISTICS_META: str
TABLE_STATISTICS_RUNS: str
TABLE_STATISTICS_SHORT_TERM: str
STATISTICS_TABLES: Incomplete
MAX_STATE_ATTRS_BYTES: int
MAX_EVENT_DATA_BYTES: int
PSQL_DIALECT: Incomplete
ALL_TABLES: Incomplete
TABLES_TO_CHECK: Incomplete
LAST_UPDATED_INDEX_TS: str
METADATA_ID_LAST_UPDATED_INDEX_TS: str
EVENTS_CONTEXT_ID_BIN_INDEX: str
STATES_CONTEXT_ID_BIN_INDEX: str
LEGACY_STATES_EVENT_ID_INDEX: str
LEGACY_STATES_ENTITY_ID_LAST_UPDATED_INDEX: str
CONTEXT_ID_BIN_MAX_LENGTH: int
MYSQL_COLLATE: str
MYSQL_DEFAULT_CHARSET: str
MYSQL_ENGINE: str
_DEFAULT_TABLE_ARGS: Incomplete

class UnusedDateTime(DateTime): ...
class Unused(CHAR): ...

def compile_char_zero(type_: TypeDecorator, compiler: Any, **kw: Any) -> str: ...
def compile_char_one(type_: TypeDecorator, compiler: Any, **kw: Any) -> str: ...

class FAST_PYSQLITE_DATETIME(sqlite.DATETIME):
    def result_processor(self, dialect, coltype): ...

class NativeLargeBinary(LargeBinary):
    def result_processor(self, dialect, coltype) -> None: ...

UINT_32_TYPE: Incomplete
JSON_VARIANT_CAST: Incomplete
JSONB_VARIANT_CAST: Incomplete
DATETIME_TYPE: Incomplete
DOUBLE_TYPE: Incomplete
UNUSED_LEGACY_COLUMN: Incomplete
UNUSED_LEGACY_DATETIME_COLUMN: Incomplete
UNUSED_LEGACY_INTEGER_COLUMN: Incomplete
DOUBLE_PRECISION_TYPE_SQL: str
CONTEXT_BINARY_TYPE: Incomplete
TIMESTAMP_TYPE = DOUBLE_TYPE

class JSONLiteral(JSON):
    def literal_processor(self, dialect: Dialect) -> Callable[[Any], str]: ...

EVENT_ORIGIN_ORDER: Incomplete
EVENT_ORIGIN_TO_IDX: Incomplete

class Events(Base):
    __table_args__: Incomplete
    __tablename__ = TABLE_EVENTS
    event_id: Mapped[int]
    event_type: Mapped[str | None]
    event_data: Mapped[str | None]
    origin: Mapped[str | None]
    origin_idx: Mapped[int | None]
    time_fired: Mapped[datetime | None]
    time_fired_ts: Mapped[float | None]
    context_id: Mapped[str | None]
    context_user_id: Mapped[str | None]
    context_parent_id: Mapped[str | None]
    data_id: Mapped[int | None]
    context_id_bin: Mapped[bytes | None]
    context_user_id_bin: Mapped[bytes | None]
    context_parent_id_bin: Mapped[bytes | None]
    event_type_id: Mapped[int | None]
    event_data_rel: Mapped[EventData | None]
    event_type_rel: Mapped[EventTypes | None]
    def __repr__(self) -> str: ...
    @property
    def _time_fired_isotime(self) -> str | None: ...
    @staticmethod
    def from_event(event: Event) -> Events: ...
    def to_native(self, validate_entity_id: bool = ...) -> Event | None: ...

class EventData(Base):
    __table_args__: Incomplete
    __tablename__ = TABLE_EVENT_DATA
    data_id: Mapped[int]
    hash: Mapped[int | None]
    shared_data: Mapped[str | None]
    def __repr__(self) -> str: ...
    @staticmethod
    def shared_data_bytes_from_event(event: Event, dialect: SupportedDialect | None) -> bytes: ...
    @staticmethod
    def hash_shared_data_bytes(shared_data_bytes: bytes) -> int: ...
    def to_native(self) -> dict[str, Any]: ...

class EventTypes(Base):
    __table_args__: Incomplete
    __tablename__ = TABLE_EVENT_TYPES
    event_type_id: Mapped[int]
    event_type: Mapped[str | None]
    def __repr__(self) -> str: ...

class States(Base):
    __table_args__: Incomplete
    __tablename__ = TABLE_STATES
    state_id: Mapped[int]
    entity_id: Mapped[str | None]
    state: Mapped[str | None]
    attributes: Mapped[str | None]
    event_id: Mapped[int | None]
    last_changed: Mapped[datetime | None]
    last_changed_ts: Mapped[float | None]
    last_updated: Mapped[datetime | None]
    last_updated_ts: Mapped[float | None]
    old_state_id: Mapped[int | None]
    attributes_id: Mapped[int | None]
    context_id: Mapped[str | None]
    context_user_id: Mapped[str | None]
    context_parent_id: Mapped[str | None]
    origin_idx: Mapped[int | None]
    old_state: Mapped[States | None]
    state_attributes: Mapped[StateAttributes | None]
    context_id_bin: Mapped[bytes | None]
    context_user_id_bin: Mapped[bytes | None]
    context_parent_id_bin: Mapped[bytes | None]
    metadata_id: Mapped[int | None]
    states_meta_rel: Mapped[StatesMeta | None]
    def __repr__(self) -> str: ...
    @property
    def _last_updated_isotime(self) -> str | None: ...
    @staticmethod
    def from_event(event: Event) -> States: ...
    def to_native(self, validate_entity_id: bool = ...) -> State | None: ...

class StateAttributes(Base):
    __table_args__: Incomplete
    __tablename__ = TABLE_STATE_ATTRIBUTES
    attributes_id: Mapped[int]
    hash: Mapped[int | None]
    shared_attrs: Mapped[str | None]
    def __repr__(self) -> str: ...
    @staticmethod
    def shared_attrs_bytes_from_event(event: Event, entity_sources: dict[str, EntityInfo], dialect: SupportedDialect | None) -> bytes: ...
    @staticmethod
    def hash_shared_attrs_bytes(shared_attrs_bytes: bytes) -> int: ...
    def to_native(self) -> dict[str, Any]: ...

class StatesMeta(Base):
    __table_args__: Incomplete
    __tablename__ = TABLE_STATES_META
    metadata_id: Mapped[int]
    entity_id: Mapped[str | None]
    def __repr__(self) -> str: ...

class StatisticsBase:
    id: Mapped[int]
    created: Mapped[datetime | None]
    created_ts: Mapped[float | None]
    metadata_id: Mapped[int | None]
    start: Mapped[datetime | None]
    start_ts: Mapped[float | None]
    mean: Mapped[float | None]
    min: Mapped[float | None]
    max: Mapped[float | None]
    last_reset: Mapped[datetime | None]
    last_reset_ts: Mapped[float | None]
    state: Mapped[float | None]
    sum: Mapped[float | None]
    duration: timedelta
    @classmethod
    def from_stats(cls, metadata_id: int, stats: StatisticData) -> Self: ...
    @classmethod
    def from_stats_ts(cls, metadata_id: int, stats: StatisticDataTimestamp) -> Self: ...

class Statistics(Base, StatisticsBase):
    duration: Incomplete
    __table_args__: Incomplete
    __tablename__ = TABLE_STATISTICS

class StatisticsShortTerm(Base, StatisticsBase):
    duration: Incomplete
    __table_args__: Incomplete
    __tablename__ = TABLE_STATISTICS_SHORT_TERM

class StatisticsMeta(Base):
    __table_args__: Incomplete
    __tablename__ = TABLE_STATISTICS_META
    id: Mapped[int]
    statistic_id: Mapped[str | None]
    source: Mapped[str | None]
    unit_of_measurement: Mapped[str | None]
    has_mean: Mapped[bool | None]
    has_sum: Mapped[bool | None]
    name: Mapped[str | None]
    @staticmethod
    def from_meta(meta: StatisticMetaData) -> StatisticsMeta: ...

class RecorderRuns(Base):
    __table_args__: Incomplete
    __tablename__ = TABLE_RECORDER_RUNS
    run_id: Mapped[int]
    start: Mapped[datetime]
    end: Mapped[datetime | None]
    closed_incorrect: Mapped[bool]
    created: Mapped[datetime]
    def __repr__(self) -> str: ...
    def to_native(self, validate_entity_id: bool = ...) -> Self: ...

class SchemaChanges(Base):
    __tablename__ = TABLE_SCHEMA_CHANGES
    change_id: Mapped[int]
    schema_version: Mapped[int | None]
    changed: Mapped[datetime]
    def __repr__(self) -> str: ...

class StatisticsRuns(Base):
    __tablename__ = TABLE_STATISTICS_RUNS
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
SHARED_ATTR_OR_LEGACY_ATTRIBUTES: Incomplete
SHARED_DATA_OR_LEGACY_EVENT_DATA: Incomplete
