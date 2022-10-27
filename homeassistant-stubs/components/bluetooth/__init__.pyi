from .const import FALLBACK_MAXIMUM_STALE_ADVERTISEMENT_SECONDS as FALLBACK_MAXIMUM_STALE_ADVERTISEMENT_SECONDS, SOURCE_LOCAL as SOURCE_LOCAL
from .match import BluetoothCallbackMatcher
from .models import BaseHaScanner as BaseHaScanner, BluetoothCallback as BluetoothCallback, BluetoothScanningMode as BluetoothScanningMode, BluetoothServiceInfo as BluetoothServiceInfo, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak, HaBleakScannerWrapper, HaBluetoothConnector as HaBluetoothConnector, ProcessAdvertisementCallback
from bleak.backends.device import BLEDevice
from collections.abc import Callable, Iterable
from homeassistant.core import CALLBACK_TYPE, HomeAssistant

def async_get_scanner(hass: HomeAssistant) -> HaBleakScannerWrapper: ...
def async_scanner_count(hass: HomeAssistant, connectable: bool = ...) -> int: ...
def async_discovered_service_info(hass: HomeAssistant, connectable: bool = ...) -> Iterable[BluetoothServiceInfoBleak]: ...
def async_last_service_info(hass: HomeAssistant, address: str, connectable: bool = ...) -> Union[BluetoothServiceInfoBleak, None]: ...
def async_ble_device_from_address(hass: HomeAssistant, address: str, connectable: bool = ...) -> Union[BLEDevice, None]: ...
def async_register_callback(hass: HomeAssistant, callback: BluetoothCallback, match_dict: Union[BluetoothCallbackMatcher, None], mode: BluetoothScanningMode) -> Callable[[], None]: ...
async def async_process_advertisements(hass: HomeAssistant, callback: ProcessAdvertisementCallback, match_dict: BluetoothCallbackMatcher, mode: BluetoothScanningMode, timeout: int) -> BluetoothServiceInfoBleak: ...
def async_track_unavailable(hass: HomeAssistant, callback: Callable[[BluetoothServiceInfoBleak], None], address: str, connectable: bool = ...) -> Callable[[], None]: ...
def async_rediscover_address(hass: HomeAssistant, address: str) -> None: ...
def async_register_scanner(hass: HomeAssistant, scanner: BaseHaScanner, connectable: bool) -> CALLBACK_TYPE: ...
