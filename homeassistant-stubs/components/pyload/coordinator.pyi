from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyloadapi import PyLoadAPI as PyLoadAPI

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete

@dataclass(kw_only=True)
class PyLoadData:
    pause: bool
    active: int
    queue: int
    total: int
    speed: float
    download: bool
    reconnect: bool
    captcha: bool | None = ...
    proxy: bool | None = ...
    free_space: int
type PyLoadConfigEntry = ConfigEntry[PyLoadCoordinator]

class PyLoadCoordinator(DataUpdateCoordinator[PyLoadData]):
    config_entry: PyLoadConfigEntry
    pyload: Incomplete
    version: str | None
    def __init__(self, hass: HomeAssistant, config_entry: PyLoadConfigEntry, pyload: PyLoadAPI) -> None: ...
    async def _async_update_data(self) -> PyLoadData: ...
    async def _async_setup(self) -> None: ...
