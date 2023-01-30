import abc
import datetime
from . import models as models
from .const import CONNECTABLE_FALLBACK_MAXIMUM_STALE_ADVERTISEMENT_SECONDS as CONNECTABLE_FALLBACK_MAXIMUM_STALE_ADVERTISEMENT_SECONDS, SCANNER_WATCHDOG_INTERVAL as SCANNER_WATCHDOG_INTERVAL, SCANNER_WATCHDOG_TIMEOUT as SCANNER_WATCHDOG_TIMEOUT
from .models import HaBluetoothConnector as HaBluetoothConnector
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
from collections.abc import Callable as Callable, Generator
from home_assistant_bluetooth import BluetoothServiceInfoBleak
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.util.dt import monotonic_time_coarse as monotonic_time_coarse
from typing import Any, Final

MONOTONIC_TIME: Final[Incomplete]
_LOGGER: Incomplete

class BluetoothScannerDevice:
    scanner: BaseHaScanner
    ble_device: BLEDevice
    advertisement: AdvertisementData
    def __init__(self, scanner, ble_device, advertisement) -> None: ...

class BaseHaScanner(ABC, metaclass=abc.ABCMeta):
    __slots__: Incomplete
    hass: Incomplete
    connectable: bool
    source: Incomplete
    connector: Incomplete
    _connecting: int
    adapter: Incomplete
    name: Incomplete
    scanning: bool
    _last_detection: float
    _start_time: float
    _cancel_watchdog: Incomplete
    def __init__(self, hass: HomeAssistant, source: str, adapter: str, connector: Union[HaBluetoothConnector, None] = ...) -> None: ...
    def _async_stop_scanner_watchdog(self) -> None: ...
    def _async_setup_scanner_watchdog(self) -> None: ...
    def _async_watchdog_triggered(self) -> bool: ...
    def _async_scanner_watchdog(self, now: datetime.datetime) -> None: ...
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
    connectable: Incomplete
    _details: Incomplete
    _expire_seconds: Incomplete
    _storage: Incomplete
    def __init__(self, hass: HomeAssistant, scanner_id: str, name: str, new_info_callback: Callable[[BluetoothServiceInfoBleak], None], connector: Union[HaBluetoothConnector, None], connectable: bool) -> None: ...
    def async_setup(self) -> CALLBACK_TYPE: ...
    def _save_history(self, event: Union[Event, None] = ...) -> None: ...
    def _async_expire_devices(self, _datetime: datetime.datetime) -> None: ...
    @property
    def discovered_devices(self) -> list[BLEDevice]: ...
    @property
    def discovered_devices_and_advertisement_data(self) -> dict[str, tuple[BLEDevice, AdvertisementData]]: ...
    _last_detection: Incomplete
    def _async_on_advertisement(self, address: str, rssi: int, local_name: Union[str, None], service_uuids: list[str], service_data: dict[str, bytes], manufacturer_data: dict[int, bytes], tx_power: Union[int, None], details: dict[Any, Any]) -> None: ...
    async def async_diagnostics(self) -> dict[str, Any]: ...
