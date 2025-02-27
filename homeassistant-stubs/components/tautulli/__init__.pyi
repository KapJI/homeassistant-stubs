from .coordinator import TautulliConfigEntry as TautulliConfigEntry, TautulliDataUpdateCoordinator as TautulliDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TautulliConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: TautulliConfigEntry) -> bool: ...
