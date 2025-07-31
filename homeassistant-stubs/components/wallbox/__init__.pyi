from .const import UPDATE_INTERVAL as UPDATE_INTERVAL
from .coordinator import InvalidAuth as InvalidAuth, WallboxConfigEntry as WallboxConfigEntry, WallboxCoordinator as WallboxCoordinator, async_validate_input as async_validate_input
from _typeshed import Incomplete
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: WallboxConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: WallboxConfigEntry) -> bool: ...
