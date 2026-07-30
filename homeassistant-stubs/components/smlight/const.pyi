from _typeshed import Incomplete
from enum import StrEnum

DOMAIN: str
ATTR_MANUFACTURER: str
DATA_COORDINATOR: str
FIRMWARE_COORDINATOR: str
SCAN_FIRMWARE_INTERVAL: Incomplete
LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
SCAN_INTERNET_INTERVAL: Incomplete
UPTIME_DEVIATION: Incomplete
CONF_BLE_SCANNER_MODE: str

class BLEScannerMode(StrEnum):
    DISABLED = 'disabled'
    AUTO = 'auto'
    ACTIVE = 'active'
    PASSIVE = 'passive'

ZWAVE_TYPES: Incomplete
