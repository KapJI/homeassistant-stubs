import voluptuous as vol
from . import commands as commands, connection as connection, const as const, decorators as decorators, http as http, messages as messages
from .connection import ActiveConnection as ActiveConnection, current_connection as current_connection
from .const import AsyncWebSocketCommandHandler as AsyncWebSocketCommandHandler, ERR_HOME_ASSISTANT_ERROR as ERR_HOME_ASSISTANT_ERROR, ERR_INVALID_FORMAT as ERR_INVALID_FORMAT, ERR_NOT_FOUND as ERR_NOT_FOUND, ERR_NOT_SUPPORTED as ERR_NOT_SUPPORTED, ERR_TEMPLATE_ERROR as ERR_TEMPLATE_ERROR, ERR_TIMEOUT as ERR_TIMEOUT, ERR_UNAUTHORIZED as ERR_UNAUTHORIZED, ERR_UNKNOWN_COMMAND as ERR_UNKNOWN_COMMAND, ERR_UNKNOWN_ERROR as ERR_UNKNOWN_ERROR, WebSocketCommandHandler as WebSocketCommandHandler
from .decorators import async_response as async_response, require_admin as require_admin, websocket_command as websocket_command, ws_require_user as ws_require_user
from .messages import BASE_COMMAND_MESSAGE_SCHEMA as BASE_COMMAND_MESSAGE_SCHEMA, error_message as error_message, event_message as event_message, result_message as result_message
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from typing import Final

DOMAIN: Final[Incomplete]
DEPENDENCIES: Final[tuple[str]]

def async_register_command(hass: HomeAssistant, command_or_handler: Union[str, const.WebSocketCommandHandler], handler: Union[const.WebSocketCommandHandler, None] = ..., schema: Union[vol.Schema, None] = ...) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
