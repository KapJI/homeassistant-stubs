from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .discovery_data_template import DynamicCurrentTempClimateDataTemplate as DynamicCurrentTempClimateDataTemplate
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from .helpers import get_value_of_zwave_value as get_value_of_zwave_value
from homeassistant.components.climate import ClimateEntity as ClimateEntity, DEFAULT_MAX_TEMP as DEFAULT_MAX_TEMP, DEFAULT_MIN_TEMP as DEFAULT_MIN_TEMP
from homeassistant.components.climate.const import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_NONE as PRESET_NONE
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_TENTHS as PRECISION_TENTHS, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from zwave_js_server.client import Client as ZwaveClient
from zwave_js_server.const.command_class.thermostat import ThermostatSetpointType
from zwave_js_server.model.value import Value as ZwaveValue

ZW_HVAC_MODE_MAP: dict[int, HVACMode]
HVAC_CURRENT_MAP: dict[int, HVACAction]
ATTR_FAN_STATE: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ZWaveClimate(ZWaveBaseEntity, ClimateEntity):
    _hvac_modes: Any
    _hvac_presets: Any
    _unit_value: Any
    _current_mode: Any
    _setpoint_values: Any
    _operating_state: Any
    _current_temp: Any
    _current_humidity: Any
    _fan_mode: Any
    _fan_state: Any
    _attr_supported_features: int
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    def _setpoint_value(self, setpoint_type: ThermostatSetpointType) -> ZwaveValue: ...
    def _set_modes_and_presets(self) -> None: ...
    @property
    def _current_mode_setpoint_enums(self) -> list[Union[ThermostatSetpointType, None]]: ...
    @property
    def temperature_unit(self) -> str: ...
    @property
    def precision(self) -> float: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def hvac_modes(self) -> list[HVACMode]: ...
    @property
    def hvac_action(self) -> Union[HVACAction, None]: ...
    @property
    def current_humidity(self) -> Union[int, None]: ...
    @property
    def current_temperature(self) -> Union[float, None]: ...
    @property
    def target_temperature(self) -> Union[float, None]: ...
    @property
    def target_temperature_high(self) -> Union[float, None]: ...
    @property
    def target_temperature_low(self) -> Union[float, None]: ...
    @property
    def preset_mode(self) -> Union[str, None]: ...
    @property
    def preset_modes(self) -> Union[list[str], None]: ...
    @property
    def fan_mode(self) -> Union[str, None]: ...
    @property
    def fan_modes(self) -> Union[list[str], None]: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, str], None]: ...
    @property
    def min_temp(self) -> float: ...
    @property
    def max_temp(self) -> float: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...

class DynamicCurrentTempClimate(ZWaveClimate):
    data_template: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def current_temperature(self) -> Union[float, None]: ...
