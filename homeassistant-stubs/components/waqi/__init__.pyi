from .coordinator import WAQIConfigEntry as WAQIConfigEntry, WAQIDataUpdateCoordinator as WAQIDataUpdateCoordinator
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: WAQIConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: WAQIConfigEntry) -> bool: ...
