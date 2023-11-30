from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
