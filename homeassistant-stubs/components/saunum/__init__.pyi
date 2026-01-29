from .coordinator import LeilSaunaCoordinator as LeilSaunaCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

PLATFORMS: list[Platform]
type LeilSaunaConfigEntry = ConfigEntry[LeilSaunaCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: LeilSaunaConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LeilSaunaConfigEntry) -> bool: ...
