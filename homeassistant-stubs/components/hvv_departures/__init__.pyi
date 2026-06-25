from .hub import GTIHub as GTIHub, HVVConfigEntry as HVVConfigEntry
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: HVVConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: HVVConfigEntry) -> bool: ...
