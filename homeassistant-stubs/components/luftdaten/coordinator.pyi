from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from luftdaten import Luftdaten as Luftdaten

_LOGGER: Incomplete
type LuftdatenConfigEntry = ConfigEntry[LuftdatenDataUpdateCoordinator]

class LuftdatenDataUpdateCoordinator(DataUpdateCoordinator[dict[str, float | int]]):
    config_entry: LuftdatenConfigEntry
    _sensor_community: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: LuftdatenConfigEntry, sensor_community: Luftdaten) -> None: ...
    async def _async_update_data(self) -> dict[str, float | int]: ...
