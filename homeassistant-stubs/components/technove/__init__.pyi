from .coordinator import TechnoVEConfigEntry as TechnoVEConfigEntry, TechnoVEDataUpdateCoordinator as TechnoVEDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TechnoVEConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: TechnoVEConfigEntry) -> bool: ...
