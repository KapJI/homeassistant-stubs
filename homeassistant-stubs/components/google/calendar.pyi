from . import CONF_CAL_ID as CONF_CAL_ID, CONF_IGNORE_AVAILABILITY as CONF_IGNORE_AVAILABILITY, CONF_SEARCH as CONF_SEARCH, CONF_TRACK as CONF_TRACK, DATA_SERVICE as DATA_SERVICE, DEFAULT_CONF_OFFSET as DEFAULT_CONF_OFFSET, DOMAIN as DOMAIN, SERVICE_SCAN_CALENDARS as SERVICE_SCAN_CALENDARS
from .const import DISCOVER_CALENDAR as DISCOVER_CALENDAR
from _typeshed import Incomplete
from datetime import datetime
from gcal_sync.api import GoogleCalendarService as GoogleCalendarService
from gcal_sync.model import Event as Event
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent, ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, extract_offset as extract_offset, is_offset_reached as is_offset_reached
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_OFFSET as CONF_OFFSET
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, PlatformNotReady as PlatformNotReady
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import generate_entity_id as generate_entity_id
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import Throttle as Throttle
from typing import Any

_LOGGER: Incomplete
DEFAULT_GOOGLE_SEARCH_PARAMS: Incomplete
MIN_TIME_BETWEEN_UPDATES: Incomplete
TRANSPARENCY: str
OPAQUE: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _async_setup_entities(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback, disc_info: dict[str, Any]) -> None: ...

class GoogleCalendarEntity(CalendarEntity):
    _calendar_service: Incomplete
    _calendar_id: Incomplete
    _search: Incomplete
    _ignore_availability: Incomplete
    _event: Incomplete
    _name: Incomplete
    _offset: Incomplete
    _offset_value: Incomplete
    entity_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    def __init__(self, calendar_service: GoogleCalendarService, calendar_id: str, data: dict[str, Any], entity_id: str, unique_id: str, entity_enabled: bool) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, bool]: ...
    @property
    def offset_reached(self) -> bool: ...
    @property
    def event(self) -> Union[CalendarEvent, None]: ...
    @property
    def name(self) -> str: ...
    def _event_filter(self, event: Event) -> bool: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
    async def async_update(self) -> None: ...

def _get_calendar_event(event: Event) -> CalendarEvent: ...
