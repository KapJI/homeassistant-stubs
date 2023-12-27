import asyncio
import uuid
from .cache import ESPHomeBluetoothCache as ESPHomeBluetoothCache
from .characteristic import BleakGATTCharacteristicESPHome as BleakGATTCharacteristicESPHome
from .descriptor import BleakGATTDescriptorESPHome as BleakGATTDescriptorESPHome
from .device import ESPHomeBluetoothDevice as ESPHomeBluetoothDevice
from .scanner import ESPHomeScanner as ESPHomeScanner
from .service import BleakGATTServiceESPHome as BleakGATTServiceESPHome
from _typeshed import Incomplete
from aioesphomeapi import APIClient as APIClient, APIVersion as APIVersion, DeviceInfo as DeviceInfo
from bleak.backends.characteristic import BleakGATTCharacteristic
from bleak.backends.client import BaseBleakClient, NotifyCallback as NotifyCallback
from bleak.backends.device import BLEDevice
from bleak.backends.service import BleakGATTServiceCollection
from collections.abc import Callable
from dataclasses import dataclass
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE
from typing import Any, TypeVar
from typing_extensions import Buffer

DEFAULT_MTU: int
GATT_HEADER_SIZE: int
DISCONNECT_TIMEOUT: float
CONNECT_FREE_SLOT_TIMEOUT: float
GATT_READ_TIMEOUT: float
CCCD_UUID: str
CCCD_NOTIFY_BYTES: bytes
CCCD_INDICATE_BYTES: bytes
DEFAULT_MAX_WRITE_WITHOUT_RESPONSE: Incomplete
_LOGGER: Incomplete
_WrapFuncType = TypeVar('_WrapFuncType', bound=Callable[..., Any])

def mac_to_int(address: str) -> int: ...
def api_error_as_bleak_error(func: _WrapFuncType) -> _WrapFuncType: ...

@dataclass(slots=True)
class ESPHomeClientData:
    bluetooth_device: ESPHomeBluetoothDevice
    cache: ESPHomeBluetoothCache
    client: APIClient
    device_info: DeviceInfo
    api_version: APIVersion
    title: str
    scanner: ESPHomeScanner | None
    disconnect_callbacks: set[Callable[[], None]] = ...
    def __init__(self, bluetooth_device, cache, client, device_info, api_version, title, scanner, disconnect_callbacks) -> None: ...

class ESPHomeClient(BaseBleakClient):
    _disconnect_callbacks: Incomplete
    _loop: Incomplete
    _ble_device: Incomplete
    _address_as_int: Incomplete
    _source: Incomplete
    _cache: Incomplete
    _bluetooth_device: Incomplete
    _client: Incomplete
    _is_connected: bool
    _mtu: Incomplete
    _cancel_connection_state: Incomplete
    _notify_cancels: Incomplete
    _device_info: Incomplete
    _feature_flags: Incomplete
    _address_type: Incomplete
    _source_name: Incomplete
    _description: Incomplete
    _scanner: Incomplete
    def __init__(self, address_or_ble_device: BLEDevice | str, *args: Any, client_data: ESPHomeClientData, **kwargs: Any) -> None: ...
    def __str__(self) -> str: ...
    services: Incomplete
    def _async_disconnected_cleanup(self) -> None: ...
    def _async_ble_device_disconnected(self) -> None: ...
    def _async_esp_disconnected(self) -> None: ...
    _disconnected_callback: Incomplete
    def _async_call_bleak_disconnected_callback(self) -> None: ...
    def _on_bluetooth_connection_state(self, connected_future: asyncio.Future[bool], connected: bool, mtu: int, error: int) -> None: ...
    async def connect(self, dangerous_use_bleak_cache: bool = False, **kwargs: Any) -> bool: ...
    async def disconnect(self) -> bool: ...
    async def _disconnect(self) -> bool: ...
    async def _wait_for_free_connection_slot(self, timeout: float) -> None: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def mtu_size(self) -> int: ...
    async def pair(self, *args: Any, **kwargs: Any) -> bool: ...
    async def unpair(self) -> bool: ...
    async def get_services(self, dangerous_use_bleak_cache: bool = False, **kwargs: Any) -> BleakGATTServiceCollection: ...
    async def _get_services(self, dangerous_use_bleak_cache: bool = False, **kwargs: Any) -> BleakGATTServiceCollection: ...
    def _resolve_characteristic(self, char_specifier: BleakGATTCharacteristic | int | str | uuid.UUID) -> BleakGATTCharacteristic: ...
    async def clear_cache(self) -> bool: ...
    async def read_gatt_char(self, char_specifier: BleakGATTCharacteristic | int | str | uuid.UUID, **kwargs: Any) -> bytearray: ...
    async def read_gatt_descriptor(self, handle: int, **kwargs: Any) -> bytearray: ...
    async def write_gatt_char(self, characteristic: BleakGATTCharacteristic | int | str | uuid.UUID, data: Buffer, response: bool = False) -> None: ...
    async def write_gatt_descriptor(self, handle: int, data: Buffer) -> None: ...
    async def start_notify(self, characteristic: BleakGATTCharacteristic, callback: NotifyCallback, **kwargs: Any) -> None: ...
    async def stop_notify(self, char_specifier: BleakGATTCharacteristic | int | str | uuid.UUID) -> None: ...
    def _raise_if_not_connected(self) -> None: ...
    def __del__(self) -> None: ...
