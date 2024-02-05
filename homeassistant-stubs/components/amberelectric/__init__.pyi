from .const import CONF_SITE_ID as CONF_SITE_ID, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import AmberUpdateCoordinator as AmberUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_TOKEN as CONF_API_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
