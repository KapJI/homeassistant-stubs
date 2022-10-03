import httpx
from .frame import warn_use as warn_use
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.const import APPLICATION_NAME as APPLICATION_NAME, EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE, __version__ as __version__
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.loader import bind_hass as bind_hass
from typing import Any

DATA_ASYNC_CLIENT: str
DATA_ASYNC_CLIENT_NOVERIFY: str
SERVER_SOFTWARE: Incomplete
USER_AGENT: str

def get_async_client(hass: HomeAssistant, verify_ssl: bool = ...) -> httpx.AsyncClient: ...

class HassHttpXAsyncClient(httpx.AsyncClient):
    async def __aenter__(self) -> HassHttpXAsyncClient: ...
    async def __aexit__(self, *args: Any) -> None: ...

def create_async_httpx_client(hass: HomeAssistant, verify_ssl: bool = ..., auto_cleanup: bool = ..., **kwargs: Any) -> httpx.AsyncClient: ...
def _async_register_async_client_shutdown(hass: HomeAssistant, client: httpx.AsyncClient, original_aclose: Callable[..., Any]) -> None: ...
