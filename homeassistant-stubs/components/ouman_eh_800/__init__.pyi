from .coordinator import OumanEh800ConfigEntry as OumanEh800ConfigEntry, OumanEh800Coordinator as OumanEh800Coordinator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

_PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: OumanEh800ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: OumanEh800ConfigEntry) -> bool: ...
