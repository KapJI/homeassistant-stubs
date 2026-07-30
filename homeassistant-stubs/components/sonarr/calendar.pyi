from .coordinator import CalendarDataUpdateCoordinator as CalendarDataUpdateCoordinator, SonarrConfigEntry as SonarrConfigEntry
from .entity import SonarrEntity as SonarrEntity
from _typeshed import Incomplete
from aiopyarr import SonarrCalendar
from datetime import datetime
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEntityDescription as CalendarEntityDescription, CalendarEvent as CalendarEvent
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

CALENDAR_TYPE: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SonarrConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def _get_calendar_event(episode: SonarrCalendar) -> CalendarEvent: ...

class SonarrCalendarEntity(SonarrEntity[list[SonarrCalendar]], CalendarEntity):
    coordinator: CalendarDataUpdateCoordinator
    @property
    @override
    def event(self) -> CalendarEvent | None: ...
    @override
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
