from .coordinator import AirGradientConfigEntry as AirGradientConfigEntry, AirGradientCoordinator as AirGradientCoordinator
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: AirGradientConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AirGradientConfigEntry) -> bool: ...
