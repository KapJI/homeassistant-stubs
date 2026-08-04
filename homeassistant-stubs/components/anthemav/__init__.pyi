import anthemav
from .const import ANTHEMAV_UPDATE_SIGNAL as ANTHEMAV_UPDATE_SIGNAL, DEVICE_TIMEOUT_SECONDS as DEVICE_TIMEOUT_SECONDS, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_MODEL as CONF_MODEL, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send

type AnthemavConfigEntry = ConfigEntry[anthemav.Connection]
PLATFORMS: Incomplete
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AnthemavConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AnthemavConfigEntry) -> bool: ...
