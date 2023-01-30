from .const import ATTR_MESSAGE as ATTR_MESSAGE, CONTEXT_DOMAIN as CONTEXT_DOMAIN, CONTEXT_ENTITY_ID as CONTEXT_ENTITY_ID, CONTEXT_ENTITY_ID_NAME as CONTEXT_ENTITY_ID_NAME, CONTEXT_EVENT_TYPE as CONTEXT_EVENT_TYPE, CONTEXT_MESSAGE as CONTEXT_MESSAGE, CONTEXT_NAME as CONTEXT_NAME, CONTEXT_SERVICE as CONTEXT_SERVICE, CONTEXT_SOURCE as CONTEXT_SOURCE, CONTEXT_STATE as CONTEXT_STATE, CONTEXT_USER_ID as CONTEXT_USER_ID, DOMAIN as DOMAIN, LOGBOOK_ENTRY_DOMAIN as LOGBOOK_ENTRY_DOMAIN, LOGBOOK_ENTRY_ENTITY_ID as LOGBOOK_ENTRY_ENTITY_ID, LOGBOOK_ENTRY_ICON as LOGBOOK_ENTRY_ICON, LOGBOOK_ENTRY_MESSAGE as LOGBOOK_ENTRY_MESSAGE, LOGBOOK_ENTRY_NAME as LOGBOOK_ENTRY_NAME, LOGBOOK_ENTRY_SOURCE as LOGBOOK_ENTRY_SOURCE, LOGBOOK_ENTRY_STATE as LOGBOOK_ENTRY_STATE, LOGBOOK_ENTRY_WHEN as LOGBOOK_ENTRY_WHEN, LOGBOOK_FILTERS as LOGBOOK_FILTERS
from .helpers import is_sensor_continuous as is_sensor_continuous
from .models import EventAsRow as EventAsRow, LazyEventPartialState as LazyEventPartialState, async_event_to_row as async_event_to_row
from .queries import statement_for_request as statement_for_request
from .queries.common import PSEUDO_EVENT_STATE_CHANGED as PSEUDO_EVENT_STATE_CHANGED
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Generator
from datetime import datetime as dt
from homeassistant.components.recorder.filters import Filters as Filters
from homeassistant.components.recorder.models import process_datetime_to_timestamp as process_datetime_to_timestamp, process_timestamp_to_utc_isoformat as process_timestamp_to_utc_isoformat
from homeassistant.components.recorder.util import session_scope as session_scope
from homeassistant.const import ATTR_DOMAIN as ATTR_DOMAIN, ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, ATTR_NAME as ATTR_NAME, ATTR_SERVICE as ATTR_SERVICE, EVENT_CALL_SERVICE as EVENT_CALL_SERVICE, EVENT_LOGBOOK_ENTRY as EVENT_LOGBOOK_ENTRY
from homeassistant.core import HomeAssistant as HomeAssistant, split_entity_id as split_entity_id
from homeassistant.helpers import entity_registry as er
from sqlalchemy.engine.row import Row as Row
from sqlalchemy.orm.query import Query as Query
from typing import Any

class LogbookRun:
    context_lookup: ContextLookup
    external_events: dict[str, tuple[str, Callable[[LazyEventPartialState], dict[str, Any]]]]
    event_cache: EventCache
    entity_name_cache: EntityNameCache
    include_entity_name: bool
    format_time: Callable[[Row], Any]
    def __init__(self, context_lookup, external_events, event_cache, entity_name_cache, include_entity_name, format_time) -> None: ...

class EventProcessor:
    hass: Incomplete
    ent_reg: Incomplete
    event_types: Incomplete
    entity_ids: Incomplete
    device_ids: Incomplete
    context_id: Incomplete
    filters: Incomplete
    logbook_run: Incomplete
    context_augmenter: Incomplete
    def __init__(self, hass: HomeAssistant, event_types: tuple[str, ...], entity_ids: Union[list[str], None] = ..., device_ids: Union[list[str], None] = ..., context_id: Union[str, None] = ..., timestamp: bool = ..., include_entity_name: bool = ...) -> None: ...
    @property
    def limited_select(self) -> bool: ...
    def switch_to_live(self) -> None: ...
    def get_events(self, start_day: dt, end_day: dt) -> list[dict[str, Any]]: ...
    def humanify(self, row_generator: Generator[Union[Row, EventAsRow], None, None]) -> list[dict[str, str]]: ...

def _humanify(rows: Generator[Union[Row, EventAsRow], None, None], ent_reg: er.EntityRegistry, logbook_run: LogbookRun, context_augmenter: ContextAugmenter) -> Generator[dict[str, Any], None, None]: ...

class ContextLookup:
    hass: Incomplete
    _memorize_new: bool
    _lookup: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def memorize(self, row: Row) -> Union[str, None]: ...
    def clear(self) -> None: ...
    def get(self, context_id: str) -> Union[Row, None]: ...

class ContextAugmenter:
    context_lookup: Incomplete
    entity_name_cache: Incomplete
    external_events: Incomplete
    event_cache: Incomplete
    include_entity_name: Incomplete
    def __init__(self, logbook_run: LogbookRun) -> None: ...
    def _get_context_row(self, context_id: Union[str, None], row: Union[Row, EventAsRow]) -> Union[Row, EventAsRow]: ...
    def augment(self, data: dict[str, Any], row: Union[Row, EventAsRow], context_id: Union[str, None]) -> None: ...

def _rows_match(row: Union[Row, EventAsRow], other_row: Union[Row, EventAsRow]) -> bool: ...
def _row_time_fired_isoformat(row: Union[Row, EventAsRow]) -> str: ...
def _row_time_fired_timestamp(row: Union[Row, EventAsRow]) -> float: ...

class EntityNameCache:
    _hass: Incomplete
    _names: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def get(self, entity_id: str) -> str: ...

class EventCache:
    _event_data_cache: Incomplete
    event_cache: Incomplete
    def __init__(self, event_data_cache: dict[str, dict[str, Any]]) -> None: ...
    def get(self, row: Union[EventAsRow, Row]) -> LazyEventPartialState: ...
    def clear(self) -> None: ...
