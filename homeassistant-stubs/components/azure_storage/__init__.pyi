from .const import CONF_ACCOUNT_NAME as CONF_ACCOUNT_NAME, CONF_CONTAINER_NAME as CONF_CONTAINER_NAME, CONF_STORAGE_ACCOUNT_KEY as CONF_STORAGE_ACCOUNT_KEY, DATA_BACKUP_AGENT_LISTENERS as DATA_BACKUP_AGENT_LISTENERS, DOMAIN as DOMAIN
from azure.storage.blob.aio import ContainerClient
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession

type AzureStorageConfigEntry = ConfigEntry[ContainerClient]
async def async_setup_entry(hass: HomeAssistant, entry: AzureStorageConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AzureStorageConfigEntry) -> bool: ...
