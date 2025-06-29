import aiohttp
from .const import XML_MIME_TYPES as XML_MIME_TYPES
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import template as template
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.json import json_dumps as json_dumps
from homeassistant.util.ssl import SSLCipherList as SSLCipherList
from multidict import CIMultiDictProxy

DEFAULT_TIMEOUT: int
_LOGGER: Incomplete

class RestData:
    _hass: Incomplete
    _method: Incomplete
    _resource: Incomplete
    _encoding: Incomplete
    _auth: aiohttp.BasicAuth | aiohttp.DigestAuthMiddleware | None
    _headers: Incomplete
    _params: Incomplete
    _request_data: Incomplete
    _timeout: Incomplete
    _verify_ssl: Incomplete
    _ssl_cipher_list: Incomplete
    _session: aiohttp.ClientSession | None
    data: str | None
    last_exception: Exception | None
    headers: CIMultiDictProxy[str] | None
    def __init__(self, hass: HomeAssistant, method: str, resource: str, encoding: str, auth: aiohttp.DigestAuthMiddleware | aiohttp.BasicAuth | tuple[str, str] | None, headers: dict[str, str] | None, params: dict[str, str] | None, data: str | None, verify_ssl: bool, ssl_cipher_list: str, timeout: int = ...) -> None: ...
    def set_payload(self, payload: str) -> None: ...
    @property
    def url(self) -> str: ...
    def set_url(self, url: str) -> None: ...
    def _is_expected_content_type(self, content_type: str) -> bool: ...
    def data_without_xml(self) -> str | None: ...
    async def async_update(self, log_errors: bool = True) -> None: ...
