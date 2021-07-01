from .const import KEY_AUTHENTICATED as KEY_AUTHENTICATED, KEY_HASS as KEY_HASS
from aiohttp import web
from aiohttp.typedefs import LooseHeaders as LooseHeaders
from aiohttp.web_urldispatcher import AbstractRoute as AbstractRoute
from collections.abc import Awaitable, Callable as Callable
from homeassistant import exceptions as exceptions
from homeassistant.const import CONTENT_TYPE_JSON as CONTENT_TYPE_JSON, HTTP_OK as HTTP_OK, HTTP_SERVICE_UNAVAILABLE as HTTP_SERVICE_UNAVAILABLE
from homeassistant.core import Context as Context, is_callback as is_callback
from homeassistant.helpers.json import JSONEncoder as JSONEncoder
from typing import Any

_LOGGER: Any

class HomeAssistantView:
    url: Union[str, None]
    extra_urls: list[str]
    requires_auth: bool
    cors_allowed: bool
    @staticmethod
    def context(request: web.Request) -> Context: ...
    @staticmethod
    def json(result: Any, status_code: int = ..., headers: Union[LooseHeaders, None] = ...) -> web.Response: ...
    def json_message(self, message: str, status_code: int = ..., message_code: Union[str, None] = ..., headers: Union[LooseHeaders, None] = ...) -> web.Response: ...
    def register(self, app: web.Application, router: web.UrlDispatcher) -> None: ...

def request_handler_factory(view: HomeAssistantView, handler: Callable) -> Callable[[web.Request], Awaitable[web.StreamResponse]]: ...
