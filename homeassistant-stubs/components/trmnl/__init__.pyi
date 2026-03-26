from .coordinator import TRMNLConfigEntry as TRMNLConfigEntry, TRMNLCoordinator as TRMNLCoordinator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: TRMNLConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: TRMNLConfigEntry) -> bool: ...
