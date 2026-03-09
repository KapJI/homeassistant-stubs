from .coordinator import HDFuryConfigEntry as HDFuryConfigEntry, HDFuryCoordinator as HDFuryCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: HDFuryConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: HDFuryConfigEntry) -> bool: ...
