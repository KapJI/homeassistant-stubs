import voluptuous as vol
from .view import HomeAssistantView as HomeAssistantView
from aiohttp import web as web
from homeassistant.const import HTTP_BAD_REQUEST as HTTP_BAD_REQUEST
from typing import Awaitable, Callable

class RequestDataValidator:
    def __init__(self, schema: vol.Schema, allow_empty: bool=...) -> None: ...
    def __call__(self, method: Callable[..., Awaitable[web.StreamResponse]]) -> Callable: ...
