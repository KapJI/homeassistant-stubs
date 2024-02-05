from _typeshed import Incomplete
from enum import IntFlag, StrEnum
from homeassistant.helpers.deprecation import DeprecatedConstant as DeprecatedConstant, DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants

MODE_NORMAL: str
MODE_ECO: str
MODE_AWAY: str
MODE_BOOST: str
MODE_COMFORT: str
MODE_HOME: str
MODE_SLEEP: str
MODE_AUTO: str
MODE_BABY: str

class HumidifierAction(StrEnum):
    HUMIDIFYING: str
    DRYING: str
    IDLE: str
    OFF: str

ATTR_ACTION: str
ATTR_AVAILABLE_MODES: str
ATTR_CURRENT_HUMIDITY: str
ATTR_HUMIDITY: str
ATTR_MAX_HUMIDITY: str
ATTR_MIN_HUMIDITY: str
DEFAULT_MIN_HUMIDITY: int
DEFAULT_MAX_HUMIDITY: int
DOMAIN: str
_DEPRECATED_DEVICE_CLASS_HUMIDIFIER: Incomplete
_DEPRECATED_DEVICE_CLASS_DEHUMIDIFIER: Incomplete
SERVICE_SET_MODE: str
SERVICE_SET_HUMIDITY: str

class HumidifierEntityFeature(IntFlag):
    MODES: int

_DEPRECATED_SUPPORT_MODES: Incomplete
__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
