from .const import CONF_PLAY_MEDIA_APP_ID as CONF_PLAY_MEDIA_APP_ID, DEFAULT_PLAY_MEDIA_APP_ID as DEFAULT_PLAY_MEDIA_APP_ID, DOMAIN as DOMAIN
from .coordinator import RokuDataUpdateCoordinator as RokuDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
