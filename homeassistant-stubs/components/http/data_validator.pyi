import voluptuous as vol
from .view import HomeAssistantView as HomeAssistantView
from aiohttp import web as web
from collections.abc import Awaitable, Callable as Callable
from typing import Any

_LOGGER: Any

class RequestDataValidator:
    _schema: Any
    _allow_empty: Any
    def __init__(self, schema: vol.Schema, allow_empty: bool = ...) -> None: ...
    def __call__(self, method: Callable[..., Awaitable[web.StreamResponse]]) -> Callable: ...
