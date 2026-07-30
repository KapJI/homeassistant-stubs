from enum import StrEnum

DOMAIN: str

class PersonEntityStateAttribute(StrEnum):
    EDITABLE = 'editable'
    ID = 'id'
    DEVICE_TRACKERS = 'device_trackers'
    IN_ZONES = 'in_zones'
    GPS_ACCURACY = 'gps_accuracy'
    SOURCE = 'source'
    USER_ID = 'user_id'
