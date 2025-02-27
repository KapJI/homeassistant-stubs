from .api import MinecraftServer as MinecraftServer, MinecraftServerAddressError as MinecraftServerAddressError, MinecraftServerConnectionError as MinecraftServerConnectionError, MinecraftServerData as MinecraftServerData, MinecraftServerNotInitializedError as MinecraftServerNotInitializedError, MinecraftServerType as MinecraftServerType
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

type MinecraftServerConfigEntry = ConfigEntry[MinecraftServerCoordinator]
SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete

class MinecraftServerCoordinator(DataUpdateCoordinator[MinecraftServerData]):
    config_entry: MinecraftServerConfigEntry
    _api: MinecraftServer
    def __init__(self, hass: HomeAssistant, config_entry: MinecraftServerConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> MinecraftServerData: ...
