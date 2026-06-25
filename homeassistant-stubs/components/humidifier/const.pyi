from enum import IntFlag, StrEnum

MODE_NORMAL: str
MODE_ECO: str
MODE_AWAY: str
MODE_BOOST: str
MODE_COMFORT: str
MODE_HOME: str
MODE_SLEEP: str
MODE_AUTO: str
MODE_BABY: str

class HumidifierAction(StrEnum):
    HUMIDIFYING = 'humidifying'
    DRYING = 'drying'
    IDLE = 'idle'
    OFF = 'off'

ATTR_ACTION: str
ATTR_AVAILABLE_MODES: str
ATTR_CURRENT_HUMIDITY: str
ATTR_HUMIDITY: str
ATTR_MAX_HUMIDITY: str
ATTR_MIN_HUMIDITY: str
ATTR_TARGET_HUMIDITY_STEP: str
DEFAULT_MIN_HUMIDITY: int
DEFAULT_MAX_HUMIDITY: int
DOMAIN: str
SERVICE_SET_MODE: str
SERVICE_SET_HUMIDITY: str

class HumidifierEntityCapabilityAttribute(StrEnum):
    MIN_HUMIDITY = 'min_humidity'
    MAX_HUMIDITY = 'max_humidity'
    TARGET_HUMIDITY_STEP = 'target_humidity_step'
    AVAILABLE_MODES = 'available_modes'

class HumidifierEntityStateAttribute(StrEnum):
    ACTION = 'action'
    CURRENT_HUMIDITY = 'current_humidity'
    HUMIDITY = 'humidity'
    MODE = 'mode'

class HumidifierEntityFeature(IntFlag):
    MODES = 1
