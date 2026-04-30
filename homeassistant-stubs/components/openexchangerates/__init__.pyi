from .const import BASE_UPDATE_INTERVAL as BASE_UPDATE_INTERVAL, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import OpenexchangeratesConfigEntry as OpenexchangeratesConfigEntry, OpenexchangeratesCoordinator as OpenexchangeratesCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_BASE as CONF_BASE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: OpenexchangeratesConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: OpenexchangeratesConfigEntry) -> bool: ...
