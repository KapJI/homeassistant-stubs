from _typeshed import Incomplete
from enum import IntFlag, StrEnum

class HVACMode(StrEnum):
    OFF = 'off'
    HEAT = 'heat'
    COOL = 'cool'
    HEAT_COOL = 'heat_cool'
    AUTO = 'auto'
    DRY = 'dry'
    FAN_ONLY = 'fan_only'

HVAC_MODES: Incomplete
PRESET_NONE: str
PRESET_ECO: str
PRESET_AWAY: str
PRESET_BOOST: str
PRESET_COMFORT: str
PRESET_HOME: str
PRESET_SLEEP: str
PRESET_ACTIVITY: str
FAN_ON: str
FAN_OFF: str
FAN_AUTO: str
FAN_LOW: str
FAN_MEDIUM: str
FAN_HIGH: str
FAN_TOP: str
FAN_MIDDLE: str
FAN_FOCUS: str
FAN_DIFFUSE: str
SWING_ON: str
SWING_OFF: str
SWING_BOTH: str
SWING_VERTICAL: str
SWING_HORIZONTAL: str
SWING_HORIZONTAL_ON: str
SWING_HORIZONTAL_OFF: str

class HVACAction(StrEnum):
    COOLING = 'cooling'
    DEFROSTING = 'defrosting'
    DRYING = 'drying'
    FAN = 'fan'
    HEATING = 'heating'
    IDLE = 'idle'
    OFF = 'off'
    PREHEATING = 'preheating'

CURRENT_HVAC_ACTIONS: Incomplete
ATTR_AUX_HEAT: str
ATTR_CURRENT_HUMIDITY: str
ATTR_CURRENT_TEMPERATURE: str
ATTR_FAN_MODES: str
ATTR_FAN_MODE: str
ATTR_PRESET_MODE: str
ATTR_PRESET_MODES: str
ATTR_HUMIDITY: str
ATTR_MAX_HUMIDITY: str
ATTR_MIN_HUMIDITY: str
ATTR_MAX_TEMP: str
ATTR_MIN_TEMP: str
ATTR_HVAC_ACTION: str
ATTR_HVAC_MODES: str
ATTR_HVAC_MODE: str
ATTR_SWING_MODES: str
ATTR_SWING_MODE: str
ATTR_SWING_HORIZONTAL_MODE: str
ATTR_SWING_HORIZONTAL_MODES: str
ATTR_TARGET_TEMP_HIGH: str
ATTR_TARGET_TEMP_LOW: str
ATTR_TARGET_TEMP_STEP: str
DEFAULT_MIN_TEMP: int
DEFAULT_MAX_TEMP: int
DEFAULT_MIN_HUMIDITY: int
DEFAULT_MAX_HUMIDITY: int
DOMAIN: str
INTENT_SET_TEMPERATURE: str
SERVICE_SET_AUX_HEAT: str
SERVICE_SET_FAN_MODE: str
SERVICE_SET_PRESET_MODE: str
SERVICE_SET_HUMIDITY: str
SERVICE_SET_HVAC_MODE: str
SERVICE_SET_SWING_MODE: str
SERVICE_SET_SWING_HORIZONTAL_MODE: str
SERVICE_SET_TEMPERATURE: str

class ClimateEntityFeature(IntFlag):
    TARGET_TEMPERATURE = 1
    TARGET_TEMPERATURE_RANGE = 2
    TARGET_HUMIDITY = 4
    FAN_MODE = 8
    PRESET_MODE = 16
    SWING_MODE = 32
    AUX_HEAT = 64
    TURN_OFF = 128
    TURN_ON = 256
    SWING_HORIZONTAL_MODE = 512
