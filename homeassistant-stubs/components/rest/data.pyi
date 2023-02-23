import httpx
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import template as template
from homeassistant.helpers.httpx_client import get_async_client as get_async_client

DEFAULT_TIMEOUT: int
_LOGGER: Incomplete

class RestData:
    _hass: Incomplete
    _method: Incomplete
    _resource: Incomplete
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
    def __init__(self, hass: HomeAssistant, method: str, resource: str, auth: Union[httpx.DigestAuth, tuple[str, str], None], headers: Union[dict[str, str], None], params: Union[dict[str, str], None], data: Union[str, None], verify_ssl: bool, timeout: int = ...) -> None: ...
    def set_url(self, url: str) -> None: ...
    async def async_update(self, log_errors: bool = ...) -> None: ...
