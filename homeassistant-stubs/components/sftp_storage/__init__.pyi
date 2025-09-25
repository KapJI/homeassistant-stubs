from .client import BackupAgentClient as BackupAgentClient
from .const import CONF_BACKUP_LOCATION as CONF_BACKUP_LOCATION, CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_PRIVATE_KEY_FILE as CONF_PRIVATE_KEY_FILE, CONF_USERNAME as CONF_USERNAME, DATA_BACKUP_AGENT_LISTENERS as DATA_BACKUP_AGENT_LISTENERS, DOMAIN as DOMAIN, LOGGER as LOGGER
from dataclasses import dataclass, field
from homeassistant.components.backup import BackupAgentError as BackupAgentError
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError

type SFTPConfigEntry = ConfigEntry[SFTPConfigEntryData]
@dataclass(kw_only=True)
class SFTPConfigEntryData:
    host: str
    port: int
    username: str
    password: str | None = field(repr=False)
    private_key_file: str | None
    backup_location: str

async def async_setup_entry(hass: HomeAssistant, entry: SFTPConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: SFTPConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: SFTPConfigEntry) -> bool: ...
