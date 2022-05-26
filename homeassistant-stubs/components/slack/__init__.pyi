from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_PLATFORM as CONF_PLATFORM, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client, discovery as discovery
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
PLATFORMS: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
