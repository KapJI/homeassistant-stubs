from .application_credentials import tenant_id_context as tenant_id_context
from .const import CONF_FOLDER_ID as CONF_FOLDER_ID, CONF_FOLDER_PATH as CONF_FOLDER_PATH, CONF_TENANT_ID as CONF_TENANT_ID, DATA_BACKUP_AGENT_LISTENERS as DATA_BACKUP_AGENT_LISTENERS, DOMAIN as DOMAIN
from .coordinator import OneDriveConfigEntry as OneDriveConfigEntry, OneDriveForBusinessUpdateCoordinator as OneDriveForBusinessUpdateCoordinator, OneDriveRuntimeData as OneDriveRuntimeData
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import ImplementationUnavailableError as ImplementationUnavailableError, OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from onedrive_personal_sdk import OneDriveClient

PLATFORMS: Incomplete
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: OneDriveConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: OneDriveConfigEntry) -> bool: ...
async def _get_onedrive_client(hass: HomeAssistant, entry: OneDriveConfigEntry) -> tuple[OneDriveClient, Callable[[], Awaitable[str]]]: ...
async def _handle_item_operation[T](func: Callable[[], Awaitable[T]], folder: str) -> T: ...
