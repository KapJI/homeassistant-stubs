from .coordinator import AirOSConfigEntry as AirOSConfigEntry, AirOSDataUpdateCoordinator as AirOSDataUpdateCoordinator
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: AirOSConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AirOSConfigEntry) -> bool: ...
