from .api import OneDriveConfigEntryAccessTokenProvider as OneDriveConfigEntryAccessTokenProvider
from .const import DATA_BACKUP_AGENT_LISTENERS as DATA_BACKUP_AGENT_LISTENERS, DOMAIN as DOMAIN, OAUTH_SCOPES as OAUTH_SCOPES
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from homeassistant.helpers.httpx_client import create_async_httpx_client as create_async_httpx_client
from msgraph.generated.drives.item.items.items_request_builder import ItemsRequestBuilder as ItemsRequestBuilder

@dataclass
class OneDriveRuntimeData:
    items: ItemsRequestBuilder
    backup_folder_id: str
type OneDriveConfigEntry = ConfigEntry[OneDriveRuntimeData]

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: OneDriveConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: OneDriveConfigEntry) -> bool: ...
def _async_notify_backup_listeners(hass: HomeAssistant) -> None: ...
@callback
def _async_notify_backup_listeners_soon(hass: HomeAssistant) -> None: ...
async def _async_create_folder_if_not_exists(items: ItemsRequestBuilder, base_folder_id: str, folder: str) -> str: ...
