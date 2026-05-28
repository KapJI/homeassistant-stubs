from .coordinator import GuntamaticConfigEntry as GuntamaticConfigEntry, GuntamaticCoordinator as GuntamaticCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

_LOGGER: Incomplete
_PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: GuntamaticConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: GuntamaticConfigEntry) -> bool: ...
