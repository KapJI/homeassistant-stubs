from .api import _get_manager as _get_manager, async_register_callback as async_register_callback
from .const import DOMAIN as DOMAIN
from .match import BluetoothCallbackMatcher as BluetoothCallbackMatcher
from .models import BluetoothChange as BluetoothChange
from .util import InvalidConfigEntryID as InvalidConfigEntryID, InvalidSource as InvalidSource, config_entry_id_to_source as config_entry_id_to_source
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable
from habluetooth import HaBluetoothSlotAllocations as HaBluetoothSlotAllocations, HaScannerRegistration as HaScannerRegistration
from home_assistant_bluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.json import json_bytes as json_bytes
from typing import Any

@callback
def async_setup(hass: HomeAssistant) -> None: ...
def serialize_service_info(service_info: BluetoothServiceInfoBleak, time_diff: float) -> dict[str, Any]: ...

class _AdvertisementSubscription:
    hass: Incomplete
    match_dict: Incomplete
    pending_service_infos: list[BluetoothServiceInfoBleak]
    ws_msg_id: Incomplete
    connection: Incomplete
    pending: bool
    time_diff: Incomplete
    def __init__(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, ws_msg_id: int, match_dict: BluetoothCallbackMatcher) -> None: ...
    @callback
    def _async_unsubscribe(self, cancel_callbacks: tuple[Callable[[], None], ...]) -> None: ...
    @callback
    def async_start(self) -> None: ...
    def _async_event_message(self, message: dict[str, Any]) -> None: ...
    def _async_added(self, service_infos: Iterable[BluetoothServiceInfoBleak]) -> None: ...
    def _async_removed(self, address: str) -> None: ...
    @callback
    def _async_on_advertisement(self, service_info: BluetoothServiceInfoBleak, change: BluetoothChange) -> None: ...

@websocket_api.require_admin
@websocket_api.async_response
async def ws_subscribe_advertisements(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def ws_subscribe_connection_allocations(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@websocket_api.require_admin
@websocket_api.async_response
async def ws_subscribe_scanner_details(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
