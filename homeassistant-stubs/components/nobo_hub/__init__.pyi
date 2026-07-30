from .const import ATTR_HARDWARE_VERSION as ATTR_HARDWARE_VERSION, ATTR_SOFTWARE_VERSION as ATTR_SOFTWARE_VERSION, CONF_OVERRIDE_TYPE as CONF_OVERRIDE_TYPE, CONF_SERIAL as CONF_SERIAL, DOMAIN as DOMAIN, NOBO_MANUFACTURER as NOBO_MANUFACTURER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_NAME as ATTR_NAME, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_MAC as CONF_MAC, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from pynobo import nobo

_LOGGER: Incomplete
PLATFORMS: Incomplete
type NoboHubConfigEntry = ConfigEntry[nobo]

async def async_setup_entry(hass: HomeAssistant, entry: NoboHubConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: NoboHubConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: NoboHubConfigEntry) -> bool: ...
