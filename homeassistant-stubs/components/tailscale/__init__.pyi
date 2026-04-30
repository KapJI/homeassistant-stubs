from .coordinator import TailscaleConfigEntry as TailscaleConfigEntry, TailscaleDataUpdateCoordinator as TailscaleDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TailscaleConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: TailscaleConfigEntry) -> bool: ...
