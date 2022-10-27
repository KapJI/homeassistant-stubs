from _typeshed import Incomplete
from homeassistant.components import camera as camera, websocket_api as websocket_api
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from rtsp_to_webrtc.interface import WebRTCClientInterface as WebRTCClientInterface
from typing import Any

_LOGGER: Incomplete
DOMAIN: str
DATA_SERVER_URL: str
DATA_UNSUB: str
TIMEOUT: int
CONF_STUN_SERVER: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
def ws_get_settings(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
