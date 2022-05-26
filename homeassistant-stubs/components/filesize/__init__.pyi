import pathlib
from .const import PLATFORMS as PLATFORMS
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_FILE_PATH as CONF_FILE_PATH
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady

def check_path(path: pathlib.Path) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
