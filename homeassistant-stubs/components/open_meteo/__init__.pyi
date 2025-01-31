from .coordinator import OpenMeteoConfigEntry as OpenMeteoConfigEntry, OpenMeteoDataUpdateCoordinator as OpenMeteoDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: OpenMeteoConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: OpenMeteoConfigEntry) -> bool: ...
