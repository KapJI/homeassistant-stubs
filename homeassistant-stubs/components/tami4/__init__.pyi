from .const import CONF_REFRESH_TOKEN as CONF_REFRESH_TOKEN
from .coordinator import Tami4ConfigEntry as Tami4ConfigEntry, Tami4EdgeCoordinator as Tami4EdgeCoordinator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: Tami4ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: Tami4ConfigEntry) -> bool: ...
