from _typeshed import Incomplete
from typing import Final, TypedDict

DOMAIN: str
CONF_ADAPTER: str
CONF_DETAILS: str
CONF_PASSIVE: str
WINDOWS_DEFAULT_BLUETOOTH_ADAPTER: str
MACOS_DEFAULT_BLUETOOTH_ADAPTER: str
UNIX_DEFAULT_BLUETOOTH_ADAPTER: str
DEFAULT_ADAPTER_BY_PLATFORM: Incomplete
DEFAULT_ADDRESS: Final[str]
SOURCE_LOCAL: Final[str]
DATA_MANAGER: Final[str]
UNAVAILABLE_TRACK_SECONDS: Final[Incomplete]
START_TIMEOUT: int
FALLBACK_MAXIMUM_STALE_ADVERTISEMENT_SECONDS: Final[Incomplete]
SCANNER_WATCHDOG_TIMEOUT: Final[int]
SCANNER_WATCHDOG_INTERVAL: Final[Incomplete]

class AdapterDetails(TypedDict):
    address: str
    sw_version: str
    hw_version: Union[str, None]
    passive_scan: bool

ADAPTER_ADDRESS: Final[str]
ADAPTER_SW_VERSION: Final[str]
ADAPTER_HW_VERSION: Final[str]
ADAPTER_PASSIVE_SCAN: Final[str]
