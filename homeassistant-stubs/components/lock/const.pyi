from enum import StrEnum
from typing import Final

DOMAIN: Final[str]

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
