from _typeshed import Incomplete
from aioesphomeapi import BluetoothLEAdvertisement as BluetoothLEAdvertisement, BluetoothLERawAdvertisement as BluetoothLERawAdvertisement
from homeassistant.components.bluetooth import BaseHaRemoteScanner as BaseHaRemoteScanner, MONOTONIC_TIME as MONOTONIC_TIME
from homeassistant.core import callback as callback

class ESPHomeScanner(BaseHaRemoteScanner):
    __slots__: Incomplete
    def async_on_advertisement(self, adv: BluetoothLEAdvertisement) -> None: ...
    def async_on_raw_advertisements(self, advertisements: list[BluetoothLERawAdvertisement]) -> None: ...
