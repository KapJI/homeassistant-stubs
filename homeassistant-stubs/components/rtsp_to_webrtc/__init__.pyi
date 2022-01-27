from homeassistant.components import camera as camera
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from rtsp_to_webrtc.interface import WebRTCClientInterface as WebRTCClientInterface
from typing import Any

_LOGGER: Any
DOMAIN: str
DATA_SERVER_URL: str
DATA_UNSUB: str
TIMEOUT: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
