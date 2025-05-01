from .coordinator import LaMarzoccoConfigEntry as LaMarzoccoConfigEntry, LaMarzoccoUpdateCoordinator as LaMarzoccoUpdateCoordinator
from .entity import LaMarzoccoBaseEntity as LaMarzoccoBaseEntity
from _typeshed import Incomplete
from collections.abc import Iterator
from datetime import datetime
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int
CALENDAR_KEY: str
WEEKDAY_TO_ENUM: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LaMarzoccoCalendarEntity(LaMarzoccoBaseEntity, CalendarEntity):
    _attr_translation_key = CALENDAR_KEY
    _identifier: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, coordinator: LaMarzoccoUpdateCoordinator, key: str, identifier: str) -> None: ...
    @property
    def event(self) -> CalendarEvent | None: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
    def _get_events(self, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
    def _get_date_range(self, start_date: datetime, end_date: datetime) -> Iterator[datetime]: ...
    def _async_get_calendar_event(self, date: datetime) -> CalendarEvent | None: ...
