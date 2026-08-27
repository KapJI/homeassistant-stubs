from enum import IntFlag, StrEnum
from typing import Final

class LawnMowerActivity(StrEnum):
    ERROR = 'error'
    PAUSED = 'paused'
    MOWING = 'mowing'
    DOCKED = 'docked'
    RETURNING = 'returning'

class LawnMowerEntityFeature(IntFlag):
    START_MOWING = 1
    PAUSE = 2
    DOCK = 4

DOMAIN: Final[str]
SERVICE_START_MOWING: str
SERVICE_PAUSE: str
SERVICE_DOCK: str
