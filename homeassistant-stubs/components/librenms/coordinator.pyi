from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiolibrenms.devices.models import LibrenmsDeviceInfo as LibrenmsDeviceInfo
from aiolibrenms.system.models import LibrenmsSystemInfo as LibrenmsSystemInfo
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

_LOGGER: Incomplete

@dataclass
class LibrenmsData:
    system: LibrenmsSystemInfo
    devices: dict[int, LibrenmsDeviceInfo]
type LibrenmsConfigEntry = ConfigEntry[LibrenmsDataUpdateCoordinator]

class LibrenmsDataUpdateCoordinator(DataUpdateCoordinator[LibrenmsData]):
    config_entry: LibrenmsConfigEntry
    api: Incomplete
    configuration_url: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: LibrenmsConfigEntry) -> None: ...
    @override
    async def _async_setup(self) -> None: ...
    @override
    async def _async_update_data(self) -> LibrenmsData: ...
