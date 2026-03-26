from enum import IntFlag, StrEnum

DOMAIN: str
ATTR_CURRENT_POSITION: str
ATTR_CURRENT_TILT_POSITION: str
ATTR_IS_CLOSED: str
ATTR_POSITION: str
ATTR_TILT_POSITION: str
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
