from .coordinator import Enigma2ConfigEntry as Enigma2ConfigEntry, Enigma2UpdateCoordinator as Enigma2UpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: Enigma2ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: Enigma2ConfigEntry) -> bool: ...
