from .const import DOMAIN as DOMAIN
from .coordinator import WattwaechterConfigEntry as WattwaechterConfigEntry, WattwaechterCoordinator as WattwaechterCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_TOKEN as CONF_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: WattwaechterConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: WattwaechterConfigEntry) -> bool: ...
