import voluptuous as vol
from .view import HomeAssistantView as HomeAssistantView
from _typeshed import Incomplete
from aiohttp import web as web
from collections.abc import Awaitable, Callable as Callable, Coroutine
from typing import Any, Concatenate, ParamSpec, TypeVar

_HassViewT = TypeVar('_HassViewT', bound=HomeAssistantView)
_P = ParamSpec('_P')
_LOGGER: Incomplete

class RequestDataValidator:
    _schema: Incomplete
    _allow_empty: Incomplete
    def __init__(self, schema: vol.Schema, allow_empty: bool = ...) -> None: ...
    def __call__(self, method: Callable[Concatenate[_HassViewT, web.Request, dict[str, Any], _P], Awaitable[web.Response]]) -> Callable[Concatenate[_HassViewT, web.Request, _P], Coroutine[Any, Any, web.Response]]: ...
