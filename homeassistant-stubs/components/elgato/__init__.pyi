from .coordinator import ElgatoDataUpdateCoordinator as ElgatoDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete
ElgatorConfigEntry = ConfigEntry[ElgatoDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: ElgatorConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ElgatorConfigEntry) -> bool: ...
