from .accessories import HomeAccessory as HomeAccessory, TYPES as TYPES
from .climate_base import HomeKitClimateAccessory as HomeKitClimateAccessory
from .climate_util import get_temperature_range_from_state as get_temperature_range_from_state, temperature_attribute_to_homekit as temperature_attribute_to_homekit
from .const import CHAR_COOLING_THRESHOLD_TEMPERATURE as CHAR_COOLING_THRESHOLD_TEMPERATURE, CHAR_CURRENT_FAN_STATE as CHAR_CURRENT_FAN_STATE, CHAR_CURRENT_HEATING_COOLING as CHAR_CURRENT_HEATING_COOLING, CHAR_CURRENT_HUMIDITY as CHAR_CURRENT_HUMIDITY, CHAR_CURRENT_TEMPERATURE as CHAR_CURRENT_TEMPERATURE, CHAR_HEATING_THRESHOLD_TEMPERATURE as CHAR_HEATING_THRESHOLD_TEMPERATURE, CHAR_ROTATION_SPEED as CHAR_ROTATION_SPEED, CHAR_SWING_MODE as CHAR_SWING_MODE, CHAR_TARGET_FAN_STATE as CHAR_TARGET_FAN_STATE, CHAR_TARGET_HEATING_COOLING as CHAR_TARGET_HEATING_COOLING, CHAR_TARGET_HUMIDITY as CHAR_TARGET_HUMIDITY, CHAR_TARGET_TEMPERATURE as CHAR_TARGET_TEMPERATURE, CHAR_TEMP_DISPLAY_UNITS as CHAR_TEMP_DISPLAY_UNITS, DEFAULT_MAX_TEMP_WATER_HEATER as DEFAULT_MAX_TEMP_WATER_HEATER, DEFAULT_MIN_TEMP_WATER_HEATER as DEFAULT_MIN_TEMP_WATER_HEATER, PROP_MAX_VALUE as PROP_MAX_VALUE, PROP_MIN_VALUE as PROP_MIN_VALUE, SERV_THERMOSTAT as SERV_THERMOSTAT
from .util import get_min_max as get_min_max, temperature_to_states as temperature_to_states
from _typeshed import Incomplete
from homeassistant.components.climate import ATTR_HUMIDITY as ATTR_HUMIDITY, ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntityCapabilityAttribute as ClimateEntityCapabilityAttribute, ClimateEntityFeature as ClimateEntityFeature, ClimateEntityStateAttribute as ClimateEntityStateAttribute, DEFAULT_MAX_HUMIDITY as DEFAULT_MAX_HUMIDITY, DEFAULT_MIN_HUMIDITY as DEFAULT_MIN_HUMIDITY, FAN_AUTO as FAN_AUTO, FAN_ON as FAN_ON, HVACAction as HVACAction, HVACMode as HVACMode, SERVICE_SET_HUMIDITY as SERVICE_SET_HUMIDITY
from homeassistant.components.water_heater import ATTR_OPERATION_MODE as ATTR_OPERATION_MODE, SERVICE_SET_OPERATION_MODE as SERVICE_SET_OPERATION_MODE, WaterHeaterCapabilityAttribute as WaterHeaterCapabilityAttribute, WaterHeaterEntityFeature as WaterHeaterEntityFeature, WaterHeaterStateAttribute as WaterHeaterStateAttribute
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_TEMPERATURE as ATTR_TEMPERATURE, EntityStateAttribute as EntityStateAttribute, PERCENTAGE as PERCENTAGE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_OFF as STATE_OFF, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import State as State, callback as callback
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from typing import Any, override

_LOGGER: Incomplete
DEFAULT_HVAC_MODES: Incomplete
HC_HOMEKIT_VALID_MODES_WATER_HEATER: Incomplete
UNIT_HASS_TO_HOMEKIT: Incomplete
HC_HEAT_COOL_OFF: int
HC_HEAT_COOL_HEAT: int
HC_HEAT_COOL_COOL: int
HC_HEAT_COOL_AUTO: int
HC_HEAT_COOL_PREFER_HEAT: Incomplete
HC_HEAT_COOL_PREFER_COOL: Incomplete
HC_MIN_TEMP: int
HC_MAX_TEMP: int
UNIT_HOMEKIT_TO_HASS: Incomplete
HC_HASS_TO_HOMEKIT: Incomplete
HC_HOMEKIT_TO_HASS: Incomplete
HC_HASS_TO_HOMEKIT_ACTION: Incomplete

def _hk_hvac_mode_from_state(state: State) -> int | None: ...

class Thermostat(HomeKitClimateAccessory):
    chars: list[str]
    char_current_heat_cool: Incomplete
    char_target_heat_cool: Incomplete
    char_target_temp: Incomplete
    char_display_units: Incomplete
    char_cooling_thresh_temp: Incomplete
    char_heating_thresh_temp: Incomplete
    char_target_humidity: Incomplete
    char_current_humidity: Incomplete
    def __init__(self, *args: Any) -> None: ...
    def _set_chars(self, char_values: dict[str, Any]) -> None: ...
    hc_homekit_to_hass: Incomplete
    hc_hass_to_homekit: Incomplete
    def _configure_hvac_modes(self, state: State) -> None: ...
    def set_target_humidity(self, value: float) -> None: ...
    @callback
    @override
    def async_update_state(self, new_state: State) -> None: ...

class WaterHeater(HomeAccessory):
    _unit: Incomplete
    _supports_on_off: Incomplete
    _supports_operation_mode: Incomplete
    _off_mode_available: Incomplete
    char_current_heat_cool: Incomplete
    char_target_heat_cool: Incomplete
    char_current_temp: Incomplete
    char_target_temp: Incomplete
    char_display_units: Incomplete
    def __init__(self, *args: Any) -> None: ...
    def get_temperature_range(self, state: State) -> tuple[float, float]: ...
    def set_heat_cool(self, value: int) -> None: ...
    def set_target_temperature(self, value: float) -> None: ...
    @callback
    @override
    def async_update_state(self, new_state: State) -> None: ...
