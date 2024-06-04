from .api import AsyncConfigEntryAuth as AsyncConfigEntryAuth
from .const import DOMAIN as DOMAIN
from .coordinator import AladdinConnectCoordinator as AladdinConnectCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation

PLATFORMS: list[Platform]
AladdinConnectConfigEntry = ConfigEntry[AladdinConnectCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: AladdinConnectConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AladdinConnectConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: AladdinConnectConfigEntry) -> bool: ...
def async_remove_stale_devices(hass: HomeAssistant, config_entry: AladdinConnectConfigEntry) -> None: ...
