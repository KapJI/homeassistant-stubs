import abc
from .manager import BluetoothManager as BluetoothManager
from _typeshed import Incomplete
from abc import abstractmethod
from bleak import BleakClient
from bleak.backends.client import BaseBleakClient as BaseBleakClient
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData as AdvertisementData, AdvertisementDataCallback as AdvertisementDataCallback, BaseBleakScanner
from collections.abc import Callable
from enum import Enum
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers.frame import report as report
from homeassistant.helpers.service_info.bluetooth import BluetoothServiceInfo as BluetoothServiceInfo
from typing import Any, Final

_LOGGER: Incomplete
FILTER_UUIDS: Final[str]
MANAGER: Union[BluetoothManager, None]

class BluetoothServiceInfoBleak(BluetoothServiceInfo):
    device: BLEDevice
    advertisement: AdvertisementData
    connectable: bool
    time: float
    def as_dict(self) -> dict[str, Any]: ...
    def __init__(self, *, device, advertisement, connectable, time, **) -> None: ...

class BluetoothScanningMode(Enum):
    PASSIVE: str
    ACTIVE: str

BluetoothChange: Incomplete
BluetoothCallback = Callable[[BluetoothServiceInfoBleak, BluetoothChange], None]
ProcessAdvertisementCallback = Callable[[BluetoothServiceInfoBleak], bool]

class HaBluetoothConnector:
    client: type[BaseBleakClient]
    source: str
    can_connect: Callable[[], bool]
    def __init__(self, client, source, can_connect) -> None: ...

class _HaWrappedBleakBackend:
    device: BLEDevice
    client: type[BaseBleakClient]
    def __init__(self, device, client) -> None: ...

class BaseHaScanner(metaclass=abc.ABCMeta):
    hass: Incomplete
    source: Incomplete
    def __init__(self, hass: HomeAssistant, source: str) -> None: ...
    @property
    @abstractmethod
    def discovered_devices(self) -> list[BLEDevice]: ...
    @property
    @abstractmethod
    def discovered_devices_and_advertisement_data(self) -> dict[str, tuple[BLEDevice, AdvertisementData]]: ...
    async def async_diagnostics(self) -> dict[str, Any]: ...

class HaBleakScannerWrapper(BaseBleakScanner):
    _detection_cancel: Incomplete
    _mapped_filters: Incomplete
    _advertisement_data_callback: Incomplete
    def __init__(self, *args: Any, detection_callback: Union[AdvertisementDataCallback, None] = ..., service_uuids: Union[list[str], None] = ..., **kwargs: Any) -> None: ...
    @classmethod
    async def discover(cls, timeout: float = ..., **kwargs: Any) -> list[BLEDevice]: ...
    async def stop(self, *args: Any, **kwargs: Any) -> None: ...
    async def start(self, *args: Any, **kwargs: Any) -> None: ...
    def _map_filters(self, *args: Any, **kwargs: Any) -> bool: ...
    def set_scanning_filter(self, *args: Any, **kwargs: Any) -> None: ...
    def _cancel_callback(self) -> None: ...
    @property
    def discovered_devices(self) -> list[BLEDevice]: ...
    def register_detection_callback(self, callback: Union[AdvertisementDataCallback, None]) -> None: ...
    def _setup_detection_callback(self) -> None: ...
    def __del__(self) -> None: ...

class HaBleakClientWrapper(BleakClient):
    __address: Incomplete
    __disconnected_callback: Incomplete
    __timeout: Incomplete
    __ble_device: Incomplete
    _backend: Incomplete
    def __init__(self, address_or_ble_device: Union[str, BLEDevice], disconnected_callback: Union[Callable[[BleakClient], None], None] = ..., *args: Any, timeout: float = ..., **kwargs: Any) -> None: ...
    @property
    def is_connected(self) -> bool: ...
    def set_disconnected_callback(self, callback: Union[Callable[[BleakClient], None], None], **kwargs: Any) -> None: ...
    async def connect(self, **kwargs: Any) -> bool: ...
    def _async_get_backend_for_ble_device(self, ble_device: BLEDevice) -> Union[_HaWrappedBleakBackend, None]: ...
    def _async_get_backend(self) -> Union[_HaWrappedBleakBackend, None]: ...
    def _async_get_fallback_backend(self) -> _HaWrappedBleakBackend: ...
    async def disconnect(self) -> bool: ...
