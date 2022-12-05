from aioesphomeapi import BluetoothLEAdvertisement as BluetoothLEAdvertisement
from homeassistant.components.bluetooth import BaseHaRemoteScanner as BaseHaRemoteScanner
from homeassistant.core import callback as callback
from typing import Any

class ESPHomeScanner(BaseHaRemoteScanner):
    def async_on_advertisement(self, adv: BluetoothLEAdvertisement) -> None: ...
    async def async_diagnostics(self) -> dict[str, Any]: ...
