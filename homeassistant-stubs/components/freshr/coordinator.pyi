from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyfreshr import FreshrClient
from pyfreshr.models import DeviceReadings, DeviceSummary

DEVICES_SCAN_INTERVAL: Incomplete
READINGS_SCAN_INTERVAL: Incomplete

@dataclass
class FreshrData:
    devices: FreshrDevicesCoordinator
    readings: dict[str, FreshrReadingsCoordinator]
type FreshrConfigEntry = ConfigEntry[FreshrData]

class FreshrDevicesCoordinator(DataUpdateCoordinator[list[DeviceSummary]]):
    config_entry: FreshrConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: FreshrConfigEntry) -> None: ...
    async def _async_update_data(self) -> list[DeviceSummary]: ...

class FreshrReadingsCoordinator(DataUpdateCoordinator[DeviceReadings]):
    config_entry: FreshrConfigEntry
    _device: Incomplete
    _client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: FreshrConfigEntry, device: DeviceSummary, client: FreshrClient) -> None: ...
    @property
    def device_id(self) -> str: ...
    async def _async_update_data(self) -> DeviceReadings: ...
