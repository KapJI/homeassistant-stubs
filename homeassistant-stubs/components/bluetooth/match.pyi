import re
from .models import BluetoothCallback as BluetoothCallback, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from _typeshed import Incomplete
from bleak.backends.scanner import AdvertisementData as AdvertisementData
from dataclasses import dataclass
from homeassistant.core import callback as callback
from homeassistant.loader import BluetoothMatcher as BluetoothMatcher, BluetoothMatcherOptional as BluetoothMatcherOptional
from typing import Final, Generic, TypeVar, TypedDict

MAX_REMEMBER_ADDRESSES: Final[int]
CALLBACK: Final[str]
DOMAIN: Final[str]
ADDRESS: Final[str]
CONNECTABLE: Final[str]
LOCAL_NAME: Final[str]
SERVICE_UUID: Final[str]
SERVICE_DATA_UUID: Final[str]
MANUFACTURER_ID: Final[str]
MANUFACTURER_DATA_START: Final[str]
LOCAL_NAME_MIN_MATCH_LENGTH: int

class BluetoothCallbackMatcherOptional(TypedDict, total=False):
    address: str

class BluetoothCallbackMatcher(BluetoothMatcherOptional, BluetoothCallbackMatcherOptional): ...

class _BluetoothCallbackMatcherWithCallback(TypedDict):
    callback: BluetoothCallback

class BluetoothCallbackMatcherWithCallback(_BluetoothCallbackMatcherWithCallback, BluetoothCallbackMatcher): ...

@dataclass(slots=True, frozen=False)
class IntegrationMatchHistory:
    manufacturer_data: bool
    service_data: set[str]
    service_uuids: set[str]
    def __init__(self, manufacturer_data, service_data, service_uuids) -> None: ...

def seen_all_fields(previous_match: IntegrationMatchHistory, advertisement_data: AdvertisementData) -> bool: ...

class IntegrationMatcher:
    _integration_matchers: Incomplete
    _matched: Incomplete
    _matched_connectable: Incomplete
    _index: Incomplete
    def __init__(self, integration_matchers: list[BluetoothMatcher]) -> None: ...
    def async_setup(self) -> None: ...
    def async_clear_address(self, address: str) -> None: ...
    def match_domains(self, service_info: BluetoothServiceInfoBleak) -> set[str]: ...
_T = TypeVar('_T', BluetoothMatcher, BluetoothCallbackMatcherWithCallback)

class BluetoothMatcherIndexBase(Generic[_T]):
    local_name: Incomplete
    service_uuid: Incomplete
    service_data_uuid: Incomplete
    manufacturer_id: Incomplete
    service_uuid_set: Incomplete
    service_data_uuid_set: Incomplete
    manufacturer_id_set: Incomplete
    def __init__(self) -> None: ...
    def add(self, matcher: _T) -> bool: ...
    def remove(self, matcher: _T) -> bool: ...
    def build(self) -> None: ...
    def match(self, service_info: BluetoothServiceInfoBleak) -> list[_T]: ...

class BluetoothMatcherIndex(BluetoothMatcherIndexBase[BluetoothMatcher]): ...

class BluetoothCallbackMatcherIndex(BluetoothMatcherIndexBase[BluetoothCallbackMatcherWithCallback]):
    address: Incomplete
    connectable: Incomplete
    def __init__(self) -> None: ...
    def add_callback_matcher(self, matcher: BluetoothCallbackMatcherWithCallback) -> None: ...
    def remove_callback_matcher(self, matcher: BluetoothCallbackMatcherWithCallback) -> None: ...
    def match_callbacks(self, service_info: BluetoothServiceInfoBleak) -> list[BluetoothCallbackMatcherWithCallback]: ...

def _local_name_to_index_key(local_name: str) -> str: ...
def ble_device_matches(matcher: BluetoothMatcherOptional, service_info: BluetoothServiceInfoBleak) -> bool: ...
def _compile_fnmatch(pattern: str) -> re.Pattern: ...
def _memorized_fnmatch(name: str, pattern: str) -> bool: ...
