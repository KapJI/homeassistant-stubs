from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiocentriconnect import Tank
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
COORDINATOR_NAME: Incomplete
UPDATE_INTERVAL: Incomplete
type CentriConnectConfigEntry = ConfigEntry[CentriConnectCoordinator]

@dataclass
class CentriConnectDeviceInfo:
    device_id: str
    device_name: str
    hardware_version: str
    lte_version: str
    tank_size: int
    tank_size_unit: str

class CentriConnectCoordinator(DataUpdateCoordinator[Tank]):
    config_entry: CentriConnectConfigEntry
    device_info: CentriConnectDeviceInfo
    api_client: Incomplete
    def __init__(self, hass: HomeAssistant, entry: CentriConnectConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> Tank: ...
