from .coordinator import StarlinkConfigEntry as StarlinkConfigEntry, StarlinkUpdateCoordinator as StarlinkUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: StarlinkConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: StarlinkConfigEntry) -> bool: ...
