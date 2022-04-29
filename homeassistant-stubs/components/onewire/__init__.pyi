from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .onewirehub import CannotConnect as CannotConnect, OneWireHub as OneWireHub
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def options_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
