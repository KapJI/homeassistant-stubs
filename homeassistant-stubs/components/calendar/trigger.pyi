import datetime
from . import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Coroutine
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_EVENT as CONF_EVENT, CONF_OFFSET as CONF_OFFSET, CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time, async_track_time_interval as async_track_time_interval
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerInfo as TriggerInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete
EVENT_START: str
EVENT_END: str
UPDATE_INTERVAL: Incomplete
TRIGGER_SCHEMA: Incomplete

class CalendarEventListener:
    _hass: Incomplete
    _job: Incomplete
    _trigger_data: Incomplete
    _entity: Incomplete
    _offset: Incomplete
    _unsub_event: Incomplete
    _unsub_refresh: Incomplete
    _events: Incomplete
    _event_type: Incomplete
    def __init__(self, hass: HomeAssistant, job: HassJob[..., Coroutine[Any, Any, None]], trigger_data: dict[str, Any], entity: CalendarEntity, event_type: str, offset: datetime.timedelta) -> None: ...
    async def async_attach(self) -> None: ...
    def async_detach(self) -> None: ...
    async def _fetch_events(self, last_endtime: datetime.datetime) -> None: ...
    def _listen_next_calendar_event(self) -> None: ...
    def _clear_event_listener(self) -> None: ...
    async def _handle_calendar_event(self, now: datetime.datetime) -> None: ...
    def _dispatch_events(self, now: datetime.datetime) -> None: ...
    async def _handle_refresh(self, now: datetime.datetime) -> None: ...

async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: TriggerActionType, trigger_info: TriggerInfo) -> CALLBACK_TYPE: ...
