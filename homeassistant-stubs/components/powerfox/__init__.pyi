from .coordinator import PowerfoxConfigEntry as PowerfoxConfigEntry, PowerfoxDataUpdateCoordinator as PowerfoxDataUpdateCoordinator
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: PowerfoxConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: PowerfoxConfigEntry) -> bool: ...
