import abc
from .manager import BluetoothManager as BluetoothManager
from _typeshed import Incomplete
from abc import abstractmethod
from bleak import BleakClient
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData as AdvertisementData, AdvertisementDataCallback as AdvertisementDataCallback, BaseBleakScanner
from collections.abc import Callable
from enum import Enum
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE
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
    def __init__(self, *, device, advertisement, connectable, time, **) -> None: ...

class BluetoothScanningMode(Enum):
    PASSIVE: str
    ACTIVE: str

BluetoothChange: Incomplete
BluetoothCallback = Callable[[BluetoothServiceInfoBleak, BluetoothChange], None]
ProcessAdvertisementCallback = Callable[[BluetoothServiceInfoBleak], bool]

class BaseHaScanner(metaclass=abc.ABCMeta):
    @property
    @abstractmethod
    def discovered_devices(self) -> list[BLEDevice]: ...
    async def async_diagnostics(self) -> dict[str, Any]: ...

class HaBleakScannerWrapper(BaseBleakScanner):
    _detection_cancel: Incomplete
    _mapped_filters: Incomplete
    _advertisement_data_callback: Incomplete
    def __init__(self, *args: Any, detection_callback: Union[AdvertisementDataCallback, None] = ..., service_uuids: Union[list[str], None] = ..., **kwargs: Any) -> None: ...
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
    def __init__(self, address_or_ble_device: Union[str, BLEDevice], *args: Any, **kwargs: Any) -> None: ...
