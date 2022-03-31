from .const import DOMAIN as DOMAIN, WASTE_TYPE_TO_DESCRIPTION as WASTE_TYPE_TO_DESCRIPTION
from .entity import TwenteMilieuEntity as TwenteMilieuEntity
from datetime import datetime
from homeassistant.components.calendar import CalendarEventDevice as CalendarEventDevice
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TwenteMilieuCalendar(TwenteMilieuEntity, CalendarEventDevice):
    _attr_name: str
    _attr_icon: str
    _attr_unique_id: Any
    _event: Any
    def __init__(self, coordinator: DataUpdateCoordinator, entry: ConfigEntry) -> None: ...
    @property
    def event(self) -> Union[dict[str, Any], None]: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[dict[str, Any]]: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
