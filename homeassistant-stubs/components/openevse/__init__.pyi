from .coordinator import OpenEVSEConfigEntry as OpenEVSEConfigEntry, OpenEVSEDataUpdateCoordinator as OpenEVSEDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: OpenEVSEConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: OpenEVSEConfigEntry) -> bool: ...
