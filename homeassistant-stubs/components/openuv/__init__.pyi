from .const import CONF_FROM_WINDOW as CONF_FROM_WINDOW, CONF_TO_WINDOW as CONF_TO_WINDOW, DATA_PROTECTION_WINDOW as DATA_PROTECTION_WINDOW, DATA_UV as DATA_UV, DEFAULT_FROM_WINDOW as DEFAULT_FROM_WINDOW, DEFAULT_TO_WINDOW as DEFAULT_TO_WINDOW, LOGGER as LOGGER
from .coordinator import OpenUvConfigEntry as OpenUvConfigEntry, OpenUvCoordinator as OpenUvCoordinator, OpenUvProtectionWindowCoordinator as OpenUvProtectionWindowCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_BINARY_SENSORS as CONF_BINARY_SENSORS, CONF_ELEVATION as CONF_ELEVATION, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_SENSORS as CONF_SENSORS, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: OpenUvConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: OpenUvConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: OpenUvConfigEntry) -> bool: ...
