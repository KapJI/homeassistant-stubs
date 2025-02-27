from .const import DOMAIN as DOMAIN, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from lacrosse_view import LaCrosse as LaCrosse, Sensor

_LOGGER: Incomplete

class LaCrosseUpdateCoordinator(DataUpdateCoordinator[list[Sensor]]):
    username: str
    password: str
    name: str
    id: str
    hass: HomeAssistant
    devices: list[Sensor] | None
    config_entry: ConfigEntry
    api: Incomplete
    last_update: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, api: LaCrosse) -> None: ...
    async def _async_update_data(self) -> list[Sensor]: ...
