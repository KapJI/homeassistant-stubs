from .connection import ActiveConnection as ActiveConnection
from .error import Disconnect as Disconnect
from .http import WebSocketAdapter as WebSocketAdapter
from aiohttp.web import Request as Request
from collections.abc import Callable as Callable
from homeassistant.auth.models import RefreshToken as RefreshToken, User as User
from homeassistant.components.http.ban import process_success_login as process_success_login, process_wrong_login as process_wrong_login
from homeassistant.const import __version__ as __version__
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any, Final

TYPE_AUTH: Final[str]
TYPE_AUTH_INVALID: Final[str]
TYPE_AUTH_OK: Final[str]
TYPE_AUTH_REQUIRED: Final[str]
AUTH_MESSAGE_SCHEMA: Final[Any]

def auth_ok_message() -> dict[str, str]: ...
def auth_required_message() -> dict[str, str]: ...
def auth_invalid_message(message: str) -> dict[str, str]: ...

class AuthPhase:
    _hass: Any
    _send_message: Any
    _logger: Any
    _request: Any
    def __init__(self, logger: WebSocketAdapter, hass: HomeAssistant, send_message: Callable[[Union[str, dict[str, Any]]], None], request: Request) -> None: ...
    async def async_handle(self, msg: dict[str, str]) -> ActiveConnection: ...
    async def _async_finish_auth(self, user: User, refresh_token: RefreshToken) -> ActiveConnection: ...
