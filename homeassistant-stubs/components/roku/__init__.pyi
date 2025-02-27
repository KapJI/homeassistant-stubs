from .coordinator import RokuConfigEntry as RokuConfigEntry, RokuDataUpdateCoordinator as RokuDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: RokuConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: RokuConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, entry: RokuConfigEntry) -> None: ...
