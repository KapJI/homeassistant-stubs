from .const import DOMAIN as DOMAIN
from .coordinator import LibrenmsCentralDataUpdateCoordinator as LibrenmsCentralDataUpdateCoordinator, LibrenmsConfigEntry as LibrenmsConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: LibrenmsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LibrenmsConfigEntry) -> bool: ...
