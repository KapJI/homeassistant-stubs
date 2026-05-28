from .const import DOMAIN as DOMAIN
from .coordinator import PajGpsConfigEntry as PajGpsConfigEntry, PajGpsCoordinator as PajGpsCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]
CONFIG_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PajGpsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: PajGpsConfigEntry) -> bool: ...
