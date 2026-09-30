from . import CoverEntity as CoverEntity
from _typeshed import Incomplete
from enum import IntFlag, StrEnum
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[CoverEntity]]
ATTR_CURRENT_POSITION: str
ATTR_CURRENT_TILT_POSITION: str
ATTR_IS_CLOSED: str
ATTR_POSITION: str
ATTR_SPEED: str
ATTR_TILT_POSITION: str

class CoverEntityCapabilityAttribute(StrEnum):
    SUPPORTED_SPEEDS = 'supported_speeds'

class CoverEntityStateAttribute(StrEnum):
    IS_CLOSED = 'is_closed'
    CURRENT_POSITION = 'current_position'
    CURRENT_TILT_POSITION = 'current_tilt_position'

INTENT_OPEN_COVER: str
INTENT_CLOSE_COVER: str

class CoverEntityFeature(IntFlag):
    OPEN = 1
    CLOSE = 2
    SET_POSITION = 4
    STOP = 8
    OPEN_TILT = 16
    CLOSE_TILT = 32
    STOP_TILT = 64
    SET_TILT_POSITION = 128
    SPEED = 256

class CoverState(StrEnum):
    CLOSED = 'closed'
    CLOSING = 'closing'
    OPEN = 'open'
    OPENING = 'opening'

class CoverDeviceClass(StrEnum):
    AWNING = 'awning'
    BLIND = 'blind'
    CURTAIN = 'curtain'
    DAMPER = 'damper'
    DOOR = 'door'
    GARAGE = 'garage'
    GATE = 'gate'
    SHADE = 'shade'
    SHUTTER = 'shutter'
    WINDOW = 'window'

DEVICE_CLASSES_SCHEMA: Incomplete
