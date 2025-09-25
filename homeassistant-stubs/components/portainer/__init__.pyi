from .coordinator import PortainerCoordinator as PortainerCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession

_PLATFORMS: list[Platform]
type PortainerConfigEntry = ConfigEntry[PortainerCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: PortainerConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: PortainerConfigEntry) -> bool: ...
