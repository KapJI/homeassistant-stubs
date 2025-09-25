from .coordinator import BRouteConfigEntry as BRouteConfigEntry, BRouteUpdateCoordinator as BRouteUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

_LOGGER: Incomplete
PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: BRouteConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: BRouteConfigEntry) -> bool: ...
