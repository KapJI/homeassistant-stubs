from .const import PLATFORMS as PLATFORMS
from .coordinator import TVDataUpdateCoordinator as TVDataUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant

TVTrainConfigEntry = ConfigEntry[TVDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: TVTrainConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
