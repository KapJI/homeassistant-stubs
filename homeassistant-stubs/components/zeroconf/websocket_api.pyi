from .const import DOMAIN as DOMAIN, REQUEST_TIMEOUT as REQUEST_TIMEOUT
from .discovery import DATA_DISCOVERY as DATA_DISCOVERY, ZeroconfDiscovery as ZeroconfDiscovery
from .models import HaAsyncZeroconf as HaAsyncZeroconf
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.json import json_bytes as json_bytes
from typing import Any
from zeroconf import DNSPointer, Zeroconf as Zeroconf
from zeroconf.asyncio import AsyncServiceInfo

_LOGGER: Incomplete
CLASS_IN: int
TYPE_PTR: int

@callback
def async_setup(hass: HomeAssistant) -> None: ...
def serialize_service_info(service_info: AsyncServiceInfo) -> dict[str, Any]: ...

class _DiscoverySubscription:
    hass: Incomplete
    discovery: Incomplete
    aiozc: Incomplete
    ws_msg_id: Incomplete
    connection: Incomplete
    def __init__(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, ws_msg_id: int, aiozc: HaAsyncZeroconf, discovery: ZeroconfDiscovery) -> None: ...
    @callback
    def _async_unsubscribe(self, cancel_callbacks: tuple[Callable[[], None], ...]) -> None: ...
    async def async_start(self) -> None: ...
    async def _async_update_from_cache(self) -> None: ...
    def _async_get_ptr_records(self, zc: Zeroconf) -> list[DNSPointer]: ...
    async def _async_handle_service(self, info: AsyncServiceInfo) -> None: ...
    def _async_event_message(self, message: dict[str, Any]) -> None: ...
    def _async_on_update(self, info: AsyncServiceInfo) -> None: ...
    def _async_on_remove(self, name: str) -> None: ...

@websocket_api.require_admin
@websocket_api.async_response
async def ws_subscribe_discovery(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
