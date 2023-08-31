from . import CONF_IGNORE_AVAILABILITY as CONF_IGNORE_AVAILABILITY, CONF_SEARCH as CONF_SEARCH, CONF_TRACK as CONF_TRACK, DEFAULT_CONF_OFFSET as DEFAULT_CONF_OFFSET, DOMAIN as DOMAIN, YAML_DEVICES as YAML_DEVICES, get_calendar_info as get_calendar_info, load_config as load_config, update_config as update_config
from .api import get_feature_access as get_feature_access
from .const import DATA_SERVICE as DATA_SERVICE, DATA_STORE as DATA_STORE, EVENT_END_DATE as EVENT_END_DATE, EVENT_END_DATETIME as EVENT_END_DATETIME, EVENT_IN as EVENT_IN, EVENT_IN_DAYS as EVENT_IN_DAYS, EVENT_IN_WEEKS as EVENT_IN_WEEKS, EVENT_START_DATE as EVENT_START_DATE, EVENT_START_DATETIME as EVENT_START_DATETIME, FeatureAccess as FeatureAccess
from _typeshed import Incomplete
from collections.abc import Iterable
from datetime import datetime, timedelta
from gcal_sync.api import GoogleCalendarService as GoogleCalendarService
from gcal_sync.model import Event
from gcal_sync.sync import CalendarEventSyncManager
from gcal_sync.timeline import Timeline
from homeassistant.components.calendar import CREATE_EVENT_SCHEMA as CREATE_EVENT_SCHEMA, CalendarEntity as CalendarEntity, CalendarEntityFeature as CalendarEntityFeature, CalendarEvent as CalendarEvent, ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, EVENT_DESCRIPTION as EVENT_DESCRIPTION, EVENT_END as EVENT_END, EVENT_LOCATION as EVENT_LOCATION, EVENT_RRULE as EVENT_RRULE, EVENT_START as EVENT_START, EVENT_SUMMARY as EVENT_SUMMARY, extract_offset as extract_offset, is_offset_reached as is_offset_reached
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_OFFSET as CONF_OFFSET
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
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
RRULE_PREFIX: str
SERVICE_CREATE_EVENT: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CalendarSyncUpdateCoordinator(DataUpdateCoordinator[Timeline]):
    config_entry: ConfigEntry
    sync: Incomplete
    def __init__(self, hass: HomeAssistant, sync: CalendarEventSyncManager, name: str) -> None: ...
    async def _async_update_data(self) -> Timeline: ...
    async def async_get_events(self, start_date: datetime, end_date: datetime) -> Iterable[Event]: ...
    @property
    def upcoming(self) -> Iterable[Event] | None: ...

class CalendarQueryUpdateCoordinator(DataUpdateCoordinator[list[Event]]):
    config_entry: ConfigEntry
    calendar_service: Incomplete
    calendar_id: Incomplete
    _search: Incomplete
    def __init__(self, hass: HomeAssistant, calendar_service: GoogleCalendarService, name: str, calendar_id: str, search: str | None) -> None: ...
    async def async_get_events(self, start_date: datetime, end_date: datetime) -> Iterable[Event]: ...
    async def _async_update_data(self) -> list[Event]: ...
    @property
    def upcoming(self) -> Iterable[Event] | None: ...

class GoogleCalendarEntity(CoordinatorEntity[CalendarSyncUpdateCoordinator | CalendarQueryUpdateCoordinator], CalendarEntity):
    _attr_has_entity_name: bool
    calendar_id: Incomplete
    _ignore_availability: Incomplete
    _event: Incomplete
    _attr_name: Incomplete
    _offset: Incomplete
    entity_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, coordinator: CalendarSyncUpdateCoordinator | CalendarQueryUpdateCoordinator, calendar_id: str, data: dict[str, Any], entity_id: str, unique_id: str | None, entity_enabled: bool, supports_write: bool) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, bool]: ...
    @property
    def offset_reached(self) -> bool: ...
    @property
    def event(self) -> CalendarEvent | None: ...
    def _event_filter(self, event: Event) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
    def _event_with_offset(self) -> tuple[CalendarEvent | None, timedelta | None]: ...
    async def async_create_event(self, **kwargs: Any) -> None: ...
    async def async_delete_event(self, uid: str, recurrence_id: str | None = ..., recurrence_range: str | None = ...) -> None: ...

def _get_calendar_event(event: Event) -> CalendarEvent: ...
async def async_create_event(entity: GoogleCalendarEntity, call: ServiceCall) -> None: ...
