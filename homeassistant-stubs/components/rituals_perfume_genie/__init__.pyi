from .const import ACCOUNT_HASH as ACCOUNT_HASH, COORDINATORS as COORDINATORS, DEVICES as DEVICES, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from pyrituals import Diffuser as Diffuser

PLATFORMS: Incomplete
_LOGGER: Incomplete
UPDATE_INTERVAL: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class RitualsDataUpdateCoordinator(DataUpdateCoordinator[None]):
    _device: Incomplete
    def __init__(self, hass: HomeAssistant, device: Diffuser) -> None: ...
    async def _async_update_data(self) -> None: ...
