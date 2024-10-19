from .const import CONF_HOUSE_LETTER as CONF_HOUSE_LETTER, CONF_HOUSE_NUMBER as CONF_HOUSE_NUMBER, CONF_POST_CODE as CONF_POST_CODE, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ID as CONF_ID, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

SCAN_INTERVAL: Incomplete
SERVICE_UPDATE: str
SERVICE_SCHEMA: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
