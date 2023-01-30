from .const import ALL_DOMAIN_EXCLUDE_ATTRS as ALL_DOMAIN_EXCLUDE_ATTRS, SupportedDialect as SupportedDialect
from .models import StatisticData as StatisticData, StatisticMetaData as StatisticMetaData, process_timestamp as process_timestamp
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.const import MAX_LENGTH_EVENT_CONTEXT_ID as MAX_LENGTH_EVENT_CONTEXT_ID, MAX_LENGTH_EVENT_EVENT_TYPE as MAX_LENGTH_EVENT_EVENT_TYPE, MAX_LENGTH_EVENT_ORIGIN as MAX_LENGTH_EVENT_ORIGIN, MAX_LENGTH_STATE_ENTITY_ID as MAX_LENGTH_STATE_ENTITY_ID, MAX_LENGTH_STATE_STATE as MAX_LENGTH_STATE_STATE
from homeassistant.core import Context as Context, Event as Event, EventOrigin as EventOrigin, State as State, split_entity_id as split_entity_id
from homeassistant.helpers.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, JSON_DUMP as JSON_DUMP, json_bytes as json_bytes, json_bytes_strip_null as json_bytes_strip_null, json_loads as json_loads
from sqlalchemy import Column, JSON
from sqlalchemy.dialects import sqlite
from typing import Any, TypeVar

Base: Incomplete
SCHEMA_VERSION: int
_StatisticsBaseSelfT = TypeVar('_StatisticsBaseSelfT', bound='StatisticsBase')
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
ALL_TABLES: Incomplete
TABLES_TO_CHECK: Incomplete
LAST_UPDATED_INDEX_TS: str
ENTITY_ID_LAST_UPDATED_INDEX_TS: str
EVENTS_CONTEXT_ID_INDEX: str
STATES_CONTEXT_ID_INDEX: str

class FAST_PYSQLITE_DATETIME(sqlite.DATETIME):
    def result_processor(self, dialect, coltype): ...

JSON_VARIANT_CAST: Incomplete
JSONB_VARIANT_CAST: Incomplete
DATETIME_TYPE: Incomplete
DOUBLE_TYPE: Incomplete
TIMESTAMP_TYPE = DOUBLE_TYPE

class JSONLiteral(JSON):
    def literal_processor(self, dialect: str) -> Callable[[Any], str]: ...

EVENT_ORIGIN_ORDER: Incomplete
EVENT_ORIGIN_TO_IDX: Incomplete

class Events(Base):
    __table_args__: Incomplete
    __tablename__: Incomplete
    event_id: Incomplete
    event_type: Incomplete
    event_data: Incomplete
    origin: Incomplete
    origin_idx: Incomplete
    time_fired: Incomplete
    time_fired_ts: Incomplete
    context_id: Incomplete
    context_user_id: Incomplete
    context_parent_id: Incomplete
    data_id: Incomplete
    event_data_rel: Incomplete
    def __repr__(self) -> str: ...
    @property
    def _time_fired_isotime(self) -> str: ...
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
    def shared_data_bytes_from_event(event: Event, dialect: Union[SupportedDialect, None]) -> bytes: ...
    @staticmethod
    def hash_shared_data_bytes(shared_data_bytes: bytes) -> int: ...
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
    last_changed_ts: Incomplete
    last_updated: Incomplete
    last_updated_ts: Incomplete
    old_state_id: Incomplete
    attributes_id: Incomplete
    context_id: Incomplete
    context_user_id: Incomplete
    context_parent_id: Incomplete
    origin_idx: Incomplete
    old_state: Incomplete
    state_attributes: Incomplete
    def __repr__(self) -> str: ...
    @property
    def _last_updated_isotime(self) -> str: ...
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
    def shared_attrs_bytes_from_event(event: Event, exclude_attrs_by_domain: dict[str, set[str]], dialect: Union[SupportedDialect, None]) -> bytes: ...
    @staticmethod
    def hash_shared_attrs_bytes(shared_attrs_bytes: bytes) -> int: ...
    def to_native(self) -> dict[str, Any]: ...

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
    def from_stats(cls, metadata_id: int, stats: StatisticData) -> _StatisticsBaseSelfT: ...

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
