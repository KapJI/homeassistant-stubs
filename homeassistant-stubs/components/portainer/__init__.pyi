from .coordinator import PortainerCoordinator as PortainerCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_API_TOKEN as CONF_API_TOKEN, CONF_HOST as CONF_HOST, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession

_PLATFORMS: list[Platform]
type PortainerConfigEntry = ConfigEntry[PortainerCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: PortainerConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: PortainerConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: PortainerConfigEntry) -> bool: ...
