from .const import DEFAULT_URL as DEFAULT_URL
from .coordinator import PTDevicesConfigEntry as PTDevicesConfigEntry, PTDevicesCoordinator as PTDevicesCoordinator
from homeassistant.const import CONF_API_TOKEN as CONF_API_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, config_entry: PTDevicesConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: PTDevicesConfigEntry) -> bool: ...
