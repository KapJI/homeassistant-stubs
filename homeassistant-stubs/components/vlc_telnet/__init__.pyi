from .const import DATA_AVAILABLE as DATA_AVAILABLE, DATA_VLC as DATA_VLC, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from aiovlc.client import Client
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def disconnect_vlc(vlc: Client) -> None: ...
