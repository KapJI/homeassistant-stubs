from .auth import DropboxConfigEntryAuth as DropboxConfigEntryAuth
from .const import DATA_BACKUP_AGENT_LISTENERS as DATA_BACKUP_AGENT_LISTENERS, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.config_entry_oauth2_flow import ImplementationUnavailableError as ImplementationUnavailableError, OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from python_dropbox_api import DropboxAPIClient

type DropboxConfigEntry = ConfigEntry[DropboxAPIClient]
async def async_setup_entry(hass: HomeAssistant, entry: DropboxConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: DropboxConfigEntry) -> bool: ...
