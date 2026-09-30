from .entity import ValveEntity as ValveEntity
from _typeshed import Incomplete
from enum import IntFlag, StrEnum
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[ValveEntity]]
ATTR_POSITION: str

class ValveEntityStateAttribute(StrEnum):
    IS_CLOSED = 'is_closed'
    CURRENT_POSITION = 'current_position'

class ValveDeviceClass(StrEnum):
    WATER = 'water'
    GAS = 'gas'

class ValveEntityFeature(IntFlag):
    OPEN = 1
    CLOSE = 2
    SET_POSITION = 4
    STOP = 8

class ValveState(StrEnum):
    OPENING = 'opening'
    CLOSING = 'closing'
    CLOSED = 'closed'
    OPEN = 'open'

DEVICE_CLASSES_SCHEMA: Incomplete
