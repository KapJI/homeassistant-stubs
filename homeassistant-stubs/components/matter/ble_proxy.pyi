from _typeshed import Incomplete
from bleak.backends.device import BLEDevice as BLEDevice
from collections.abc import Callable as Callable
from home_assistant_bluetooth import BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from homeassistant.components.bluetooth import BluetoothScanningMode as BluetoothScanningMode, MONOTONIC_TIME as MONOTONIC_TIME, async_ble_device_from_address as async_ble_device_from_address, async_register_callback as async_register_callback
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from matter_ble_proxy import AdvertisementData, BleDeviceResolver, BleScanSource, MatterBleProxy
from typing import override

_LOGGER: Incomplete
_MAX_STALE_ADVERTISEMENT_SECONDS: int

class HaBluetoothScanSource(BleScanSource):
    _hass: Incomplete
    _cancel: CALLBACK_TYPE | None
    def __init__(self, hass: HomeAssistant) -> None: ...
    @override
    async def start(self, callback_fn: Callable[[AdvertisementData], None]) -> None: ...
    @override
    async def stop(self) -> None: ...

class HaBluetoothDeviceResolver(BleDeviceResolver):
    _hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    @override
    async def resolve(self, address: str) -> BLEDevice | None: ...

def _to_advertisement_data(service_info: BluetoothServiceInfoBleak) -> AdvertisementData: ...
def create_matter_ble_proxy(hass: HomeAssistant, ws_url: str) -> MatterBleProxy: ...
