from .const import DATA_COORDINATOR as DATA_COORDINATOR, DATA_TILE as DATA_TILE, DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry, async_migrate_entries as async_migrate_entries
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.async_ import gather_with_concurrency as gather_with_concurrency
from pytile.tile import Tile as Tile
from typing import Any

PLATFORMS: Any
DEVICE_TYPES: Any
DEFAULT_INIT_TASK_LIMIT: int
DEFAULT_UPDATE_INTERVAL: Any
CONF_SHOW_INACTIVE: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
