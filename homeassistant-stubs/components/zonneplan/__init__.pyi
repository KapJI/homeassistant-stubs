from .coordinator import ZonneplanConfigEntry as ZonneplanConfigEntry, ZonneplanCoordinator as ZonneplanCoordinator
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_TOKEN as CONF_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: ZonneplanConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ZonneplanConfigEntry) -> bool: ...
