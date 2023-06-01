from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.recorder.filters import Filters as Filters
from homeassistant.components.recorder.models import bytes_to_ulid_or_none as bytes_to_ulid_or_none, bytes_to_uuid_hex_or_none as bytes_to_uuid_hex_or_none, ulid_to_bytes_or_none as ulid_to_bytes_or_none, uuid_hex_to_bytes_or_none as uuid_hex_to_bytes_or_none
from homeassistant.const import ATTR_ICON as ATTR_ICON, EVENT_STATE_CHANGED as EVENT_STATE_CHANGED
from homeassistant.core import Context as Context, Event as Event, State as State, callback as callback
from homeassistant.util.json import json_loads as json_loads
from homeassistant.util.ulid import ulid_to_bytes as ulid_to_bytes
from sqlalchemy.engine.row import Row as Row
from typing import Any

class LogbookConfig:
    external_events: dict[str, tuple[str, Callable[[LazyEventPartialState], dict[str, Any]]]]
    sqlalchemy_filter: Filters | None
    entity_filter: Callable[[str], bool] | None
    def __init__(self, external_events, sqlalchemy_filter, entity_filter) -> None: ...

class LazyEventPartialState:
    __slots__: Incomplete
    row: Incomplete
    _event_data: Incomplete
    _event_data_cache: Incomplete
    event_type: Incomplete
    entity_id: Incomplete
    state: Incomplete
    context_id_bin: Incomplete
    context_user_id_bin: Incomplete
    context_parent_id_bin: Incomplete
    data: Incomplete
    def __init__(self, row: Row | EventAsRow, event_data_cache: dict[str, dict[str, Any]]) -> None: ...
    @property
    def context_id(self) -> str | None: ...
    @property
    def context_user_id(self) -> str | None: ...
    @property
    def context_parent_id(self) -> str | None: ...

class EventAsRow:
    data: dict[str, Any]
    context: Context
    context_id_bin: bytes
    time_fired_ts: float
    row_id: int
    event_data: str | None
    entity_id: str | None
    icon: str | None
    context_user_id_bin: bytes | None
    context_parent_id_bin: bytes | None
    event_type: str | None
    state: str | None
    context_only: None
    def __init__(self, data, context, context_id_bin, time_fired_ts, row_id, event_data, entity_id, icon, context_user_id_bin, context_parent_id_bin, event_type, state, context_only) -> None: ...

def async_event_to_row(event: Event) -> EventAsRow: ...
