from .coordinator import IndiAllSkyConfigEntry as IndiAllSkyConfigEntry, IndiAllSkyDataUpdateCoordinator as IndiAllSkyDataUpdateCoordinator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

_PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: IndiAllSkyConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: IndiAllSkyConfigEntry) -> bool: ...
