from .const import DEFAULT_ACCESS as DEFAULT_ACCESS, DOMAIN as DOMAIN
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete
type GoogleSheetsConfigEntry = ConfigEntry[OAuth2Session]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: GoogleSheetsConfigEntry) -> bool: ...
def async_entry_has_scopes(hass: HomeAssistant, entry: GoogleSheetsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: GoogleSheetsConfigEntry) -> bool: ...
