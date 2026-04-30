from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from fumis import FumisInfo
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_MAC as CONF_MAC, CONF_PIN as CONF_PIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

type FumisConfigEntry = ConfigEntry[FumisDataUpdateCoordinator]
class FumisDataUpdateCoordinator(DataUpdateCoordinator[FumisInfo]):
    config_entry: FumisConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, entry: FumisConfigEntry) -> None: ...
    async def _async_update_data(self) -> FumisInfo: ...
