from .const import CONF_BAUDRATE as CONF_BAUDRATE, DOMAIN as DOMAIN, RUSSOUND_RIO_EXCEPTIONS as RUSSOUND_RIO_EXCEPTIONS, TYPE_TCP as TYPE_TCP
from _typeshed import Incomplete
from aiorussound.connection import RussoundConnectionHandler as RussoundConnectionHandler
from aiorussound.rio import RussoundRIOClient
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC

PLATFORMS: Incomplete
_LOGGER: Incomplete
type RussoundConfigEntry = ConfigEntry[RussoundRIOClient]

async def async_setup_entry(hass: HomeAssistant, entry: RussoundConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: RussoundConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: RussoundConfigEntry) -> bool: ...
