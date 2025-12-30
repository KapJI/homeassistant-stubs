from .const import DOMAIN as DOMAIN
from .coordinator import CookidooConfigEntry as CookidooConfigEntry, CookidooDataUpdateCoordinator as CookidooDataUpdateCoordinator
from .entity import CookidooBaseEntity as CookidooBaseEntity
from _typeshed import Incomplete
from cookidoo_api.types import CookidooCalendarDayRecipe as CookidooCalendarDayRecipe
from datetime import date, datetime
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: CookidooConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def recipe_to_event(day_date: date, recipe: CookidooCalendarDayRecipe) -> CalendarEvent: ...

class CookidooCalendarEntity(CookidooBaseEntity, CalendarEntity):
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: CookidooDataUpdateCoordinator) -> None: ...
    @property
    def event(self) -> CalendarEvent | None: ...
    async def _fetch_week_plan(self, week_day: date) -> list: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
