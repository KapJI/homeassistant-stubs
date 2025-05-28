from .api import AsyncConfigEntryAuth as AsyncConfigEntryAuth
from .const import DOMAIN as DOMAIN
from .coordinator import MieleConfigEntry as MieleConfigEntry, MieleDataUpdateCoordinator as MieleDataUpdateCoordinator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: MieleConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: MieleConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: MieleConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
