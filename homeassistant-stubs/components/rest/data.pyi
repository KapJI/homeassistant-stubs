import httpx
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import template as template
from homeassistant.helpers.httpx_client import create_async_httpx_client as create_async_httpx_client

DEFAULT_TIMEOUT: int
_LOGGER: Incomplete

class RestData:
    _hass: Incomplete
    _method: Incomplete
    _resource: Incomplete
    _encoding: Incomplete
    _auth: Incomplete
    _headers: Incomplete
    _params: Incomplete
    _request_data: Incomplete
    _timeout: Incomplete
    _verify_ssl: Incomplete
    _async_client: Incomplete
    data: Incomplete
    last_exception: Incomplete
    headers: Incomplete
    def __init__(self, hass: HomeAssistant, method: str, resource: str, encoding: str, auth: httpx.DigestAuth | tuple[str, str] | None, headers: dict[str, str] | None, params: dict[str, str] | None, data: str | None, verify_ssl: bool, timeout: int = ...) -> None: ...
    def set_url(self, url: str) -> None: ...
    async def async_update(self, log_errors: bool = ...) -> None: ...
