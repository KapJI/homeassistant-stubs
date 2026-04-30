from enum import StrEnum

DOMAIN: str
ATTR_EVENT_TYPE: str
ATTR_EVENT_TYPES: str

class DoorbellEventType(StrEnum):
    RING = 'ring'
