from .const import CONF_FOLDER_ID as CONF_FOLDER_ID, CONF_FOLDER_NAME as CONF_FOLDER_NAME, DATA_BACKUP_AGENT_LISTENERS as DATA_BACKUP_AGENT_LISTENERS, DOMAIN as DOMAIN
from .coordinator import OneDriveConfigEntry as OneDriveConfigEntry, OneDriveRuntimeData as OneDriveRuntimeData, OneDriveUpdateCoordinator as OneDriveUpdateCoordinator
from .services import async_register_services as async_register_services
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from homeassistant.helpers.typing import ConfigType as ConfigType
from onedrive_personal_sdk import OneDriveClient
from onedrive_personal_sdk.models.items import Item as Item

CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete
_LOGGER: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: OneDriveConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: OneDriveConfigEntry) -> bool: ...
async def _migrate_backup_files(client: OneDriveClient, backup_folder_id: str) -> None: ...
async def async_migrate_entry(hass: HomeAssistant, entry: OneDriveConfigEntry) -> bool: ...
async def _get_onedrive_client(hass: HomeAssistant, entry: OneDriveConfigEntry) -> tuple[OneDriveClient, Callable[[], Awaitable[str]]]: ...
async def _handle_item_operation(func: Callable[[], Awaitable[Item]], folder: str) -> Item: ...
