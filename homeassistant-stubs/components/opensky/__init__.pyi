from .const import CONF_CONTRIBUTING_USER as CONF_CONTRIBUTING_USER, PLATFORMS as PLATFORMS
from .coordinator import OpenSkyConfigEntry as OpenSkyConfigEntry, OpenSkyDataUpdateCoordinator as OpenSkyDataUpdateCoordinator
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

async def async_setup_entry(hass: HomeAssistant, entry: OpenSkyConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: OpenSkyConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: OpenSkyConfigEntry) -> None: ...
