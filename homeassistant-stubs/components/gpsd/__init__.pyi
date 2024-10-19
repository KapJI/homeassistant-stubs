from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: GPSDConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: GPSDConfigEntry) -> bool: ...
