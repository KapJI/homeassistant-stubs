from .api import OneDriveConfigEntryAccessTokenProvider as OneDriveConfigEntryAccessTokenProvider
from .const import DATA_BACKUP_AGENT_LISTENERS as DATA_BACKUP_AGENT_LISTENERS, DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from onedrive_personal_sdk import OneDriveClient

@dataclass
class OneDriveRuntimeData:
    client: OneDriveClient
    token_provider: OneDriveConfigEntryAccessTokenProvider
    backup_folder_id: str
type OneDriveConfigEntry = ConfigEntry[OneDriveRuntimeData]

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: OneDriveConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: OneDriveConfigEntry) -> bool: ...
def _async_notify_backup_listeners(hass: HomeAssistant) -> None: ...
@callback
def _async_notify_backup_listeners_soon(hass: HomeAssistant) -> None: ...
