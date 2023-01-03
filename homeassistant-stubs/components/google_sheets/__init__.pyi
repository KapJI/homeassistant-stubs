from .const import DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DEFAULT_ACCESS as DEFAULT_ACCESS, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from homeassistant.helpers.selector import ConfigEntrySelector as ConfigEntrySelector

DATA: str
WORKSHEET: str
SERVICE_APPEND_SHEET: str
SHEET_SERVICE_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def async_entry_has_scopes(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_setup_service(hass: HomeAssistant) -> None: ...
