from .coordinator import TileConfigEntry as TileConfigEntry, TileCoordinator as TileCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.util.async_ import gather_with_limited_concurrency as gather_with_limited_concurrency

PLATFORMS: Incomplete
DEVICE_TYPES: Incomplete
DEFAULT_INIT_TASK_LIMIT: int
CONF_SHOW_INACTIVE: str

async def async_setup_entry(hass: HomeAssistant, entry: TileConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: TileConfigEntry) -> bool: ...
