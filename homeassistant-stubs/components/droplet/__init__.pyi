from .coordinator import DropletConfigEntry as DropletConfigEntry, DropletDataCoordinator as DropletDataCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]
logger: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: DropletConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: DropletConfigEntry) -> bool: ...
