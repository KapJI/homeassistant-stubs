from .const import CONF_ENABLE_PUSH as CONF_ENABLE_PUSH, DOMAIN as DOMAIN
from .coordinator import ImapPollingDataUpdateCoordinator as ImapPollingDataUpdateCoordinator, ImapPushDataUpdateCoordinator as ImapPushDataUpdateCoordinator, connect_to_server as connect_to_server
from .errors import InvalidAuth as InvalidAuth, InvalidFolder as InvalidFolder
from aioimaplib import IMAP4_SSL as IMAP4_SSL
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
