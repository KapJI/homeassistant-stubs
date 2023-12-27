import voluptuous as vol
from . import const as const, messages as messages
from .connection import ActiveConnection as ActiveConnection
from collections.abc import Callable as Callable
from homeassistant.const import HASSIO_USER_NAME as HASSIO_USER_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import Unauthorized as Unauthorized
from typing import Any

async def _handle_async_response(func: const.AsyncWebSocketCommandHandler, hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None: ...
def async_response(func: const.AsyncWebSocketCommandHandler) -> const.WebSocketCommandHandler: ...
def require_admin(func: const.WebSocketCommandHandler) -> const.WebSocketCommandHandler: ...
def ws_require_user(only_owner: bool = False, only_system_user: bool = False, allow_system_user: bool = True, only_active_user: bool = True, only_inactive_user: bool = False, only_supervisor: bool = False) -> Callable[[const.WebSocketCommandHandler], const.WebSocketCommandHandler]: ...
def websocket_command(schema: dict[vol.Marker, Any] | vol.All) -> Callable[[const.WebSocketCommandHandler], const.WebSocketCommandHandler]: ...
