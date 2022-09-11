from .const import CONF_FORCE as CONF_FORCE, DATA_ADGUARD_CLIENT as DATA_ADGUARD_CLIENT, DOMAIN as DOMAIN, SERVICE_ADD_URL as SERVICE_ADD_URL, SERVICE_DISABLE_URL as SERVICE_DISABLE_URL, SERVICE_ENABLE_URL as SERVICE_ENABLE_URL, SERVICE_REFRESH as SERVICE_REFRESH, SERVICE_REMOVE_URL as SERVICE_REMOVE_URL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

SERVICE_URL_SCHEMA: Incomplete
SERVICE_ADD_URL_SCHEMA: Incomplete
SERVICE_REFRESH_SCHEMA: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
