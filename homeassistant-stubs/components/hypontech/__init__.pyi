from .coordinator import HypontechConfigEntry as HypontechConfigEntry, HypontechDataCoordinator as HypontechDataCoordinator
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: HypontechConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: HypontechConfigEntry) -> bool: ...
