from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioaseko import Unit as Unit, Variable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete
PLATFORMS: list[str]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class AsekoDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Variable]]):
    _unit: Incomplete
    def __init__(self, hass: HomeAssistant, unit: Unit) -> None: ...
    async def _async_update_data(self) -> dict[str, Variable]: ...
