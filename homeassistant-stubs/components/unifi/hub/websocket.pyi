import aiounifi
from ..const import LOGGER as LOGGER
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval

RETRY_TIMER: int
CHECK_WEBSOCKET_INTERVAL: Incomplete

class UnifiWebsocket:
    hass: Incomplete
    api: Incomplete
    signal: Incomplete
    ws_task: Incomplete
    _cancel_websocket_check: Incomplete
    available: bool
    def __init__(self, hass: HomeAssistant, api: aiounifi.Controller, signal: str) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    async def stop_and_wait(self) -> None: ...
    def start_websocket(self) -> None: ...
    def reconnect(self, log: bool = False) -> None: ...
    def _async_watch_websocket(self, now: datetime) -> None: ...
