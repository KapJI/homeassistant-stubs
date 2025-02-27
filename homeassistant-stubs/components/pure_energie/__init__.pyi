from .coordinator import PureEnergieConfigEntry as PureEnergieConfigEntry, PureEnergieDataUpdateCoordinator as PureEnergieDataUpdateCoordinator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: PureEnergieConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: PureEnergieConfigEntry) -> bool: ...
