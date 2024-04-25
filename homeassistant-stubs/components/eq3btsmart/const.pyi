from _typeshed import Incomplete
from enum import Enum
from eq3btsmart.const import OperationMode
from homeassistant.components.climate import HVACMode as HVACMode, PRESET_AWAY as PRESET_AWAY, PRESET_BOOST as PRESET_BOOST, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO, PRESET_NONE as PRESET_NONE

DOMAIN: str
MANUFACTURER: str
DEVICE_MODEL: str
GET_DEVICE_TIMEOUT: int
EQ_TO_HA_HVAC: dict[OperationMode, HVACMode]
HA_TO_EQ_HVAC: Incomplete

class Preset(str, Enum):
    NONE = PRESET_NONE
    ECO = PRESET_ECO
    COMFORT = PRESET_COMFORT
    BOOST = PRESET_BOOST
    AWAY = PRESET_AWAY
    OPEN: str
    LOW_BATTERY: str
    WINDOW_OPEN: str

class CurrentTemperatureSelector(str, Enum):
    NOTHING: str
    UI: str
    DEVICE: str
    VALVE: str
    ENTITY: str

class TargetTemperatureSelector(str, Enum):
    TARGET: str
    LAST_REPORTED: str

DEFAULT_CURRENT_TEMP_SELECTOR: Incomplete
DEFAULT_TARGET_TEMP_SELECTOR: Incomplete
DEFAULT_SCAN_INTERVAL: int
SIGNAL_THERMOSTAT_DISCONNECTED: Incomplete
SIGNAL_THERMOSTAT_CONNECTED: Incomplete
