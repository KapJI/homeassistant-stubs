from enum import StrEnum

DOMAIN: str
ATTR_EVENT_TYPE: str
ATTR_EVENT_TYPES: str
ATTR_MULTI_PRESS_COUNT: str

class EventEntityCapabilityAttribute(StrEnum):
    EVENT_TYPES = 'event_types'

class EventEntityStateAttribute(StrEnum):
    EVENT_TYPE = 'event_type'

class DoorbellEventType(StrEnum):
    RING = 'ring'

class ButtonEventType(StrEnum):
    PRESS_START = 'press_start'
    PRESS_END = 'press_end'
    LONG_PRESS_START = 'long_press_start'
    LONG_PRESS_END = 'long_press_end'
    MULTI_PRESS_ONGOING = 'multi_press_ongoing'
    MULTI_PRESS_END = 'multi_press_end'
