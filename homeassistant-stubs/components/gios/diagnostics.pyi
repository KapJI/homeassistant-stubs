from . import GiosDataUpdateCoordinator as GiosDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry) -> dict: ...
