import datetime
from . import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent, DOMAIN as DOMAIN
from homeassistant.components.automation import AutomationActionType as AutomationActionType, AutomationTriggerInfo as AutomationTriggerInfo
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_EVENT as CONF_EVENT, CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time, async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Any
EVENT_START: str
EVENT_END: str
UPDATE_INTERVAL: Any
TRIGGER_SCHEMA: Any

class CalendarEventListener:
    _hass: Any
    _job: Any
    _trigger_data: Any
    _entity: Any
    _unsub_event: Any
    _unsub_refresh: Any
    _events: Any
    _event_type: Any
    def __init__(self, hass: HomeAssistant, job: HassJob, trigger_data: dict[str, Any], entity: CalendarEntity, event_type: str) -> None: ...
    async def async_attach(self) -> None: ...
    def async_detach(self) -> None: ...
    async def _fetch_events(self, last_endtime: datetime.datetime) -> None: ...
    def _listen_next_calendar_event(self) -> None: ...
    def _clear_event_listener(self) -> None: ...
    async def _handle_calendar_event(self, now: datetime.datetime) -> None: ...
    def _dispatch_events(self, now: datetime.datetime) -> None: ...
    async def _handle_refresh(self, now: datetime.datetime) -> None: ...

async def async_attach_trigger(hass: HomeAssistant, config: ConfigType, action: AutomationActionType, automation_info: AutomationTriggerInfo) -> CALLBACK_TYPE: ...