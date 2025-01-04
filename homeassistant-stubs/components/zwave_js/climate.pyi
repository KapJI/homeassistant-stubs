from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .discovery_data_template import DynamicCurrentTempClimateDataTemplate as DynamicCurrentTempClimateDataTemplate
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from .helpers import get_value_of_zwave_value as get_value_of_zwave_value
from _typeshed import Incomplete
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_NONE as PRESET_NONE
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_TENTHS as PRECISION_TENTHS, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter
from typing import Any
from zwave_js_server.const.command_class.thermostat import ThermostatSetpointType
from zwave_js_server.model.driver import Driver as Driver
from zwave_js_server.model.value import Value as ZwaveValue

PARALLEL_UPDATES: int
THERMOSTAT_MODES: Incomplete
ZW_HVAC_MODE_MAP: dict[int, HVACMode]
HVAC_CURRENT_MAP: dict[int, HVACAction]
ATTR_FAN_STATE: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ZWaveClimate(ZWaveBaseEntity, ClimateEntity):
    _attr_precision = PRECISION_TENTHS
    _hvac_modes: Incomplete
    _hvac_presets: Incomplete
    _unit_value: Incomplete
    _last_hvac_mode_id_before_off: Incomplete
    _current_mode: Incomplete
    _supports_resume: Incomplete
    _setpoint_values: Incomplete
    _operating_state: Incomplete
    _current_temp: Incomplete
    _current_humidity: Incomplete
    _fan_mode: Incomplete
    _fan_state: Incomplete
    def __init__(self, config_entry: ConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo) -> None: ...
    def _setpoint_value_or_raise(self, setpoint_type: ThermostatSetpointType) -> ZwaveValue: ...
    def _setpoint_temperature(self, setpoint_type: ThermostatSetpointType) -> float | None: ...
    def _set_modes_and_presets(self) -> None: ...
    @property
    def _current_mode_setpoint_enums(self) -> list[ThermostatSetpointType]: ...
    @property
    def temperature_unit(self) -> str: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def hvac_modes(self) -> list[HVACMode]: ...
    @property
    def hvac_action(self) -> HVACAction | None: ...
    @property
    def current_humidity(self) -> int | None: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def target_temperature_high(self) -> float | None: ...
    @property
    def target_temperature_low(self) -> float | None: ...
    @property
    def preset_mode(self) -> str | None: ...
    @property
    def preset_modes(self) -> list[str] | None: ...
    @property
    def fan_mode(self) -> str | None: ...
    @property
    def fan_modes(self) -> list[str] | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str] | None: ...
    @property
    def min_temp(self) -> float: ...
    @property
    def max_temp(self) -> float: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_turn_off(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...

class DynamicCurrentTempClimate(ZWaveClimate):
    data_template: Incomplete
    def __init__(self, config_entry: ConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def current_temperature(self) -> float | None: ...
