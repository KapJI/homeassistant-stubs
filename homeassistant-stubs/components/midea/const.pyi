from _typeshed import Incomplete
from enum import IntEnum

LOGGER: Incomplete
DOMAIN: str
CONF_KEY: str
CONF_SUBTYPE: str
CONF_ACCOUNT: str
CONF_SERVER: str
CONF_SN: str
PRESET_MODE_NONE: str

class FanSpeed(IntEnum):
    LOW = 20
    MEDIUM = 40
    HIGH = 60
    FULL_SPEED = 80
    AUTO = 100
