from . import RemoteCalendarConfigEntry as RemoteCalendarConfigEntry
from .const import CONF_CALENDAR_NAME as CONF_CALENDAR_NAME
from .coordinator import RemoteCalendarDataUpdateCoordinator as RemoteCalendarDataUpdateCoordinator
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from ical.event import Event as Event

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: RemoteCalendarConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RemoteCalendarEntity(CoordinatorEntity[RemoteCalendarDataUpdateCoordinator], CalendarEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _event: CalendarEvent | None
    def __init__(self, coordinator: RemoteCalendarDataUpdateCoordinator, entry: RemoteCalendarConfigEntry) -> None: ...
    @property
    def event(self) -> CalendarEvent | None: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
    async def async_update(self) -> None: ...

def _get_calendar_event(event: Event) -> CalendarEvent: ...
