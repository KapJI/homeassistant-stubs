from enum import IntFlag, StrEnum

class LawnMowerActivity(StrEnum):
    ERROR: str
    PAUSED: str
    MOWING: str
    DOCKED: str

class LawnMowerEntityFeature(IntFlag):
    START_MOWING: int
    PAUSE: int
    DOCK: int

DOMAIN: str
SERVICE_START_MOWING: str
SERVICE_PAUSE: str
SERVICE_DOCK: str
