from .const import DOMAIN as DOMAIN, RUSSOUND_RIO_EXCEPTIONS as RUSSOUND_RIO_EXCEPTIONS
from _typeshed import Incomplete
from aiorussound import RussoundClient
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC

PLATFORMS: Incomplete
_LOGGER: Incomplete
type RussoundConfigEntry = ConfigEntry[RussoundClient]

async def async_setup_entry(hass: HomeAssistant, entry: RussoundConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: RussoundConfigEntry) -> bool: ...
