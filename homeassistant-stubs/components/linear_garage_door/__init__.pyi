from .const import DOMAIN as DOMAIN
from .coordinator import LinearConfigEntry as LinearConfigEntry, LinearUpdateCoordinator as LinearUpdateCoordinator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: LinearConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LinearConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: LinearConfigEntry) -> None: ...
