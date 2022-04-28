from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass
from homeassistant.components.climate.const import FAN_AUTO as FAN_AUTO, FAN_HIGH as FAN_HIGH, FAN_MEDIUM as FAN_MEDIUM, FAN_ON as FAN_ON, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_AWAY as PRESET_AWAY, PRESET_BOOST as PRESET_BOOST
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, CURRENCY_CENT as CURRENCY_CENT, CURRENCY_DOLLAR as CURRENCY_DOLLAR, DEGREE as DEGREE, ELECTRIC_CURRENT_MILLIAMPERE as ELECTRIC_CURRENT_MILLIAMPERE, ELECTRIC_POTENTIAL_MILLIVOLT as ELECTRIC_POTENTIAL_MILLIVOLT, ELECTRIC_POTENTIAL_VOLT as ELECTRIC_POTENTIAL_VOLT, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, ENERGY_WATT_HOUR as ENERGY_WATT_HOUR, FREQUENCY_HERTZ as FREQUENCY_HERTZ, IRRADIATION_WATTS_PER_SQUARE_METER as IRRADIATION_WATTS_PER_SQUARE_METER, LENGTH_CENTIMETERS as LENGTH_CENTIMETERS, LENGTH_FEET as LENGTH_FEET, LENGTH_INCHES as LENGTH_INCHES, LENGTH_KILOMETERS as LENGTH_KILOMETERS, LENGTH_METERS as LENGTH_METERS, LENGTH_MILES as LENGTH_MILES, LENGTH_MILLIMETERS as LENGTH_MILLIMETERS, LIGHT_LUX as LIGHT_LUX, MASS_KILOGRAMS as MASS_KILOGRAMS, MASS_POUNDS as MASS_POUNDS, PERCENTAGE as PERCENTAGE, POWER_KILO_WATT as POWER_KILO_WATT, POWER_WATT as POWER_WATT, PRECIPITATION_MILLIMETERS_PER_HOUR as PRECIPITATION_MILLIMETERS_PER_HOUR, PRESSURE_HPA as PRESSURE_HPA, PRESSURE_INHG as PRESSURE_INHG, PRESSURE_MBAR as PRESSURE_MBAR, Platform as Platform, SERVICE_LOCK as SERVICE_LOCK, SERVICE_UNLOCK as SERVICE_UNLOCK, SOUND_PRESSURE_DB as SOUND_PRESSURE_DB, SOUND_PRESSURE_WEIGHTED_DBA as SOUND_PRESSURE_WEIGHTED_DBA, SPEED_INCHES_PER_DAY as SPEED_INCHES_PER_DAY, SPEED_INCHES_PER_HOUR as SPEED_INCHES_PER_HOUR, SPEED_KILOMETERS_PER_HOUR as SPEED_KILOMETERS_PER_HOUR, SPEED_METERS_PER_SECOND as SPEED_METERS_PER_SECOND, SPEED_MILES_PER_HOUR as SPEED_MILES_PER_HOUR, SPEED_MILLIMETERS_PER_DAY as SPEED_MILLIMETERS_PER_DAY, STATE_CLOSED as STATE_CLOSED, STATE_CLOSING as STATE_CLOSING, STATE_LOCKED as STATE_LOCKED, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_OPEN as STATE_OPEN, STATE_OPENING as STATE_OPENING, STATE_PROBLEM as STATE_PROBLEM, STATE_UNKNOWN as STATE_UNKNOWN, STATE_UNLOCKED as STATE_UNLOCKED, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT, TEMP_KELVIN as TEMP_KELVIN, TIME_DAYS as TIME_DAYS, TIME_HOURS as TIME_HOURS, TIME_MILLISECONDS as TIME_MILLISECONDS, TIME_MINUTES as TIME_MINUTES, TIME_MONTHS as TIME_MONTHS, TIME_SECONDS as TIME_SECONDS, TIME_YEARS as TIME_YEARS, UV_INDEX as UV_INDEX, VOLUME_CUBIC_FEET as VOLUME_CUBIC_FEET, VOLUME_CUBIC_METERS as VOLUME_CUBIC_METERS, VOLUME_FLOW_RATE_CUBIC_FEET_PER_MINUTE as VOLUME_FLOW_RATE_CUBIC_FEET_PER_MINUTE, VOLUME_FLOW_RATE_CUBIC_METERS_PER_HOUR as VOLUME_FLOW_RATE_CUBIC_METERS_PER_HOUR, VOLUME_GALLONS as VOLUME_GALLONS, VOLUME_LITERS as VOLUME_LITERS
from typing import Any

_LOGGER: Any
DOMAIN: str
MANUFACTURER: str
CONF_IGNORE_STRING: str
CONF_SENSOR_STRING: str
CONF_VAR_SENSOR_STRING: str
CONF_TLS_VER: str
CONF_RESTORE_LIGHT_STATE: str
DEFAULT_IGNORE_STRING: str
DEFAULT_SENSOR_STRING: str
DEFAULT_RESTORE_LIGHT_STATE: bool
DEFAULT_TLS_VERSION: float
DEFAULT_PROGRAM_STRING: str
DEFAULT_VAR_SENSOR_STRING: str
KEY_ACTIONS: str
KEY_STATUS: str
PLATFORMS: Any
PROGRAM_PLATFORMS: Any
SUPPORTED_BIN_SENS_CLASSES: Any
ISY_GROUP_PLATFORM: Any
ISY994_ISY: str
ISY994_NODES: str
ISY994_PROGRAMS: str
ISY994_VARIABLES: str
FILTER_UOM: str
FILTER_STATES: str
FILTER_NODE_DEF_ID: str
FILTER_INSTEON_TYPE: str
FILTER_ZWAVE_CAT: str
SUBNODE_CLIMATE_COOL: int
SUBNODE_CLIMATE_HEAT: int
SUBNODE_DUSK_DAWN: int
SUBNODE_EZIO2X4_SENSORS: Any
SUBNODE_FANLINC_LIGHT: int
SUBNODE_HEARTBEAT: int
SUBNODE_IOLINC_RELAY: int
SUBNODE_LOW_BATTERY: int
SUBNODE_MOTION_DISABLED: Any
SUBNODE_NEGATIVE: int
SUBNODE_TAMPER: Any
TYPE_CATEGORY_CONTROLLERS: str
TYPE_CATEGORY_DIMMABLE: str
TYPE_CATEGORY_SWITCHED: str
TYPE_CATEGORY_IRRIGATION: str
TYPE_CATEGORY_CLIMATE: str
TYPE_CATEGORY_POOL_CTL: str
TYPE_CATEGORY_SENSOR_ACTUATORS: str
TYPE_CATEGORY_ENERGY_MGMT: str
TYPE_CATEGORY_COVER: str
TYPE_CATEGORY_LOCK: str
TYPE_CATEGORY_SAFETY: str
TYPE_CATEGORY_X10: str
TYPE_EZIO2X4: str
TYPE_INSTEON_MOTION: Any
UDN_UUID_PREFIX: str
ISY_URL_POSTFIX: str
EVENTS_SUFFIX: str
UOM_ISYV4_DEGREES: str
UOM_ISYV4_NONE: str
UOM_ISY_CELSIUS: int
UOM_ISY_FAHRENHEIT: int
UOM_8_BIT_RANGE: str
UOM_BARRIER: str
UOM_DOUBLE_TEMP: str
UOM_HVAC_ACTIONS: str
UOM_HVAC_MODE_GENERIC: str
UOM_HVAC_MODE_INSTEON: str
UOM_FAN_MODES: str
UOM_INDEX: str
UOM_ON_OFF: str
UOM_PERCENTAGE: str
NODE_FILTERS: dict[Platform, dict[str, list[str]]]
UOM_FRIENDLY_NAME: Any
UOM_TO_STATES: Any
ISY_HVAC_MODES: Any
HA_HVAC_TO_ISY: Any
HA_FAN_TO_ISY: Any
BINARY_SENSOR_DEVICE_TYPES_ISY: Any
BINARY_SENSOR_DEVICE_TYPES_ZWAVE: Any
SCHEME_HTTP: str
HTTP_PORT: int
SCHEME_HTTPS: str
HTTPS_PORT: int
