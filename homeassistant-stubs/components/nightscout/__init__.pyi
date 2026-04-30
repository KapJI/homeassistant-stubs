from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity import SLOW_UPDATE_WARNING as SLOW_UPDATE_WARNING
from py_nightscout import Api as NightscoutAPI

PLATFORMS: Incomplete
_API_TIMEOUT: Incomplete
type NightscoutConfigEntry = ConfigEntry[NightscoutAPI]

async def async_setup_entry(hass: HomeAssistant, entry: NightscoutConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: NightscoutConfigEntry) -> bool: ...
