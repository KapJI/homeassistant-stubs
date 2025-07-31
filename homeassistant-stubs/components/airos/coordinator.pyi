from .const import DOMAIN as DOMAIN, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from airos.airos8 import AirOS as AirOS, AirOSData
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
type AirOSConfigEntry = ConfigEntry[AirOSDataUpdateCoordinator]

class AirOSDataUpdateCoordinator(DataUpdateCoordinator[AirOSData]):
    config_entry: AirOSConfigEntry
    airos_device: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: AirOSConfigEntry, airos_device: AirOS) -> None: ...
    async def _async_update_data(self) -> AirOSData: ...
