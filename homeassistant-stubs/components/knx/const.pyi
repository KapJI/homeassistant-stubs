from enum import Enum
from homeassistant.components.climate.const import HVAC_MODE_AUTO as HVAC_MODE_AUTO, HVAC_MODE_COOL as HVAC_MODE_COOL, HVAC_MODE_DRY as HVAC_MODE_DRY, HVAC_MODE_FAN_ONLY as HVAC_MODE_FAN_ONLY, HVAC_MODE_HEAT as HVAC_MODE_HEAT, HVAC_MODE_OFF as HVAC_MODE_OFF, PRESET_AWAY as PRESET_AWAY, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO, PRESET_NONE as PRESET_NONE, PRESET_SLEEP as PRESET_SLEEP
from typing import Any

DOMAIN: str
KNX_ADDRESS: str
CONF_INVERT: str
CONF_STATE_ADDRESS: str
CONF_SYNC_STATE: str
CONF_RESET_AFTER: str
ATTR_COUNTER: str

class ColorTempModes(Enum):
    ABSOLUTE: str = ...
    RELATIVE: str = ...

class SupportedPlatforms(Enum):
    BINARY_SENSOR: str = ...
    CLIMATE: str = ...
    COVER: str = ...
    FAN: str = ...
    LIGHT: str = ...
    NOTIFY: str = ...
    SCENE: str = ...
    SENSOR: str = ...
    SWITCH: str = ...
    WEATHER: str = ...

CONTROLLER_MODES: Any
PRESET_MODES: Any