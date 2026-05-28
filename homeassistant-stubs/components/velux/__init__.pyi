from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, PLATFORMS as PLATFORMS, PYVLX_FROM_CONFIG_FLOW as PYVLX_FROM_CONFIG_FLOW
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_PASSWORD as CONF_PASSWORD, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from pyvlx import PyVLX

type VeluxConfigEntry = ConfigEntry[PyVLX]
CONFIG_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: VeluxConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: VeluxConfigEntry) -> bool: ...
