import voluptuous as vol
from .view import HomeAssistantView as HomeAssistantView
from _typeshed import Incomplete
from aiohttp import web as web
from collections.abc import Awaitable, Callable as Callable

_LOGGER: Incomplete

class RequestDataValidator:
    _schema: Incomplete
    _allow_empty: Incomplete
    def __init__(self, schema: vol.Schema, allow_empty: bool = ...) -> None: ...
    def __call__(self, method: Callable[..., Awaitable[web.StreamResponse]]) -> Callable: ...
