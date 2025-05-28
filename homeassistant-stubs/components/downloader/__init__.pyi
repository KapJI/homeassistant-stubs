from .const import CONF_DOWNLOAD_DIR as CONF_DOWNLOAD_DIR, _LOGGER as _LOGGER
from .services import register_services as register_services
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
