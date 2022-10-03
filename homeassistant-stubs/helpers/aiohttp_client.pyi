import aiohttp
from .frame import warn_use as warn_use
from .json import json_dumps as json_dumps, json_loads as json_loads
from _typeshed import Incomplete
from aiohttp import web
from aiohttp.typedefs import JSONDecoder as JSONDecoder
from collections.abc import Awaitable, Callable as Callable
from homeassistant import config_entries as config_entries
from homeassistant.const import APPLICATION_NAME as APPLICATION_NAME, EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE, __version__ as __version__
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.loader import bind_hass as bind_hass
from typing import Any

DATA_CONNECTOR: str
DATA_CONNECTOR_NOTVERIFY: str
DATA_CLIENTSESSION: str
DATA_CLIENTSESSION_NOTVERIFY: str
SERVER_SOFTWARE: Incomplete
WARN_CLOSE_MSG: str

class HassClientResponse(aiohttp.ClientResponse):
    async def json(self, *args: Any, loads: JSONDecoder = ..., **kwargs: Any) -> Any: ...

def async_get_clientsession(hass: HomeAssistant, verify_ssl: bool = ...) -> aiohttp.ClientSession: ...
def async_create_clientsession(hass: HomeAssistant, verify_ssl: bool = ..., auto_cleanup: bool = ..., **kwargs: Any) -> aiohttp.ClientSession: ...
def _async_create_clientsession(hass: HomeAssistant, verify_ssl: bool = ..., auto_cleanup_method: Union[Callable[[HomeAssistant, aiohttp.ClientSession], None], None] = ..., **kwargs: Any) -> aiohttp.ClientSession: ...
async def async_aiohttp_proxy_web(hass: HomeAssistant, request: web.BaseRequest, web_coro: Awaitable[aiohttp.ClientResponse], buffer_size: int = ..., timeout: int = ...) -> Union[web.StreamResponse, None]: ...
async def async_aiohttp_proxy_stream(hass: HomeAssistant, request: web.BaseRequest, stream: aiohttp.StreamReader, content_type: Union[str, None], buffer_size: int = ..., timeout: int = ...) -> web.StreamResponse: ...
def _async_register_clientsession_shutdown(hass: HomeAssistant, clientsession: aiohttp.ClientSession) -> None: ...
def _async_register_default_clientsession_shutdown(hass: HomeAssistant, clientsession: aiohttp.ClientSession) -> None: ...
def _async_get_connector(hass: HomeAssistant, verify_ssl: bool = ...) -> aiohttp.BaseConnector: ...
