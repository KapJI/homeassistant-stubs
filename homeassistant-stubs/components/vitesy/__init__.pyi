from .coordinator import VitesyConfigEntry as VitesyConfigEntry, VitesyDataUpdateCoordinator as VitesyDataUpdateCoordinator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: VitesyConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: VitesyConfigEntry) -> bool: ...
