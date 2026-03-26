from . import EvoData as EvoData
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
EVOHOME_DATA: HassKey[EvoData]
STORAGE_VER: Final[int]
STORAGE_KEY: Final[Incomplete]
CONF_LOCATION_IDX: Final[str]
USER_DATA: Final[str]
SCAN_INTERVAL_DEFAULT: Final[Incomplete]
SCAN_INTERVAL_MINIMUM: Final[Incomplete]
ATTR_PERIOD: Final[str]
ATTR_DURATION: Final[str]
ATTR_SETPOINT: Final[str]

class EvoService(StrEnum):
    REFRESH_SYSTEM = 'refresh_system'
    SET_SYSTEM_MODE = 'set_system_mode'
    RESET_SYSTEM = 'reset_system'
    SET_ZONE_OVERRIDE = 'set_zone_override'
    CLEAR_ZONE_OVERRIDE = 'clear_zone_override'
