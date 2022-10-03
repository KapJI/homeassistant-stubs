import datetime
from _typeshed import Incomplete
from aioesphomeapi import BluetoothLEAdvertisement as BluetoothLEAdvertisement
from bleak.backends.device import BLEDevice
from collections.abc import Callable as Callable
from homeassistant.components.bluetooth import BaseHaScanner as BaseHaScanner, HaBluetoothConnector as HaBluetoothConnector
from homeassistant.components.bluetooth.models import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval

ADV_STALE_TIME: Incomplete
TWO_CHAR: Incomplete

class ESPHomeScanner(BaseHaScanner):
    _hass: Incomplete
    _new_info_callback: Incomplete
    _discovered_devices: Incomplete
    _discovered_device_timestamps: Incomplete
    _source: Incomplete
    _connector: Incomplete
    _connectable: Incomplete
    _details: Incomplete
    def __init__(self, hass: HomeAssistant, scanner_id: str, new_info_callback: Callable[[BluetoothServiceInfoBleak], None], connector: HaBluetoothConnector, connectable: bool) -> None: ...
    def async_setup(self) -> CALLBACK_TYPE: ...
    def _async_expire_devices(self, _datetime: datetime.datetime) -> None: ...
    @property
    def discovered_devices(self) -> list[BLEDevice]: ...
    async def async_get_device_by_address(self, address: str) -> Union[BLEDevice, None]: ...
    def async_on_advertisement(self, adv: BluetoothLEAdvertisement) -> None: ...
