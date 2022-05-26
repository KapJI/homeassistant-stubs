from . import api as api
from .const import NEATO_CONFIG as NEATO_CONFIG, NEATO_DOMAIN as NEATO_DOMAIN, NEATO_LOGIN as NEATO_LOGIN
from .hub import NeatoHub as NeatoHub
from _typeshed import Incomplete
from homeassistant.components.application_credentials import ClientCredential as ClientCredential, async_import_client_credential as async_import_client_credential
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_TOKEN as CONF_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
