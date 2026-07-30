from .accessories import TYPES as TYPES
from .climate_base import CLIMATE_INACTIVE_STATES as CLIMATE_INACTIVE_STATES, HomeKitClimateAccessory as HomeKitClimateAccessory
from .climate_util import temperature_attribute_to_homekit as temperature_attribute_to_homekit
from .const import CHAR_ACTIVE as CHAR_ACTIVE, CHAR_COOLING_THRESHOLD_TEMPERATURE as CHAR_COOLING_THRESHOLD_TEMPERATURE, CHAR_CURRENT_FAN_STATE as CHAR_CURRENT_FAN_STATE, CHAR_CURRENT_HEATER_COOLER_STATE as CHAR_CURRENT_HEATER_COOLER_STATE, CHAR_CURRENT_HUMIDITY as CHAR_CURRENT_HUMIDITY, CHAR_CURRENT_TEMPERATURE as CHAR_CURRENT_TEMPERATURE, CHAR_HEATING_THRESHOLD_TEMPERATURE as CHAR_HEATING_THRESHOLD_TEMPERATURE, CHAR_NAME as CHAR_NAME, CHAR_ROTATION_SPEED as CHAR_ROTATION_SPEED, CHAR_SWING_MODE as CHAR_SWING_MODE, CHAR_TARGET_FAN_STATE as CHAR_TARGET_FAN_STATE, CHAR_TARGET_HEATER_COOLER_STATE as CHAR_TARGET_HEATER_COOLER_STATE, PROP_MAX_VALUE as PROP_MAX_VALUE, PROP_MIN_STEP as PROP_MIN_STEP, PROP_MIN_VALUE as PROP_MIN_VALUE, SERV_HEATER_COOLER as SERV_HEATER_COOLER, SERV_HUMIDITY_SENSOR as SERV_HUMIDITY_SENSOR
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.climate import ATTR_CURRENT_HUMIDITY as ATTR_CURRENT_HUMIDITY, ATTR_CURRENT_TEMPERATURE as ATTR_CURRENT_TEMPERATURE, ATTR_HVAC_ACTION as ATTR_HVAC_ACTION, ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_HVAC_MODES as ATTR_HVAC_MODES, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ATTR_TEMPERATURE as ATTR_TEMPERATURE, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_ON as FAN_ON, HVACAction as HVACAction, HVACMode as HVACMode, SERVICE_SET_FAN_MODE as SERVICE_SET_FAN_MODE, SERVICE_SET_HVAC_MODE as SERVICE_SET_HVAC_MODE, SERVICE_SET_SWING_MODE as SERVICE_SET_SWING_MODE, SERVICE_SET_TEMPERATURE as SERVICE_SET_TEMPERATURE
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES
from homeassistant.core import State as State, callback as callback
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from pyhap.characteristic import Characteristic as Characteristic
from typing import Any, Concatenate, NamedTuple, override

_LOGGER: Incomplete
HC_INACTIVE: Incomplete
HC_IDLE: Incomplete
HC_HEATING: Incomplete
HC_COOLING: Incomplete
HC_TARGET_AUTO: Incomplete
HC_TARGET_HEAT: Incomplete
HC_TARGET_COOL: Incomplete
HC_HASS_TO_HOMEKIT_TARGET: Incomplete
HC_HASS_TO_HOMEKIT_ACTION: Incomplete
ACTION_HYSTERESIS: float

class ClimateServiceCall(NamedTuple):
    service: str
    data: dict[str, Any]
    commit_mode: HVACMode | None = ...
    pending_mode: HVACMode | None = ...

def _locked_write[**_P](func: Callable[Concatenate[HeaterCooler, _P], Coroutine[Any, Any, None]]) -> Callable[Concatenate[HeaterCooler, _P], Coroutine[Any, Any, None]]: ...

RANGE_MODES: Incomplete

class HeaterCooler(HomeKitClimateAccessory):
    char_cool: Characteristic
    char_heat: Characteristic
    char_current_humidity: Characteristic
    _supports_off: Incomplete
    category: Incomplete
    _has_cool_threshold: Incomplete
    _has_heat_threshold: Incomplete
    _hk_to_ha_target: dict[int, HVACMode]
    char_active: Incomplete
    char_current_state: Incomplete
    _ha_to_hk_target: Incomplete
    char_target_state: Incomplete
    char_speed: Incomplete
    char_swing: Incomplete
    _has_humidity: Incomplete
    _last_known_mode: HVACMode
    _write_lock: Incomplete
    _pending_mode: HVACMode | None
    _last_reported_mode: Incomplete
    def __init__(self, *args: Any) -> None: ...
    def _set_chars(self, char_values: dict[str, Any]) -> None: ...
    @_locked_write
    async def _async_apply_batch(self, char_values: dict[str, Any]) -> None: ...
    @override
    def _dispatch_climate_write(self, service: str, params: dict[str, Any]) -> None: ...
    @_locked_write
    async def _async_apply_locked_write(self, service: str, params: dict[str, Any]) -> None: ...
    def _queue_fan_swing_changes(self, char_values: dict[str, Any], service_calls: list[ClimateServiceCall]) -> None: ...
    def _handle_active_mode_changes(self, active: int | None, target_mode: int | None, service_calls: list[ClimateServiceCall], current_state: State | None, requested_mode: HVACMode | None) -> bool: ...
    def _handle_temperature_changes(self, char_values: dict[str, Any], service_calls: list[ClimateServiceCall], current_state: State | None, requested_mode: HVACMode | None) -> None: ...
    def _handle_single_temp_changes(self, service_calls: list[ClimateServiceCall], cooling_temp: float | None, heating_temp: float | None, current_state: State | None, effective_mode: HVACMode | str | None) -> None: ...
    def _hk_target_mode(self, mode: HVACMode) -> int | None: ...
    @callback
    @override
    def async_update_state(self, new_state: State) -> None: ...
    def _update_temperature_thresholds(self, state: State) -> None: ...
    def _derive_action(self, state: State, mode: HVACMode | None) -> HVACAction: ...
