from .const import CONF_SET_ID as CONF_SET_ID, LGTVRS232ConfigEntry as LGTVRS232ConfigEntry, LOGGER as LOGGER, QUERY_ATTRIBUTES as QUERY_ATTRIBUTES
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from lg_rs232_tv import TVState as TVState

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LGTVRS232ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LGTVRS232ConfigEntry) -> bool: ...
