from .coordinator import AirobotConfigEntry as AirobotConfigEntry, AirobotDataUpdateCoordinator as AirobotDataUpdateCoordinator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: AirobotConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AirobotConfigEntry) -> bool: ...
