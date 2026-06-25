from enum import StrEnum

DOMAIN: str
ATTR_EVENT_TYPE: str
ATTR_EVENT_TYPES: str

class EventEntityCapabilityAttribute(StrEnum):
    EVENT_TYPES = 'event_types'

class EventEntityStateAttribute(StrEnum):
    EVENT_TYPE = 'event_type'

class DoorbellEventType(StrEnum):
    RING = 'ring'
