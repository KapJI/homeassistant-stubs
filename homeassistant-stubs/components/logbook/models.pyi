from _typeshed import Incomplete
from homeassistant.const import ATTR_ICON as ATTR_ICON, EVENT_STATE_CHANGED as EVENT_STATE_CHANGED
from homeassistant.core import Context as Context, Event as Event, State as State, callback as callback
from sqlalchemy.engine.row import Row as Row
from typing import Any

class LazyEventPartialState:
    __slots__: Incomplete
    row: Incomplete
    _event_data: Incomplete
    _event_data_cache: Incomplete
    event_type: Incomplete
    entity_id: Incomplete
    state: Incomplete
    context_id: Incomplete
    context_user_id: Incomplete
    context_parent_id: Incomplete
    data: Incomplete
    def __init__(self, row: Union[Row, EventAsRow], event_data_cache: dict[str, dict[str, Any]]) -> None: ...

class EventAsRow:
    data: dict[str, Any]
    context: Context
    context_id: str
    time_fired_ts: float
    state_id: int
    event_data: Union[str, None]
    old_format_icon: None
    event_id: None
    entity_id: Union[str, None]
    icon: Union[str, None]
    context_user_id: Union[str, None]
    context_parent_id: Union[str, None]
    event_type: Union[str, None]
    state: Union[str, None]
    shared_data: Union[str, None]
    context_only: None
    def __init__(self, data, context, context_id, time_fired_ts, state_id, event_data, old_format_icon, event_id, entity_id, icon, context_user_id, context_parent_id, event_type, state, shared_data, context_only) -> None: ...

def async_event_to_row(event: Event) -> Union[EventAsRow, None]: ...
