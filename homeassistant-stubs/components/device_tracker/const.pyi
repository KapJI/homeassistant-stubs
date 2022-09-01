from _typeshed import Incomplete
from homeassistant.backports.enum import StrEnum as StrEnum
from typing import Final

LOGGER: Final[Incomplete]
DOMAIN: Final[str]
ENTITY_ID_FORMAT: Final[Incomplete]
PLATFORM_TYPE_LEGACY: Final[str]
PLATFORM_TYPE_ENTITY: Final[str]
SOURCE_TYPE_GPS: Final[str]
SOURCE_TYPE_ROUTER: Final[str]
SOURCE_TYPE_BLUETOOTH: Final[str]
SOURCE_TYPE_BLUETOOTH_LE: Final[str]

class SourceType(StrEnum):
    GPS: str
    ROUTER: str
    BLUETOOTH: str
    BLUETOOTH_LE: str

CONF_SCAN_INTERVAL: Final[str]
SCAN_INTERVAL: Final[Incomplete]
CONF_TRACK_NEW: Final[str]
DEFAULT_TRACK_NEW: Final[bool]
CONF_CONSIDER_HOME: Final[str]
DEFAULT_CONSIDER_HOME: Final[Incomplete]
CONF_NEW_DEVICE_DEFAULTS: Final[str]
ATTR_ATTRIBUTES: Final[str]
ATTR_BATTERY: Final[str]
ATTR_DEV_ID: Final[str]
ATTR_GPS: Final[str]
ATTR_HOST_NAME: Final[str]
ATTR_LOCATION_NAME: Final[str]
ATTR_MAC: Final[str]
ATTR_SOURCE_TYPE: Final[str]
ATTR_CONSIDER_HOME: Final[str]
ATTR_IP: Final[str]
CONNECTED_DEVICE_REGISTERED: Final[str]
