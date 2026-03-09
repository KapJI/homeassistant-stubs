from .const import CONF_ADMIN_API_KEY as CONF_ADMIN_API_KEY, CONF_API_URL as CONF_API_URL
from .coordinator import GhostDataUpdateCoordinator as GhostDataUpdateCoordinator
from _typeshed import Incomplete
from aioghost import GhostAdminAPI
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession

_LOGGER: Incomplete
PLATFORMS: list[Platform]
type GhostConfigEntry = ConfigEntry[GhostRuntimeData]

@dataclass
class GhostRuntimeData:
    coordinator: GhostDataUpdateCoordinator
    api: GhostAdminAPI

async def async_setup_entry(hass: HomeAssistant, entry: GhostConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: GhostConfigEntry) -> bool: ...
