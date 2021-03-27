import aiohttp
from aiohttp import web
from homeassistant.const import EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE
from homeassistant.core import Event as Event, callback as callback
from homeassistant.helpers.frame import warn_use as warn_use
from homeassistant.helpers.typing import HomeAssistantType as HomeAssistantType
from homeassistant.loader import bind_hass as bind_hass
from typing import Any, Awaitable, Optional

DATA_CONNECTOR: str
DATA_CONNECTOR_NOTVERIFY: str
DATA_CLIENTSESSION: str
DATA_CLIENTSESSION_NOTVERIFY: str
SERVER_SOFTWARE: Any

def async_get_clientsession(hass: HomeAssistantType, verify_ssl: bool=...) -> aiohttp.ClientSession: ...
def async_create_clientsession(hass: HomeAssistantType, verify_ssl: bool=..., auto_cleanup: bool=..., **kwargs: Any) -> aiohttp.ClientSession: ...
async def async_aiohttp_proxy_web(hass: HomeAssistantType, request: web.BaseRequest, web_coro: Awaitable[aiohttp.ClientResponse], buffer_size: int=..., timeout: int=...) -> Optional[web.StreamResponse]: ...
async def async_aiohttp_proxy_stream(hass: HomeAssistantType, request: web.BaseRequest, stream: aiohttp.StreamReader, content_type: Optional[str], buffer_size: int=..., timeout: int=...) -> web.StreamResponse: ...
