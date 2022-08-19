import time
from . import models as models
from .const import CONF_ADAPTER as CONF_ADAPTER, DEFAULT_ADAPTERS as DEFAULT_ADAPTERS, DOMAIN as DOMAIN
from .match import ADDRESS as ADDRESS, BluetoothCallbackMatcher as BluetoothCallbackMatcher, IntegrationMatcher as IntegrationMatcher, ble_device_matches as ble_device_matches
from .models import HaBleakScanner as HaBleakScanner, HaBleakScannerWrapper as HaBleakScannerWrapper
from .usage import install_multiple_bleak_catcher as install_multiple_bleak_catcher, uninstall_multiple_bleak_catcher as uninstall_multiple_bleak_catcher
from .util import async_get_bluetooth_adapters as async_get_bluetooth_adapters
from _typeshed import Incomplete
from bleak.backends.device import BLEDevice as BLEDevice
from bleak.backends.scanner import AdvertisementData as AdvertisementData
from collections.abc import Callable
from datetime import datetime
from enum import Enum
from homeassistant import config_entries as config_entries
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import discovery_flow as discovery_flow
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.service_info.bluetooth import BluetoothServiceInfo as BluetoothServiceInfo
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import async_get_bluetooth as async_get_bluetooth
from homeassistant.util.package import is_docker_env as is_docker_env
from typing import Final

_LOGGER: Incomplete
UNAVAILABLE_TRACK_SECONDS: Final[Incomplete]
START_TIMEOUT: int
SOURCE_LOCAL: Final[str]
SCANNER_WATCHDOG_TIMEOUT: Final[Incomplete]
SCANNER_WATCHDOG_INTERVAL: Final[Incomplete]
MONOTONIC_TIME = time.monotonic

class BluetoothServiceInfoBleak(BluetoothServiceInfo):
    device: BLEDevice
    advertisement: AdvertisementData
    @classmethod
    def from_advertisement(cls, device: BLEDevice, advertisement_data: AdvertisementData, source: str) -> BluetoothServiceInfoBleak: ...
    def __init__(self, *, device, advertisement, **) -> None: ...

class BluetoothScanningMode(Enum):
    PASSIVE: str
    ACTIVE: str

SCANNING_MODE_TO_BLEAK: Incomplete
BluetoothChange: Incomplete
BluetoothCallback = Callable[[BluetoothServiceInfoBleak, BluetoothChange], None]
ProcessAdvertisementCallback = Callable[[BluetoothServiceInfoBleak], bool]

def async_get_scanner(hass: HomeAssistant) -> HaBleakScannerWrapper: ...
def async_discovered_service_info(hass: HomeAssistant) -> list[BluetoothServiceInfoBleak]: ...
def async_ble_device_from_address(hass: HomeAssistant, address: str) -> Union[BLEDevice, None]: ...
def async_address_present(hass: HomeAssistant, address: str) -> bool: ...
def async_register_callback(hass: HomeAssistant, callback: BluetoothCallback, match_dict: Union[BluetoothCallbackMatcher, None], mode: BluetoothScanningMode) -> Callable[[], None]: ...
async def async_process_advertisements(hass: HomeAssistant, callback: ProcessAdvertisementCallback, match_dict: BluetoothCallbackMatcher, mode: BluetoothScanningMode, timeout: int) -> BluetoothServiceInfoBleak: ...
def async_track_unavailable(hass: HomeAssistant, callback: Callable[[str], None], address: str) -> Callable[[], None]: ...
async def _async_has_bluetooth_adapter() -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: config_entries.ConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry) -> bool: ...

class BluetoothManager:
    hass: Incomplete
    _integration_matcher: Incomplete
    scanner: Incomplete
    start_stop_lock: Incomplete
    _cancel_device_detected: Incomplete
    _cancel_unavailable_tracking: Incomplete
    _cancel_stop: Incomplete
    _cancel_watchdog: Incomplete
    _unavailable_callbacks: Incomplete
    _callbacks: Incomplete
    _last_detection: float
    _reloading: bool
    _adapter: Incomplete
    _scanning_mode: Incomplete
    def __init__(self, hass: HomeAssistant, integration_matcher: IntegrationMatcher) -> None: ...
    def async_setup(self) -> None: ...
    def async_get_scanner(self) -> HaBleakScannerWrapper: ...
    def async_start_reload(self) -> None: ...
    async def async_start(self, scanning_mode: BluetoothScanningMode, adapter: Union[str, None]) -> None: ...
    def _async_setup_scanner_watchdog(self) -> None: ...
    async def _async_scanner_watchdog(self, now: datetime) -> None: ...
    def async_setup_unavailable_tracking(self) -> None: ...
    def _device_detected(self, device: BLEDevice, advertisement_data: AdvertisementData) -> None: ...
    def async_track_unavailable(self, callback: Callable[[str], None], address: str) -> Callable[[], None]: ...
    def async_register_callback(self, callback: BluetoothCallback, matcher: Union[BluetoothCallbackMatcher, None] = ...) -> Callable[[], None]: ...
    def async_ble_device_from_address(self, address: str) -> Union[BLEDevice, None]: ...
    def async_address_present(self, address: str) -> bool: ...
    def async_discovered_service_info(self) -> list[BluetoothServiceInfoBleak]: ...
    async def _async_hass_stopping(self, event: Event) -> None: ...
    def _async_cancel_scanner_callback(self) -> None: ...
    async def async_stop(self) -> None: ...