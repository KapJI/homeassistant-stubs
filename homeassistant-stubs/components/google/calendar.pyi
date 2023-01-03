from . import CONF_IGNORE_AVAILABILITY as CONF_IGNORE_AVAILABILITY, CONF_SEARCH as CONF_SEARCH, CONF_TRACK as CONF_TRACK, DEFAULT_CONF_OFFSET as DEFAULT_CONF_OFFSET, DOMAIN as DOMAIN, YAML_DEVICES as YAML_DEVICES, get_calendar_info as get_calendar_info, load_config as load_config, update_config as update_config
from .api import get_feature_access as get_feature_access
from .const import DATA_SERVICE as DATA_SERVICE, DATA_STORE as DATA_STORE, EVENT_DESCRIPTION as EVENT_DESCRIPTION, EVENT_END_DATE as EVENT_END_DATE, EVENT_END_DATETIME as EVENT_END_DATETIME, EVENT_IN as EVENT_IN, EVENT_IN_DAYS as EVENT_IN_DAYS, EVENT_IN_WEEKS as EVENT_IN_WEEKS, EVENT_START_DATE as EVENT_START_DATE, EVENT_START_DATETIME as EVENT_START_DATETIME, EVENT_SUMMARY as EVENT_SUMMARY, EVENT_TYPES_CONF as EVENT_TYPES_CONF, FeatureAccess as FeatureAccess
from _typeshed import Incomplete
from collections.abc import Iterable
from datetime import datetime
from gcal_sync.api import GoogleCalendarService as GoogleCalendarService
from gcal_sync.model import Event
from gcal_sync.sync import CalendarEventSyncManager
from gcal_sync.timeline import Timeline
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent, ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, extract_offset as extract_offset, is_offset_reached as is_offset_reached
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_OFFSET as CONF_OFFSET
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, PlatformNotReady as PlatformNotReady
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity import generate_entity_id as generate_entity_id
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

_LOGGER: Incomplete
MIN_TIME_BETWEEN_UPDATES: Incomplete
SYNC_EVENT_MIN_TIME: Incomplete
OPAQUE: str
_EVENT_IN_TYPES: Incomplete
SERVICE_CREATE_EVENT: str
CREATE_EVENT_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CalendarSyncUpdateCoordinator(DataUpdateCoordinator[Timeline]):
    sync: Incomplete
    def __init__(self, hass: HomeAssistant, sync: CalendarEventSyncManager, name: str) -> None: ...
    async def _async_update_data(self) -> Timeline: ...
    async def async_get_events(self, start_date: datetime, end_date: datetime) -> Iterable[Event]: ...
    @property
    def upcoming(self) -> Union[Iterable[Event], None]: ...

class CalendarQueryUpdateCoordinator(DataUpdateCoordinator[list[Event]]):
    calendar_service: Incomplete
    calendar_id: Incomplete
    _search: Incomplete
    def __init__(self, hass: HomeAssistant, calendar_service: GoogleCalendarService, name: str, calendar_id: str, search: Union[str, None]) -> None: ...
    async def async_get_events(self, start_date: datetime, end_date: datetime) -> Iterable[Event]: ...
    async def _async_update_data(self) -> list[Event]: ...
    @property
    def upcoming(self) -> Union[Iterable[Event], None]: ...

class GoogleCalendarEntity(CoordinatorEntity, CalendarEntity):
    _attr_has_entity_name: bool
    coordinator: Incomplete
    calendar_id: Incomplete
    _ignore_availability: Incomplete
    _event: Incomplete
    _attr_name: Incomplete
    _offset: Incomplete
    _offset_value: Incomplete
    entity_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    def __init__(self, coordinator: Union[CalendarSyncUpdateCoordinator, CalendarQueryUpdateCoordinator], calendar_id: str, data: dict[str, Any], entity_id: str, unique_id: Union[str, None], entity_enabled: bool) -> None: ...
    @property
    def should_poll(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, bool]: ...
    @property
    def offset_reached(self) -> bool: ...
    @property
    def event(self) -> Union[CalendarEvent, None]: ...
    def _event_filter(self, event: Event) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
    def _apply_coordinator_update(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_update(self) -> None: ...

def _get_calendar_event(event: Event) -> CalendarEvent: ...
async def async_create_event(entity: GoogleCalendarEntity, call: ServiceCall) -> None: ...
