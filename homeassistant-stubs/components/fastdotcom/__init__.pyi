from .const import PLATFORMS as PLATFORMS
from .coordinator import FastdotcomConfigEntry as FastdotcomConfigEntry, FastdotcomDataUpdateCoordinator as FastdotcomDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.start import async_at_started as async_at_started

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: FastdotcomConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: FastdotcomConfigEntry) -> bool: ...
