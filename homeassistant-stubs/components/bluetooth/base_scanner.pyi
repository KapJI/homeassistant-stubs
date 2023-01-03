import abc
import datetime
from .const import CONNECTABLE_FALLBACK_MAXIMUM_STALE_ADVERTISEMENT_SECONDS as CONNECTABLE_FALLBACK_MAXIMUM_STALE_ADVERTISEMENT_SECONDS, FALLBACK_MAXIMUM_STALE_ADVERTISEMENT_SECONDS as FALLBACK_MAXIMUM_STALE_ADVERTISEMENT_SECONDS
from .models import HaBluetoothConnector as HaBluetoothConnector
from _typeshed import Incomplete
from abc import abstractmethod
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
from collections.abc import Callable as Callable, Generator
from home_assistant_bluetooth import BluetoothServiceInfoBleak
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.util.dt import monotonic_time_coarse as monotonic_time_coarse
from typing import Any, Final

MONOTONIC_TIME: Final[Incomplete]

class BaseHaScanner(metaclass=abc.ABCMeta):
    __slots__: Incomplete
    hass: Incomplete
    source: Incomplete
    _connecting: int
    name: Incomplete
    scanning: bool
    def __init__(self, hass: HomeAssistant, source: str, adapter: str) -> None: ...
    def connecting(self) -> Generator[None, None, None]: ...
    @property
    @abstractmethod
    def discovered_devices(self) -> list[BLEDevice]: ...
    @property
    @abstractmethod
    def discovered_devices_and_advertisement_data(self) -> dict[str, tuple[BLEDevice, AdvertisementData]]: ...
    async def async_diagnostics(self) -> dict[str, Any]: ...

class BaseHaRemoteScanner(BaseHaScanner):
    __slots__: Incomplete
    _new_info_callback: Incomplete
    _discovered_device_advertisement_datas: Incomplete
    _discovered_device_timestamps: Incomplete
    _connector: Incomplete
    _connectable: Incomplete
    _details: Incomplete
    _expire_seconds: Incomplete
    def __init__(self, hass: HomeAssistant, scanner_id: str, name: str, new_info_callback: Callable[[BluetoothServiceInfoBleak], None], connector: HaBluetoothConnector, connectable: bool) -> None: ...
    def async_setup(self) -> CALLBACK_TYPE: ...
    def _async_expire_devices(self, _datetime: datetime.datetime) -> None: ...
    @property
    def discovered_devices(self) -> list[BLEDevice]: ...
    @property
    def discovered_devices_and_advertisement_data(self) -> dict[str, tuple[BLEDevice, AdvertisementData]]: ...
    def _async_on_advertisement(self, address: str, rssi: int, local_name: Union[str, None], service_uuids: list[str], service_data: dict[str, bytes], manufacturer_data: dict[int, bytes], tx_power: Union[int, None], details: dict[Any, Any]) -> None: ...
