from .coordinator import LaundrifyConfigEntry as LaundrifyConfigEntry, LaundrifyUpdateCoordinator as LaundrifyUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_LOGGER: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LaundrifyConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LaundrifyConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: LaundrifyConfigEntry) -> bool: ...
