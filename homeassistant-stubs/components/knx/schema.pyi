from .const import CONF_INVERT as CONF_INVERT, CONF_RESET_AFTER as CONF_RESET_AFTER, CONF_STATE_ADDRESS as CONF_STATE_ADDRESS, CONF_SYNC_STATE as CONF_SYNC_STATE, CONTROLLER_MODES as CONTROLLER_MODES, ColorTempModes as ColorTempModes, KNX_ADDRESS as KNX_ADDRESS, PRESET_MODES as PRESET_MODES
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE
from typing import Any

def ga_validator(value: Any) -> Union[str, int]: ...

ga_list_validator: Any
ia_validator: Any
sync_state_validator: Any
sensor_type_validator: Any

class ConnectionSchema:
    CONF_KNX_LOCAL_IP: str = ...
    CONF_KNX_ROUTE_BACK: str = ...
    TUNNELING_SCHEMA: Any = ...
    ROUTING_SCHEMA: Any = ...

class BinarySensorSchema:
    CONF_STATE_ADDRESS: Any = ...
    CONF_SYNC_STATE: Any = ...
    CONF_INVERT: Any = ...
    CONF_IGNORE_INTERNAL_STATE: str = ...
    CONF_CONTEXT_TIMEOUT: str = ...
    CONF_RESET_AFTER: Any = ...
    DEFAULT_NAME: str = ...
    SCHEMA: Any = ...

class ClimateSchema:
    CONF_SETPOINT_SHIFT_ADDRESS: str = ...
    CONF_SETPOINT_SHIFT_STATE_ADDRESS: str = ...
    CONF_SETPOINT_SHIFT_MODE: str = ...
    CONF_SETPOINT_SHIFT_MAX: str = ...
    CONF_SETPOINT_SHIFT_MIN: str = ...
    CONF_TEMPERATURE_ADDRESS: str = ...
    CONF_TEMPERATURE_STEP: str = ...
    CONF_TARGET_TEMPERATURE_ADDRESS: str = ...
    CONF_TARGET_TEMPERATURE_STATE_ADDRESS: str = ...
    CONF_OPERATION_MODE_ADDRESS: str = ...
    CONF_OPERATION_MODE_STATE_ADDRESS: str = ...
    CONF_CONTROLLER_STATUS_ADDRESS: str = ...
    CONF_CONTROLLER_STATUS_STATE_ADDRESS: str = ...
    CONF_CONTROLLER_MODE_ADDRESS: str = ...
    CONF_CONTROLLER_MODE_STATE_ADDRESS: str = ...
    CONF_HEAT_COOL_ADDRESS: str = ...
    CONF_HEAT_COOL_STATE_ADDRESS: str = ...
    CONF_OPERATION_MODE_FROST_PROTECTION_ADDRESS: str = ...
    CONF_OPERATION_MODE_NIGHT_ADDRESS: str = ...
    CONF_OPERATION_MODE_COMFORT_ADDRESS: str = ...
    CONF_OPERATION_MODE_STANDBY_ADDRESS: str = ...
    CONF_OPERATION_MODES: str = ...
    CONF_CONTROLLER_MODES: str = ...
    CONF_ON_OFF_ADDRESS: str = ...
    CONF_ON_OFF_STATE_ADDRESS: str = ...
    CONF_ON_OFF_INVERT: str = ...
    CONF_MIN_TEMP: str = ...
    CONF_MAX_TEMP: str = ...
    CONF_CREATE_TEMPERATURE_SENSORS: str = ...
    DEFAULT_NAME: str = ...
    DEFAULT_SETPOINT_SHIFT_MODE: str = ...
    DEFAULT_SETPOINT_SHIFT_MAX: int = ...
    DEFAULT_SETPOINT_SHIFT_MIN: int = ...
    DEFAULT_TEMPERATURE_STEP: float = ...
    DEFAULT_ON_OFF_INVERT: bool = ...
    SCHEMA: Any = ...

class CoverSchema:
    CONF_MOVE_LONG_ADDRESS: str = ...
    CONF_MOVE_SHORT_ADDRESS: str = ...
    CONF_STOP_ADDRESS: str = ...
    CONF_POSITION_ADDRESS: str = ...
    CONF_POSITION_STATE_ADDRESS: str = ...
    CONF_ANGLE_ADDRESS: str = ...
    CONF_ANGLE_STATE_ADDRESS: str = ...
    CONF_TRAVELLING_TIME_DOWN: str = ...
    CONF_TRAVELLING_TIME_UP: str = ...
    CONF_INVERT_POSITION: str = ...
    CONF_INVERT_ANGLE: str = ...
    DEFAULT_TRAVEL_TIME: int = ...
    DEFAULT_NAME: str = ...
    SCHEMA: Any = ...

class ExposeSchema:
    CONF_KNX_EXPOSE_TYPE: Any = ...
    CONF_KNX_EXPOSE_ATTRIBUTE: str = ...
    CONF_KNX_EXPOSE_DEFAULT: str = ...
    EXPOSE_TIME_TYPES: Any = ...
    EXPOSE_TIME_SCHEMA: Any = ...
    EXPOSE_SENSOR_SCHEMA: Any = ...
    SCHEMA: Any = ...

class FanSchema:
    CONF_STATE_ADDRESS: Any = ...
    CONF_OSCILLATION_ADDRESS: str = ...
    CONF_OSCILLATION_STATE_ADDRESS: str = ...
    CONF_MAX_STEP: str = ...
    DEFAULT_NAME: str = ...
    SCHEMA: Any = ...

class LightSchema:
    CONF_STATE_ADDRESS: Any = ...
    CONF_BRIGHTNESS_ADDRESS: str = ...
    CONF_BRIGHTNESS_STATE_ADDRESS: str = ...
    CONF_COLOR_ADDRESS: str = ...
    CONF_COLOR_STATE_ADDRESS: str = ...
    CONF_COLOR_TEMP_ADDRESS: str = ...
    CONF_COLOR_TEMP_STATE_ADDRESS: str = ...
    CONF_COLOR_TEMP_MODE: str = ...
    CONF_RGBW_ADDRESS: str = ...
    CONF_RGBW_STATE_ADDRESS: str = ...
    CONF_MIN_KELVIN: str = ...
    CONF_MAX_KELVIN: str = ...
    DEFAULT_NAME: str = ...
    DEFAULT_COLOR_TEMP_MODE: str = ...
    DEFAULT_MIN_KELVIN: int = ...
    DEFAULT_MAX_KELVIN: int = ...
    CONF_INDIVIDUAL_COLORS: str = ...
    CONF_RED: str = ...
    CONF_GREEN: str = ...
    CONF_BLUE: str = ...
    CONF_WHITE: str = ...
    COLOR_SCHEMA: Any = ...
    SCHEMA: Any = ...

class NotifySchema:
    DEFAULT_NAME: str = ...
    SCHEMA: Any = ...

class SceneSchema:
    CONF_SCENE_NUMBER: str = ...
    DEFAULT_NAME: str = ...
    SCHEMA: Any = ...

class SensorSchema:
    CONF_ALWAYS_CALLBACK: str = ...
    CONF_STATE_ADDRESS: Any = ...
    CONF_SYNC_STATE: Any = ...
    DEFAULT_NAME: str = ...
    SCHEMA: Any = ...

class SwitchSchema:
    CONF_INVERT: Any = ...
    CONF_STATE_ADDRESS: Any = ...
    DEFAULT_NAME: str = ...
    SCHEMA: Any = ...

class WeatherSchema:
    CONF_SYNC_STATE: Any = ...
    CONF_KNX_TEMPERATURE_ADDRESS: str = ...
    CONF_KNX_BRIGHTNESS_SOUTH_ADDRESS: str = ...
    CONF_KNX_BRIGHTNESS_EAST_ADDRESS: str = ...
    CONF_KNX_BRIGHTNESS_WEST_ADDRESS: str = ...
    CONF_KNX_BRIGHTNESS_NORTH_ADDRESS: str = ...
    CONF_KNX_WIND_SPEED_ADDRESS: str = ...
    CONF_KNX_WIND_BEARING_ADDRESS: str = ...
    CONF_KNX_RAIN_ALARM_ADDRESS: str = ...
    CONF_KNX_FROST_ALARM_ADDRESS: str = ...
    CONF_KNX_WIND_ALARM_ADDRESS: str = ...
    CONF_KNX_DAY_NIGHT_ADDRESS: str = ...
    CONF_KNX_AIR_PRESSURE_ADDRESS: str = ...
    CONF_KNX_HUMIDITY_ADDRESS: str = ...
    CONF_KNX_CREATE_SENSORS: str = ...
    DEFAULT_NAME: str = ...
    SCHEMA: Any = ...
