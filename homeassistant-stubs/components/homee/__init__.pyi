from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from pyHomee import Homee

_LOGGER: Incomplete
PLATFORMS: Incomplete
type HomeeConfigEntry = ConfigEntry[Homee]

async def async_setup_entry(hass: HomeAssistant, entry: HomeeConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: HomeeConfigEntry) -> bool: ...
