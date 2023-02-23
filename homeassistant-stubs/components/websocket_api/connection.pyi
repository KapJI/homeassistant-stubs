from . import const as const, messages as messages
from .http import WebSocketAdapter as WebSocketAdapter
from .util import describe_request as describe_request
from _typeshed import Incomplete
from aiohttp import web as web
from collections.abc import Callable as Callable
from homeassistant.auth.models import RefreshToken as RefreshToken, User as User
from homeassistant.components.http import current_request as current_request
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, Unauthorized as Unauthorized
from typing import Any

current_connection: Incomplete

class ActiveConnection:
    logger: Incomplete
    hass: Incomplete
    send_message: Incomplete
    user: Incomplete
    refresh_token_id: Incomplete
    subscriptions: Incomplete
    last_id: int
    supported_features: Incomplete
    handlers: Incomplete
    def __init__(self, logger: WebSocketAdapter, hass: HomeAssistant, send_message: Callable[[Union[str, dict[str, Any], Callable[[], str]]], None], user: User, refresh_token: RefreshToken) -> None: ...
    def get_description(self, request: Union[web.Request, None]) -> str: ...
    def context(self, msg: dict[str, Any]) -> Context: ...
    def send_result(self, msg_id: int, result: Union[Any, None] = ...) -> None: ...
    def send_error(self, msg_id: int, code: str, message: str) -> None: ...
    def async_handle(self, msg: dict[str, Any]) -> None: ...
    def async_handle_close(self) -> None: ...
    def async_handle_exception(self, msg: dict[str, Any], err: Exception) -> None: ...
