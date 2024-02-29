from .const import DOMAIN as DOMAIN
from .entity import LaMarzoccoBaseEntity as LaMarzoccoBaseEntity
from collections.abc import Iterator
from datetime import datetime
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

CALENDAR_KEY: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMarzoccoCalendarEntity(LaMarzoccoBaseEntity, CalendarEntity):
    _attr_translation_key = CALENDAR_KEY
    @property
    def event(self) -> CalendarEvent | None: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
    def _get_events(self, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
    def _get_date_range(self, start_date: datetime, end_date: datetime) -> Iterator[datetime]: ...
    def _async_get_calendar_event(self, date: datetime) -> CalendarEvent | None: ...
