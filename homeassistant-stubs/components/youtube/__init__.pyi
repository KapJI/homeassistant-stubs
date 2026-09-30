from .api import AsyncConfigEntryAuth as AsyncConfigEntryAuth
from .coordinator import YouTubeConfigEntry as YouTubeConfigEntry, YouTubeDataUpdateCoordinator as YouTubeDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: YouTubeConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: YouTubeConfigEntry) -> bool: ...
async def delete_devices(hass: HomeAssistant, entry: YouTubeConfigEntry, coordinator: YouTubeDataUpdateCoordinator) -> None: ...
