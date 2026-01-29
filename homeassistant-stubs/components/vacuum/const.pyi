from . import StateVacuumEntity as StateVacuumEntity
from enum import IntFlag, StrEnum
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey

DOMAIN: str
DATA_COMPONENT: HassKey[EntityComponent[StateVacuumEntity]]

class VacuumActivity(StrEnum):
    CLEANING = 'cleaning'
    DOCKED = 'docked'
    IDLE = 'idle'
    PAUSED = 'paused'
    RETURNING = 'returning'
    ERROR = 'error'

class VacuumEntityFeature(IntFlag):
    TURN_ON = 1
    TURN_OFF = 2
    PAUSE = 4
    STOP = 8
    RETURN_HOME = 16
    FAN_SPEED = 32
    BATTERY = 64
    STATUS = 128
    SEND_COMMAND = 256
    LOCATE = 512
    CLEAN_SPOT = 1024
    MAP = 2048
    STATE = 4096
    START = 8192
