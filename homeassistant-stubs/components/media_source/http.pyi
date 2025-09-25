from .error import Unresolvable as Unresolvable
from .helper import async_browse_media as async_browse_media, async_resolve_media as async_resolve_media
from homeassistant.components import frontend as frontend, websocket_api as websocket_api
from homeassistant.components.media_player import ATTR_MEDIA_CONTENT_ID as ATTR_MEDIA_CONTENT_ID, BrowseError as BrowseError, CONTENT_AUTH_EXPIRY_TIME as CONTENT_AUTH_EXPIRY_TIME, async_process_play_media_url as async_process_play_media_url
from homeassistant.components.websocket_api import ActiveConnection as ActiveConnection
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

def async_setup(hass: HomeAssistant) -> None: ...
@websocket_api.async_response
async def websocket_browse_media(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.async_response
async def websocket_resolve_media(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
