import bleak
from .base_scanner import BaseHaScanner as BaseHaScanner, MONOTONIC_TIME as MONOTONIC_TIME
from .const import SCANNER_WATCHDOG_INTERVAL as SCANNER_WATCHDOG_INTERVAL, SCANNER_WATCHDOG_TIMEOUT as SCANNER_WATCHDOG_TIMEOUT, SOURCE_LOCAL as SOURCE_LOCAL, START_TIMEOUT as START_TIMEOUT
from .models import BluetoothScanningMode as BluetoothScanningMode, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from .util import async_reset_adapter as async_reset_adapter
from _typeshed import Incomplete
from bleak.backends.device import BLEDevice as BLEDevice
from bleak.backends.scanner import AdvertisementData as AdvertisementData, AdvertisementDataCallback as AdvertisementDataCallback
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util.package import is_docker_env as is_docker_env
from typing import Any

OriginalBleakScanner: Incomplete
PASSIVE_SCANNER_ARGS: Incomplete
_LOGGER: Incomplete
NEED_RESET_ERRORS: Incomplete
WAIT_FOR_ADAPTER_TO_INIT_ERRORS: Incomplete
ADAPTER_INIT_TIME: float
START_ATTEMPTS: int
SCANNING_MODE_TO_BLEAK: Incomplete
SCANNER_WATCHDOG_MULTIPLE: Incomplete

class ScannerStartError(HomeAssistantError): ...

def create_bleak_scanner(detection_callback: AdvertisementDataCallback, scanning_mode: BluetoothScanningMode, adapter: Union[str, None]) -> bleak.BleakScanner: ...

class HaScanner(BaseHaScanner):
    scanner: bleak.BleakScanner
    mac_address: Incomplete
    connectable: bool
    mode: Incomplete
    _start_stop_lock: Incomplete
    _new_info_callback: Incomplete
    scanning: bool
    def __init__(self, hass: HomeAssistant, mode: BluetoothScanningMode, adapter: str, address: str, new_info_callback: Callable[[BluetoothServiceInfoBleak], None]) -> None: ...
    @property
    def discovered_devices(self) -> list[BLEDevice]: ...
    @property
    def discovered_devices_and_advertisement_data(self) -> dict[str, tuple[BLEDevice, AdvertisementData]]: ...
    def async_setup(self) -> None: ...
    async def async_diagnostics(self) -> dict[str, Any]: ...
    _last_detection: Incomplete
    def _async_detection_callback(self, device: BLEDevice, advertisement_data: AdvertisementData) -> None: ...
    async def async_start(self) -> None: ...
    async def _async_start(self) -> None: ...
    def _async_scanner_watchdog(self, now: datetime) -> None: ...
    async def _async_restart_scanner(self) -> None: ...
    async def _async_reset_adapter(self) -> None: ...
    async def async_stop(self) -> None: ...
    async def _async_stop_scanner(self) -> None: ...
