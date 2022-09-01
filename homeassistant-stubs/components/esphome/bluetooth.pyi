import datetime
from _typeshed import Incomplete
from aioesphomeapi import APIClient as APIClient, BluetoothLEAdvertisement as BluetoothLEAdvertisement
from bleak.backends.device import BLEDevice
from collections.abc import Callable as Callable
from homeassistant.components.bluetooth import BaseHaScanner as BaseHaScanner, async_get_advertisement_callback as async_get_advertisement_callback, async_register_scanner as async_register_scanner
from homeassistant.components.bluetooth.models import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval

ADV_STALE_TIME: int
TWO_CHAR: Incomplete

async def async_connect_scanner(hass: HomeAssistant, entry: ConfigEntry, cli: APIClient) -> None: ...

class ESPHomeScannner(BaseHaScanner):
    _hass: Incomplete
    _new_info_callback: Incomplete
    _discovered_devices: Incomplete
    _discovered_device_timestamps: Incomplete
    _source: Incomplete
    def __init__(self, hass: HomeAssistant, scanner_id: str, new_info_callback: Callable[[BluetoothServiceInfoBleak], None]) -> None: ...
    def async_setup(self) -> CALLBACK_TYPE: ...
    def _async_expire_devices(self, _datetime: datetime.datetime) -> None: ...
    @property
    def discovered_devices(self) -> list[BLEDevice]: ...
    def async_on_advertisement(self, adv: BluetoothLEAdvertisement) -> None: ...
