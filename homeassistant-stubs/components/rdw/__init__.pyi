from .coordinator import RDWConfigEntry as RDWConfigEntry, RDWDataUpdateCoordinator as RDWDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: RDWConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: RDWConfigEntry) -> bool: ...
