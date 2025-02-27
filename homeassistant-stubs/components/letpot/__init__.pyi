from .const import CONF_ACCESS_TOKEN_EXPIRES as CONF_ACCESS_TOKEN_EXPIRES, CONF_REFRESH_TOKEN as CONF_REFRESH_TOKEN, CONF_REFRESH_TOKEN_EXPIRES as CONF_REFRESH_TOKEN_EXPIRES, CONF_USER_ID as CONF_USER_ID
from .coordinator import LetPotConfigEntry as LetPotConfigEntry, LetPotDeviceCoordinator as LetPotDeviceCoordinator
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_EMAIL as CONF_EMAIL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: LetPotConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LetPotConfigEntry) -> bool: ...
