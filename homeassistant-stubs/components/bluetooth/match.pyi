from _typeshed import Incomplete
from bleak.backends.device import BLEDevice as BLEDevice
from bleak.backends.scanner import AdvertisementData as AdvertisementData
from homeassistant.loader import BluetoothMatcher as BluetoothMatcher, BluetoothMatcherOptional as BluetoothMatcherOptional
from typing import Final, TypedDict

MAX_REMEMBER_ADDRESSES: Final[int]
ADDRESS: Final[str]
LOCAL_NAME: Final[str]
SERVICE_UUID: Final[str]
SERVICE_DATA_UUID: Final[str]
MANUFACTURER_ID: Final[str]
MANUFACTURER_DATA_START: Final[str]

class BluetoothCallbackMatcherOptional(TypedDict):
    address: str

class BluetoothCallbackMatcher(BluetoothMatcherOptional, BluetoothCallbackMatcherOptional): ...

class IntegrationMatchHistory:
    manufacturer_data: bool
    service_data: bool
    service_uuids: bool
    def __init__(self, manufacturer_data, service_data, service_uuids) -> None: ...

def seen_all_fields(previous_match: IntegrationMatchHistory, adv_data: AdvertisementData) -> bool: ...

class IntegrationMatcher:
    _integration_matchers: Incomplete
    _matched: Incomplete
    def __init__(self, integration_matchers: list[BluetoothMatcher]) -> None: ...
    def async_clear_history(self) -> None: ...
    def match_domains(self, device: BLEDevice, adv_data: AdvertisementData) -> set[str]: ...

def ble_device_matches(matcher: Union[BluetoothCallbackMatcher, BluetoothMatcher], device: BLEDevice, adv_data: AdvertisementData) -> bool: ...
