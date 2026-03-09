from .coordinator import ZinvoltConfigEntry as ZinvoltConfigEntry, ZinvoltDeviceCoordinator as ZinvoltDeviceCoordinator
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: ZinvoltConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ZinvoltConfigEntry) -> bool: ...
