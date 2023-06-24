from .state_attributes import decode_attributes_from_source as decode_attributes_from_source
from .time import process_datetime_to_timestamp as process_datetime_to_timestamp, process_timestamp as process_timestamp, process_timestamp_to_utc_isoformat as process_timestamp_to_utc_isoformat
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.const import COMPRESSED_STATE_ATTRIBUTES as COMPRESSED_STATE_ATTRIBUTES, COMPRESSED_STATE_LAST_CHANGED as COMPRESSED_STATE_LAST_CHANGED, COMPRESSED_STATE_LAST_UPDATED as COMPRESSED_STATE_LAST_UPDATED, COMPRESSED_STATE_STATE as COMPRESSED_STATE_STATE
from homeassistant.core import Context as Context, State as State
from sqlalchemy.engine.row import Row as Row
from typing import Any

class LegacyLazyStatePreSchema31(State):
    __slots__: Incomplete
    _row: Incomplete
    entity_id: Incomplete
    state: Incomplete
    _attributes: Incomplete
    _last_changed: Incomplete
    _last_updated: Incomplete
    _context: Incomplete
    attr_cache: Incomplete
    def __init__(self, row: Row, attr_cache: dict[str, dict[str, Any]], start_time: datetime | None) -> None: ...
    @property
    def attributes(self) -> dict[str, Any]: ...
    @property
    def context(self) -> Context: ...
    @property
    def last_changed(self) -> datetime: ...
    @property
    def last_updated(self) -> datetime: ...
    def as_dict(self) -> dict[str, Any]: ...

def legacy_row_to_compressed_state_pre_schema_31(row: Row, attr_cache: dict[str, dict[str, Any]], start_time: datetime | None) -> dict[str, Any]: ...

class LegacyLazyState(State):
    __slots__: Incomplete
    _row: Incomplete
    entity_id: Incomplete
    state: Incomplete
    _attributes: Incomplete
    _last_updated_ts: Incomplete
    _last_changed_ts: Incomplete
    _context: Incomplete
    attr_cache: Incomplete
    def __init__(self, row: Row, attr_cache: dict[str, dict[str, Any]], start_time: datetime | None, entity_id: str | None = ...) -> None: ...
    @property
    def attributes(self) -> dict[str, Any]: ...
    @property
    def context(self) -> Context: ...
    @property
    def last_changed(self) -> datetime: ...
    @property
    def last_updated(self) -> datetime: ...
    def as_dict(self) -> dict[str, Any]: ...

def legacy_row_to_compressed_state(row: Row, attr_cache: dict[str, dict[str, Any]], start_time: datetime | None, entity_id: str | None = ...) -> dict[str, Any]: ...
def decode_attributes_from_row_legacy(row: Row, attr_cache: dict[str, dict[str, Any]]) -> dict[str, Any]: ...
