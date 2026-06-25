from .coordinator import InComfortConfigEntry as InComfortConfigEntry, InComfortDataCoordinator as InComfortDataCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: Incomplete
INTEGRATION_TITLE: str

async def async_setup_entry(hass: HomeAssistant, entry: InComfortConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: InComfortConfigEntry) -> bool: ...
