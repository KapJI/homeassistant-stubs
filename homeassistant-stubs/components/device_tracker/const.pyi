from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.helpers.deprecation import DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from homeassistant.util.signal_type import SignalType as SignalType
from typing import Final

LOGGER: Final[Incomplete]
DOMAIN: Final[str]
ENTITY_ID_FORMAT: Final[Incomplete]
PLATFORM_TYPE_LEGACY: Final[str]
PLATFORM_TYPE_ENTITY: Final[str]

class SourceType(StrEnum):
    GPS = 'gps'
    ROUTER = 'router'
    BLUETOOTH = 'bluetooth'
    BLUETOOTH_LE = 'bluetooth_le'

_DEPRECATED_SOURCE_TYPE_GPS: Final[Incomplete]
_DEPRECATED_SOURCE_TYPE_ROUTER: Final[Incomplete]
_DEPRECATED_SOURCE_TYPE_BLUETOOTH: Final[Incomplete]
_DEPRECATED_SOURCE_TYPE_BLUETOOTH_LE: Final[Incomplete]
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
CONNECTED_DEVICE_REGISTERED: Incomplete
__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
