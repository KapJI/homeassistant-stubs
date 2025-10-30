from .const import DOMAIN as DOMAIN, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from airos.airos8 import AirOS8 as AirOS8, AirOS8Data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
type AirOSConfigEntry = ConfigEntry[AirOSDataUpdateCoordinator]

class AirOSDataUpdateCoordinator(DataUpdateCoordinator[AirOS8Data]):
    config_entry: AirOSConfigEntry
    airos_device: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: AirOSConfigEntry, airos_device: AirOS8) -> None: ...
    async def _async_update_data(self) -> AirOS8Data: ...
