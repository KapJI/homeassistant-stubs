import datetime as dt
import logging
from .auth import AuthPhase as AuthPhase, auth_required_message as auth_required_message
from .connection import ActiveConnection as ActiveConnection
from .const import CANCELLATION_ERRORS as CANCELLATION_ERRORS, DATA_CONNECTIONS as DATA_CONNECTIONS, FEATURE_COALESCE_MESSAGES as FEATURE_COALESCE_MESSAGES, MAX_PENDING_MSG as MAX_PENDING_MSG, PENDING_MSG_PEAK as PENDING_MSG_PEAK, PENDING_MSG_PEAK_TIME as PENDING_MSG_PEAK_TIME, SIGNAL_WEBSOCKET_CONNECTED as SIGNAL_WEBSOCKET_CONNECTED, SIGNAL_WEBSOCKET_DISCONNECTED as SIGNAL_WEBSOCKET_DISCONNECTED, URL as URL
from .error import Disconnect as Disconnect
from .messages import message_to_json as message_to_json
from _typeshed import Incomplete
from aiohttp import web
from collections.abc import Callable as Callable
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.json import json_loads as json_loads
from typing import Any, Final

_WS_LOGGER: Final[Incomplete]

class WebsocketAPIView(HomeAssistantView):
    name: str
    url: str
    requires_auth: bool
    async def get(self, request: web.Request) -> web.WebSocketResponse: ...

class WebSocketAdapter(logging.LoggerAdapter):
    def process(self, msg: str, kwargs: Any) -> tuple[str, Any]: ...

class WebSocketHandler:
    hass: Incomplete
    request: Incomplete
    wsock: Incomplete
    _to_write: Incomplete
    _handle_task: Incomplete
    _writer_task: Incomplete
    _logger: Incomplete
    _peak_checker_unsub: Incomplete
    connection: Incomplete
    def __init__(self, hass: HomeAssistant, request: web.Request) -> None: ...
    async def _writer(self) -> None: ...
    def _send_message(self, message: Union[str, dict[str, Any], Callable[[], str]]) -> None: ...
    def _check_write_peak(self, _utc_time: dt.datetime) -> None: ...
    def _cancel(self) -> None: ...
    async def async_handle(self) -> web.WebSocketResponse: ...
