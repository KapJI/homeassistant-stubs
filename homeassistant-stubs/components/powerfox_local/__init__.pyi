from .coordinator import PowerfoxLocalConfigEntry as PowerfoxLocalConfigEntry, PowerfoxLocalDataUpdateCoordinator as PowerfoxLocalDataUpdateCoordinator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: PowerfoxLocalConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: PowerfoxLocalConfigEntry) -> bool: ...
