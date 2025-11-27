from .const import DOMAIN as DOMAIN
from .coordinator import XboxConfigEntry as XboxConfigEntry, XboxConsolesCoordinator as XboxConsolesCoordinator, XboxCoordinators as XboxCoordinators, XboxUpdateCoordinator as XboxUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: XboxConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: XboxConfigEntry) -> bool: ...
async def async_migrate_unique_id(hass: HomeAssistant, entry: XboxConfigEntry) -> bool: ...
