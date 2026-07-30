from enum import StrEnum

DOMAIN: str
CONF_INFRARED_ENTITY_ID: str
CONF_INFRARED_RECEIVER_ENTITY_ID: str
CONF_DEVICE_TYPE: str

class LEDIrDeviceType(StrEnum):
    GENERIC_13_KEY = 'generic_13_key'
    GENERIC_24_KEY = 'generic_24_key'
    GENERIC_40_KEY = 'generic_40_key'
    GENERIC_44_KEY = 'generic_44_key'
