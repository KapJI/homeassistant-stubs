from .api import AsyncConfigEntryAuth as AsyncConfigEntryAuth, DriveClient as DriveClient
from .const import DOMAIN as DOMAIN
from .coordinator import GoogleDriveConfigEntry as GoogleDriveConfigEntry, GoogleDriveDataUpdateCoordinator as GoogleDriveDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import instance_id as instance_id
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from homeassistant.util.hass_dict import HassKey as HassKey

DATA_BACKUP_AGENT_LISTENERS: HassKey[list[Callable[[], None]]]
_PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: GoogleDriveConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: GoogleDriveConfigEntry) -> bool: ...
