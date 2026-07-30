from .coordinator import GatusConfigEntry as GatusConfigEntry, GatusDataUpdateCoordinator as GatusDataUpdateCoordinator
from homeassistant.const import CONF_URL as CONF_URL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

_PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: GatusConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: GatusConfigEntry) -> bool: ...
