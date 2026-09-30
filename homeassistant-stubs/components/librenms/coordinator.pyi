from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiolibrenms import Librenms as Librenms
from aiolibrenms.devices.models import LibrenmsDeviceInfo as LibrenmsDeviceInfo
from aiolibrenms.system.models import LibrenmsSystemInfo as LibrenmsSystemInfo
from dataclasses import dataclass
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

_LOGGER: Incomplete

@dataclass
class LibrenmsCentralData:
    system: LibrenmsSystemInfo
    devices: dict[int, LibrenmsDeviceInfo]
type LibrenmsConfigEntry = ConfigEntry[LibrenmsCentralDataUpdateCoordinator]

class LibrenmsBaseDataUpdateCoordinator[T](DataUpdateCoordinator[T]):
    config_entry: LibrenmsConfigEntry
    api: Incomplete
    configuration_url: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: LibrenmsConfigEntry, api: Librenms, update_interval: timedelta) -> None: ...

class LibrenmsCentralDataUpdateCoordinator(LibrenmsBaseDataUpdateCoordinator[LibrenmsCentralData]):
    def __init__(self, hass: HomeAssistant, config_entry: LibrenmsConfigEntry, api: Librenms) -> None: ...
    @override
    async def _async_update_data(self) -> LibrenmsCentralData: ...
