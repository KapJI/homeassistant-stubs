import logging
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

_LOGGER: logging.Logger
PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: DeakoConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: DeakoConfigEntry) -> bool: ...
