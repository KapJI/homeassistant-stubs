from . import const as const, messages as messages
from .http import WebSocketAdapter as WebSocketAdapter
from homeassistant.auth.models import RefreshToken as RefreshToken, User as User
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, Unauthorized as Unauthorized
from typing import Any, Callable

class ActiveConnection:
    logger: Any
    hass: Any
    send_message: Any
    user: Any
    refresh_token_id: Any
    subscriptions: Any
    last_id: int
    def __init__(self, logger: WebSocketAdapter, hass: HomeAssistant, send_message: Callable[[Union[str, dict[str, Any]]], None], user: User, refresh_token: RefreshToken) -> None: ...
    def context(self, msg: dict[str, Any]) -> Context: ...
    def send_result(self, msg_id: int, result: Union[Any, None] = ...) -> None: ...
    async def send_big_result(self, msg_id: int, result: Any) -> None: ...
    def send_error(self, msg_id: int, code: str, message: str) -> None: ...
    def async_handle(self, msg: dict[str, Any]) -> None: ...
    def async_close(self) -> None: ...
    def async_handle_exception(self, msg: dict[str, Any], err: Exception) -> None: ...
