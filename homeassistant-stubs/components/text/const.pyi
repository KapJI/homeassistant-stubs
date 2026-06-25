from enum import StrEnum

DOMAIN: str

class TextEntityCapabilityAttribute(StrEnum):
    MODE = 'mode'
    MIN = 'min'
    MAX = 'max'
    PATTERN = 'pattern'

ATTR_MAX: str
ATTR_MIN: str
ATTR_PATTERN: str
ATTR_VALUE: str
SERVICE_SET_VALUE: str
