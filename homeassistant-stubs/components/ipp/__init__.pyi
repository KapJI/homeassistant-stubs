from .coordinator import IPPConfigEntry as IPPConfigEntry, IPPDataUpdateCoordinator as IPPDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: IPPConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: IPPConfigEntry) -> bool: ...
