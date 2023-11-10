from .state_attributes import decode_attributes_from_source as decode_attributes_from_source
from .time import process_timestamp as process_timestamp
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.const import COMPRESSED_STATE_ATTRIBUTES as COMPRESSED_STATE_ATTRIBUTES, COMPRESSED_STATE_LAST_CHANGED as COMPRESSED_STATE_LAST_CHANGED, COMPRESSED_STATE_LAST_UPDATED as COMPRESSED_STATE_LAST_UPDATED, COMPRESSED_STATE_STATE as COMPRESSED_STATE_STATE
from homeassistant.core import Context as Context, State as State
from sqlalchemy.engine.row import Row as Row
from typing import Any

_LOGGER: Incomplete

def extract_metadata_ids(entity_id_to_metadata_id: dict[str, int | None]) -> list[int]: ...

class LazyState(State):
    __slots__: Incomplete
    _row: Incomplete
    entity_id: Incomplete
    state: Incomplete
    _attributes: Incomplete
    _last_updated_ts: Incomplete
    _last_changed_ts: Incomplete
    _context: Incomplete
    attr_cache: Incomplete
    def __init__(self, row: Row, attr_cache: dict[str, dict[str, Any]], start_time_ts: float | None, entity_id: str, state: str, last_updated_ts: float | None, no_attributes: bool) -> None: ...
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

def row_to_compressed_state(row: Row, attr_cache: dict[str, dict[str, Any]], start_time_ts: float | None, entity_id: str, state: str, last_updated_ts: float | None, no_attributes: bool) -> dict[str, Any]: ...
