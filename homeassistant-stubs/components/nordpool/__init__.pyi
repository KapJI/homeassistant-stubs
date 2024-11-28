from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import NordPoolDataUpdateCoordinator as NordPoolDataUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

type NordPoolConfigEntry = ConfigEntry[NordPoolDataUpdateCoordinator]
async def async_setup_entry(hass: HomeAssistant, entry: NordPoolConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: NordPoolConfigEntry) -> bool: ...
