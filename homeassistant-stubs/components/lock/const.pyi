from . import LockEntity as LockEntity
from enum import IntFlag, StrEnum
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Final

DOMAIN: Final[str]
DATA_COMPONENT: HassKey[EntityComponent[LockEntity]]

class LockEntityStateAttribute(StrEnum):
    CHANGED_BY = 'changed_by'
    CODE_FORMAT = 'code_format'

class LockState(StrEnum):
    JAMMED = 'jammed'
    OPENING = 'opening'
    LOCKING = 'locking'
    OPEN = 'open'
    UNLOCKING = 'unlocking'
    LOCKED = 'locked'
    UNLOCKED = 'unlocked'

class LockEntityFeature(IntFlag):
    OPEN = 1
