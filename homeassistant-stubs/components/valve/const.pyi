from enum import IntFlag, StrEnum

DOMAIN: str

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
