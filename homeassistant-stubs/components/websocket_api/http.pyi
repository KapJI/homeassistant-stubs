import datetime as dt
import logging
from .auth import AUTH_REQUIRED_MESSAGE as AUTH_REQUIRED_MESSAGE, AuthPhase as AuthPhase
from .connection import ActiveConnection as ActiveConnection
from .const import DATA_CONNECTIONS as DATA_CONNECTIONS, MAX_PENDING_MSG as MAX_PENDING_MSG, PENDING_MSG_MAX_FORCE_READY as PENDING_MSG_MAX_FORCE_READY, PENDING_MSG_PEAK as PENDING_MSG_PEAK, PENDING_MSG_PEAK_TIME as PENDING_MSG_PEAK_TIME, SIGNAL_WEBSOCKET_CONNECTED as SIGNAL_WEBSOCKET_CONNECTED, SIGNAL_WEBSOCKET_DISCONNECTED as SIGNAL_WEBSOCKET_DISCONNECTED, URL as URL
from .error import Disconnect as Disconnect
from .messages import message_to_json_bytes as message_to_json_bytes
from .util import describe_request as describe_request
from _typeshed import Incomplete
from aiohttp import web
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.util.async_ import create_eager_task as create_eager_task
from homeassistant.util.json import json_loads as json_loads
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
    __slots__: Incomplete
    _hass: Incomplete
    _loop: Incomplete
    _request: Incomplete
    _wsock: Incomplete
    _handle_task: Incomplete
    _writer_task: Incomplete
    _closing: bool
    _authenticated: bool
    _logger: Incomplete
    _peak_checker_unsub: Incomplete
    _connection: Incomplete
    _message_queue: Incomplete
    _ready_future: Incomplete
    _release_ready_queue_size: int
    def __init__(self, hass: HomeAssistant, request: web.Request) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def description(self) -> str: ...
    async def _writer(self, send_bytes_text: Callable[[bytes], Coroutine[Any, Any, None]]) -> None: ...
    def _cancel_peak_checker(self) -> None: ...
    def _send_message(self, message: str | bytes | dict[str, Any]) -> None: ...
    def _release_ready_future_or_reschedule(self) -> None: ...
    def _check_write_peak(self, _utc_time: dt.datetime) -> None: ...
    def _cancel(self) -> None: ...
    def _async_handle_hass_stop(self, event: Event) -> None: ...
    async def async_handle(self) -> web.WebSocketResponse: ...
