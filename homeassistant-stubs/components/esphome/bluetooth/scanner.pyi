from aioesphomeapi import BluetoothLEAdvertisement as BluetoothLEAdvertisement
from homeassistant.components.bluetooth import BaseHaRemoteScanner as BaseHaRemoteScanner
from homeassistant.core import callback as callback

class ESPHomeScanner(BaseHaRemoteScanner):
    def async_on_advertisement(self, adv: BluetoothLEAdvertisement) -> None: ...
