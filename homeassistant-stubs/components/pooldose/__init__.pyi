from .coordinator import PooldoseConfigEntry as PooldoseConfigEntry, PooldoseCoordinator as PooldoseCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

_LOGGER: Incomplete
PLATFORMS: list[Platform]

async def async_migrate_entry(hass: HomeAssistant, entry: PooldoseConfigEntry) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: PooldoseConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: PooldoseConfigEntry) -> bool: ...
