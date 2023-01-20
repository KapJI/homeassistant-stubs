import asyncio
from .const import LOGBOOK_ENTITIES_FILTER as LOGBOOK_ENTITIES_FILTER
from .helpers import async_determine_event_types as async_determine_event_types, async_filter_entities as async_filter_entities, async_subscribe_events as async_subscribe_events
from .models import async_event_to_row as async_event_to_row
from .processor import EventProcessor as EventProcessor
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime as dt
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.recorder import get_instance as get_instance
from homeassistant.components.websocket_api import messages as messages
from homeassistant.components.websocket_api.connection import ActiveConnection as ActiveConnection
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entityfilter import EntityFilter as EntityFilter
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time
from homeassistant.helpers.json import JSON_DUMP as JSON_DUMP
from typing import Any

MAX_PENDING_LOGBOOK_EVENTS: int
EVENT_COALESCE_TIME: float
BIG_QUERY_HOURS: int
BIG_QUERY_RECENT_HOURS: int
_LOGGER: Incomplete

class LogbookLiveStream:
    stream_queue: asyncio.Queue[Event]
    subscriptions: list[CALLBACK_TYPE]
    end_time_unsub: Union[CALLBACK_TYPE, None]
    task: Union[asyncio.Task, None]
    wait_sync_task: Union[asyncio.Task, None]
    def __init__(self, stream_queue, subscriptions, end_time_unsub, task, wait_sync_task) -> None: ...

def async_setup(hass: HomeAssistant) -> None: ...
def _async_send_empty_response(connection: ActiveConnection, msg_id: int, start_time: dt, end_time: Union[dt, None]) -> None: ...
async def _async_send_historical_events(hass: HomeAssistant, connection: ActiveConnection, msg_id: int, start_time: dt, end_time: dt, formatter: Callable[[int, Any], dict[str, Any]], event_processor: EventProcessor, partial: bool, force_send: bool = ...) -> Union[dt, None]: ...
async def _async_get_ws_stream_events(hass: HomeAssistant, msg_id: int, start_time: dt, end_time: dt, formatter: Callable[[int, Any], dict[str, Any]], event_processor: EventProcessor, partial: bool) -> tuple[str, Union[dt, None]]: ...
def _generate_stream_message(events: list[dict[str, Any]], start_day: dt, end_day: dt) -> dict[str, Any]: ...
def _ws_stream_get_events(msg_id: int, start_day: dt, end_day: dt, formatter: Callable[[int, Any], dict[str, Any]], event_processor: EventProcessor, partial: bool) -> tuple[str, Union[dt, None]]: ...
async def _async_events_consumer(subscriptions_setup_complete_time: dt, connection: ActiveConnection, msg_id: int, stream_queue: asyncio.Queue[Event], event_processor: EventProcessor) -> None: ...
async def ws_event_stream(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def _ws_formatted_get_events(msg_id: int, start_time: dt, end_time: dt, event_processor: EventProcessor) -> str: ...
async def ws_get_events(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
