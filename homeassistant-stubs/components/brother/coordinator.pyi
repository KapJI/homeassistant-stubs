from .const import DOMAIN as DOMAIN, UPDATE_INTERVAL as UPDATE_INTERVAL
from _typeshed import Incomplete
from brother import Brother as Brother, BrotherSensors
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
type BrotherConfigEntry = ConfigEntry[BrotherDataUpdateCoordinator]

class BrotherDataUpdateCoordinator(DataUpdateCoordinator[BrotherSensors]):
    config_entry: BrotherConfigEntry
    brother: Incomplete
    device_name: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: BrotherConfigEntry, brother: Brother) -> None: ...
    async def _async_update_data(self) -> BrotherSensors: ...
