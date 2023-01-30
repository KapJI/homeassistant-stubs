from .const import DOMAIN as DOMAIN, WASTE_TYPE_TO_DESCRIPTION as WASTE_TYPE_TO_DESCRIPTION
from .entity import TwenteMilieuEntity as TwenteMilieuEntity
from _typeshed import Incomplete
from datetime import date, datetime
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from twentemilieu import WasteType as WasteType

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TwenteMilieuCalendar(TwenteMilieuEntity, CalendarEntity):
    _attr_has_entity_name: bool
    _attr_icon: str
    _attr_unique_id: Incomplete
    _event: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[dict[WasteType, list[date]]], entry: ConfigEntry) -> None: ...
    @property
    def event(self) -> Union[CalendarEvent, None]: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
