import datetime
from _typeshed import Incomplete
from aioesphomeapi import BluetoothLEAdvertisement as BluetoothLEAdvertisement
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
from collections.abc import Callable as Callable
from homeassistant.components.bluetooth import BaseHaScanner as BaseHaScanner, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak, FALLBACK_MAXIMUM_STALE_ADVERTISEMENT_SECONDS as FALLBACK_MAXIMUM_STALE_ADVERTISEMENT_SECONDS, HaBluetoothConnector as HaBluetoothConnector
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.util.dt import monotonic_time_coarse as monotonic_time_coarse
from typing import Final

TWO_CHAR: Incomplete
CONNECTABLE_FALLBACK_MAXIMUM_STALE_ADVERTISEMENT_SECONDS: Final[int]

class ESPHomeScanner(BaseHaScanner):
    _new_info_callback: Incomplete
    _discovered_device_advertisement_datas: Incomplete
    _discovered_device_timestamps: Incomplete
    _connector: Incomplete
    _connectable: Incomplete
    _details: Incomplete
    _fallback_seconds: Incomplete
    def __init__(self, hass: HomeAssistant, scanner_id: str, new_info_callback: Callable[[BluetoothServiceInfoBleak], None], connector: HaBluetoothConnector, connectable: bool) -> None: ...
    def async_setup(self) -> CALLBACK_TYPE: ...
    def _async_expire_devices(self, _datetime: datetime.datetime) -> None: ...
    @property
    def discovered_devices(self) -> list[BLEDevice]: ...
    @property
    def discovered_devices_and_advertisement_data(self) -> dict[str, tuple[BLEDevice, AdvertisementData]]: ...
    def async_on_advertisement(self, adv: BluetoothLEAdvertisement) -> None: ...
