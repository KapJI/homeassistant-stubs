from .const import LOGGER as LOGGER
from homeassistant import config_entries as config_entries
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

PLATFORMS: Any

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry) -> bool: ...