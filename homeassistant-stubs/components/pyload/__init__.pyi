from .coordinator import PyLoadConfigEntry as PyLoadConfigEntry, PyLoadCoordinator as PyLoadCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession

_LOGGER: Incomplete
PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: PyLoadConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: PyLoadConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: PyLoadConfigEntry) -> bool: ...
