from enum import StrEnum

DOMAIN: str
CONF_INFRARED_ENTITY_ID: str
CONF_INFRARED_RECEIVER_ENTITY_ID: str
CONF_DEVICE_TYPE: str
CONF_HVAC_MODES: str

class LGDeviceType(StrEnum):
    TV = 'tv'
    AC = 'ac'
