from _typeshed import Incomplete
from enum import Enum
from typing import Final

DOMAIN: Final[str]
ENTRY_TITLE: str
DEFAULT_SCAN_INTERVAL: Incomplete
SENSOR_KIND_TEMPERATURE: str
SENSOR_KIND_HUMIDITY: str
SENSOR_KIND_BATTERY: str
VACUUM_FAN_SPEED_QUIET: str
VACUUM_FAN_SPEED_STANDARD: str
VACUUM_FAN_SPEED_STRONG: str
VACUUM_FAN_SPEED_MAX: str
AFTER_COMMAND_REFRESH: int
COVER_ENTITY_AFTER_COMMAND_REFRESH: int

class AirPurifierMode(Enum):
    NORMAL = 1
    AUTO = 2
    SLEEP = 3
    PET = 4
    @classmethod
    def get_modes(cls) -> list[str]: ...
