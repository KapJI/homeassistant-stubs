from enum import StrEnum

CONF_PASSIVE: str
DOMAIN: str
HOME_ZONE: str

class ZoneEntityStateAttribute(StrEnum):
    RADIUS = 'radius'
    PASSIVE = 'passive'
    PERSONS = 'persons'
    DEVICE_TRACKERS = 'device_trackers'
    EDITABLE = 'editable'

ATTR_PASSIVE: str
ATTR_RADIUS: str
