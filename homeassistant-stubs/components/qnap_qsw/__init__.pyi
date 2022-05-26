from .const import DOMAIN as DOMAIN
from .coordinator import QswUpdateCoordinator as QswUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
