from .coordinator import RedgtechConfigEntry as RedgtechConfigEntry, RedgtechDataUpdateCoordinator as RedgtechDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

_LOGGER: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: RedgtechConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: RedgtechConfigEntry) -> bool: ...
