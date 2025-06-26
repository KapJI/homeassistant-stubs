from .const import CONF_HOST as CONF_HOST
from _typeshed import Incomplete
from altruistclient import AltruistClient
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
UPDATE_INTERVAL: Incomplete
type AltruistConfigEntry = ConfigEntry[AltruistDataUpdateCoordinator]

class AltruistDataUpdateCoordinator(DataUpdateCoordinator[dict[str, str]]):
    client: AltruistClient
    _ip_address: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: AltruistConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> dict[str, str]: ...
