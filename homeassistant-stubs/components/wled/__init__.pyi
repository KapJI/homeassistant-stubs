from .const import LOGGER as LOGGER
from .coordinator import WLEDDataUpdateCoordinator as WLEDDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete
WLEDConfigEntry = ConfigEntry[WLEDDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: WLEDConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: WLEDConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
