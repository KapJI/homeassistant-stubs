from .const import CONF_INFO as CONF_INFO, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS, UPDATE_RATE as UPDATE_RATE
from .discovery import async_start_discovery as async_start_discovery
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
