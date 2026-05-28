from .coordinator import CentriConnectConfigEntry as CentriConnectConfigEntry, CentriConnectCoordinator as CentriConnectCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

_LOGGER: Incomplete
PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: CentriConnectConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: CentriConnectConfigEntry) -> bool: ...
