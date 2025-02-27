from .coordinator import FlexitConfigEntry as FlexitConfigEntry, FlexitCoordinator as FlexitCoordinator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: FlexitConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: FlexitConfigEntry) -> bool: ...
