from . import LawnMowerEntity as LawnMowerEntity
from enum import IntFlag, StrEnum
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[LawnMowerEntity]]

class LawnMowerActivity(StrEnum):
    ERROR = 'error'
    PAUSED = 'paused'
    MOWING = 'mowing'
    DOCKED = 'docked'
    RETURNING = 'returning'
    IDLE = 'idle'

class LawnMowerEntityFeature(IntFlag):
    START_MOWING = 1
    PAUSE = 2
    DOCK = 4
    STOP = 8

SERVICE_START_MOWING: str
SERVICE_PAUSE: str
SERVICE_DOCK: str
SERVICE_STOP: str
