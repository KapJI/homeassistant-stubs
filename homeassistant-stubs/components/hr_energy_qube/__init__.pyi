from .const import PLATFORMS as PLATFORMS
from .coordinator import QubeCoordinator as QubeCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant

type QubeConfigEntry = ConfigEntry[QubeCoordinator]
async def async_setup_entry(hass: HomeAssistant, entry: QubeConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: QubeConfigEntry) -> bool: ...
