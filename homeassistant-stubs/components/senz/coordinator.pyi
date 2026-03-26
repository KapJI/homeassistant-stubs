from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pysenz import SENZAPI as SENZAPI, Thermostat

UPDATE_INTERVAL: Incomplete
_LOGGER: Incomplete
type SENZConfigEntry = ConfigEntry[SENZDataUpdateCoordinator]

class SENZDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Thermostat]]):
    config_entry: SENZConfigEntry
    _senz_api: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: SENZConfigEntry, *, name: str, senz_api: SENZAPI) -> None: ...
    async def _async_update_data(self) -> dict[str, Thermostat]: ...
