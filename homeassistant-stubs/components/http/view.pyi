from .const import KEY_AUTHENTICATED as KEY_AUTHENTICATED
from _typeshed import Incomplete
from aiohttp import web
from aiohttp.typedefs import LooseHeaders as LooseHeaders
from aiohttp.web_urldispatcher import AbstractRoute as AbstractRoute
from collections.abc import Awaitable, Callable as Callable
from homeassistant import exceptions as exceptions
from homeassistant.const import CONTENT_TYPE_JSON as CONTENT_TYPE_JSON
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, is_callback as is_callback
from homeassistant.helpers.json import find_paths_unserializable_data as find_paths_unserializable_data, json_bytes as json_bytes, json_dumps as json_dumps
from homeassistant.util.json import JSON_ENCODE_EXCEPTIONS as JSON_ENCODE_EXCEPTIONS, format_unserializable_data as format_unserializable_data
from http import HTTPStatus
from typing import Any

_LOGGER: Incomplete

class HomeAssistantView:
    url: str | None
    extra_urls: list[str]
    requires_auth: bool
    cors_allowed: bool
    @staticmethod
    def context(request: web.Request) -> Context: ...
    @staticmethod
    def json(result: Any, status_code: HTTPStatus | int = ..., headers: LooseHeaders | None = ...) -> web.Response: ...
    def json_message(self, message: str, status_code: HTTPStatus | int = ..., message_code: str | None = ..., headers: LooseHeaders | None = ...) -> web.Response: ...
    def register(self, hass: HomeAssistant, app: web.Application, router: web.UrlDispatcher) -> None: ...

def request_handler_factory(hass: HomeAssistant, view: HomeAssistantView, handler: Callable) -> Callable[[web.Request], Awaitable[web.StreamResponse]]: ...
