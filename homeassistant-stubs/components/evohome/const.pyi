from _typeshed import Incomplete
from enum import StrEnum
from typing import Final

DOMAIN: Final[str]
STORAGE_VER: Final[int]
STORAGE_KEY: Final[Incomplete]
CONF_LOCATION_IDX: Final[str]
USER_DATA: Final[str]
SCAN_INTERVAL_DEFAULT: Final[Incomplete]
SCAN_INTERVAL_MINIMUM: Final[Incomplete]
ATTR_PERIOD: Final[str]
ATTR_DURATION: Final[str]
ATTR_SETPOINT: Final[str]
ATTR_DURATION_UNTIL: Final[str]

class EvoService(StrEnum):
    REFRESH_SYSTEM = 'refresh_system'
    SET_SYSTEM_MODE = 'set_system_mode'
    RESET_SYSTEM = 'reset_system'
    SET_ZONE_OVERRIDE = 'set_zone_override'
    RESET_ZONE_OVERRIDE = 'clear_zone_override'
