from .const import CONF_API_SECRET as CONF_API_SECRET, CONF_TRACKER_INTERFACES as CONF_TRACKER_INTERFACES, DOMAIN as DOMAIN
from .types import OPNsenseConfigEntry as OPNsenseConfigEntry, OPNsenseRuntimeData as OPNsenseRuntimeData
from _typeshed import Incomplete
from homeassistant.config_entries import SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def _async_setup(hass: HomeAssistant, config: ConfigType) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: OPNsenseConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: OPNsenseConfigEntry) -> bool: ...
