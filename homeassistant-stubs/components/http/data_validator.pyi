import voluptuous as vol
from .view import HomeAssistantView as HomeAssistantView
from aiohttp import web as web
from collections.abc import Awaitable
from homeassistant.const import HTTP_BAD_REQUEST as HTTP_BAD_REQUEST
from typing import Any, Callable

_LOGGER: Any

class RequestDataValidator:
    _schema: Any
    _allow_empty: Any
    def __init__(self, schema: vol.Schema, allow_empty: bool = ...) -> None: ...
    def __call__(self, method: Callable[..., Awaitable[web.StreamResponse]]) -> Callable: ...
