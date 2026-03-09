from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyintelliclima import IntelliClimaAPI as IntelliClimaAPI, IntelliClimaDevices

type IntelliClimaConfigEntry = ConfigEntry[IntelliClimaCoordinator]
class IntelliClimaCoordinator(DataUpdateCoordinator[IntelliClimaDevices]):
    api: Incomplete
    def __init__(self, hass: HomeAssistant, entry: IntelliClimaConfigEntry, api: IntelliClimaAPI) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> IntelliClimaDevices: ...
