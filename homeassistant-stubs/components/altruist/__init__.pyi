from .coordinator import AltruistConfigEntry as AltruistConfigEntry, AltruistDataUpdateCoordinator as AltruistDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AltruistConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AltruistConfigEntry) -> bool: ...
