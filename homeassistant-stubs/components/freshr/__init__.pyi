from .coordinator import FreshrConfigEntry as FreshrConfigEntry, FreshrData as FreshrData, FreshrDevicesCoordinator as FreshrDevicesCoordinator, FreshrReadingsCoordinator as FreshrReadingsCoordinator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

_PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: FreshrConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: FreshrConfigEntry) -> bool: ...
