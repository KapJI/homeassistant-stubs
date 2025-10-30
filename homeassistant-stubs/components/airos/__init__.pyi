from .const import DEFAULT_SSL as DEFAULT_SSL, DEFAULT_VERIFY_SSL as DEFAULT_VERIFY_SSL, DOMAIN as DOMAIN, SECTION_ADVANCED_SETTINGS as SECTION_ADVANCED_SETTINGS
from .coordinator import AirOSConfigEntry as AirOSConfigEntry, AirOSDataUpdateCoordinator as AirOSDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_SSL as CONF_SSL, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_PLATFORMS: list[Platform]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AirOSConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: AirOSConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AirOSConfigEntry) -> bool: ...
