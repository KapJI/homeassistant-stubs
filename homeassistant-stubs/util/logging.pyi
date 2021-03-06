import logging.handlers
from collections.abc import Coroutine
from homeassistant.const import EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback, is_callback as is_callback
from typing import Any, Awaitable, Callable, overload

class HideSensitiveDataFilter(logging.Filter):
    text: Any
    def __init__(self, text: str) -> None: ...
    def filter(self, record: logging.LogRecord) -> bool: ...

class HomeAssistantQueueHandler(logging.handlers.QueueHandler):
    def handle(self, record: logging.LogRecord) -> Any: ...

def async_activate_log_queue_handler(hass: HomeAssistant) -> None: ...
def log_exception(format_err: Callable[..., Any], *args: Any) -> None: ...
@overload
def catch_log_exception(func: Callable[..., Awaitable[Any]], format_err: Callable[..., Any], *args: Any) -> Callable[..., Awaitable[None]]: ...
@overload
def catch_log_exception(func: Callable[..., Any], format_err: Callable[..., Any], *args: Any) -> Callable[..., None]: ...
def catch_log_coro_exception(target: Coroutine[Any, Any, Any], format_err: Callable[..., Any], *args: Any) -> Coroutine[Any, Any, Any]: ...
def async_create_catching_coro(target: Coroutine) -> Coroutine: ...
