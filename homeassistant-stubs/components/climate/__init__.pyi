from .const import ATTR_CURRENT_HUMIDITY as ATTR_CURRENT_HUMIDITY, ATTR_CURRENT_TEMPERATURE as ATTR_CURRENT_TEMPERATURE, ATTR_FAN_MODE as ATTR_FAN_MODE, ATTR_FAN_MODES as ATTR_FAN_MODES, ATTR_HUMIDITY as ATTR_HUMIDITY, ATTR_HVAC_ACTION as ATTR_HVAC_ACTION, ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_HVAC_MODES as ATTR_HVAC_MODES, ATTR_MAX_HUMIDITY as ATTR_MAX_HUMIDITY, ATTR_MAX_TEMP as ATTR_MAX_TEMP, ATTR_MIN_HUMIDITY as ATTR_MIN_HUMIDITY, ATTR_MIN_TEMP as ATTR_MIN_TEMP, ATTR_PRESET_MODE as ATTR_PRESET_MODE, ATTR_PRESET_MODES as ATTR_PRESET_MODES, ATTR_SWING_HORIZONTAL_MODE as ATTR_SWING_HORIZONTAL_MODE, ATTR_SWING_HORIZONTAL_MODES as ATTR_SWING_HORIZONTAL_MODES, ATTR_SWING_MODE as ATTR_SWING_MODE, ATTR_SWING_MODES as ATTR_SWING_MODES, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ATTR_TARGET_TEMP_STEP as ATTR_TARGET_TEMP_STEP, ClimateEntityFeature as ClimateEntityFeature, DOMAIN as DOMAIN, FAN_AUTO as FAN_AUTO, FAN_DIFFUSE as FAN_DIFFUSE, FAN_FOCUS as FAN_FOCUS, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, FAN_MIDDLE as FAN_MIDDLE, FAN_OFF as FAN_OFF, FAN_ON as FAN_ON, FAN_TOP as FAN_TOP, HVACAction as HVACAction, HVACMode as HVACMode, HVAC_MODES as HVAC_MODES, INTENT_SET_TEMPERATURE as INTENT_SET_TEMPERATURE, PRESET_ACTIVITY as PRESET_ACTIVITY, PRESET_AWAY as PRESET_AWAY, PRESET_BOOST as PRESET_BOOST, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO, PRESET_HOME as PRESET_HOME, PRESET_NONE as PRESET_NONE, PRESET_SLEEP as PRESET_SLEEP, SERVICE_SET_FAN_MODE as SERVICE_SET_FAN_MODE, SERVICE_SET_HUMIDITY as SERVICE_SET_HUMIDITY, SERVICE_SET_HVAC_MODE as SERVICE_SET_HVAC_MODE, SERVICE_SET_PRESET_MODE as SERVICE_SET_PRESET_MODE, SERVICE_SET_SWING_HORIZONTAL_MODE as SERVICE_SET_SWING_HORIZONTAL_MODE, SERVICE_SET_SWING_MODE as SERVICE_SET_SWING_MODE, SERVICE_SET_TEMPERATURE as SERVICE_SET_TEMPERATURE, SWING_BOTH as SWING_BOTH, SWING_HORIZONTAL as SWING_HORIZONTAL, SWING_OFF as SWING_OFF, SWING_ON as SWING_ON, SWING_VERTICAL as SWING_VERTICAL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter
from propcache.api import cached_property
from typing import Any, Literal, final

_LOGGER: Incomplete
DATA_COMPONENT: HassKey[EntityComponent[ClimateEntity]]
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete
DEFAULT_MIN_TEMP: int
DEFAULT_MAX_TEMP: int
DEFAULT_MIN_HUMIDITY: int
DEFAULT_MAX_HUMIDITY: int
CONVERTIBLE_ATTRIBUTE: Incomplete
SET_TEMPERATURE_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class ClimateEntityDescription(EntityDescription, frozen_or_thawed=True): ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class ClimateEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    _entity_component_unrecorded_attributes: Incomplete
    entity_description: ClimateEntityDescription
    _attr_current_humidity: int | None
    _attr_current_temperature: float | None
    _attr_fan_mode: str | None
    _attr_fan_modes: list[str] | None
    _attr_hvac_action: HVACAction | None
    _attr_hvac_mode: HVACMode | None
    _attr_hvac_modes: list[HVACMode]
    _attr_max_humidity: float
    _attr_max_temp: float
    _attr_min_humidity: float
    _attr_min_temp: float
    _attr_precision: float
    _attr_preset_mode: str | None
    _attr_preset_modes: list[str] | None
    _attr_supported_features: ClimateEntityFeature
    _attr_swing_mode: str | None
    _attr_swing_modes: list[str] | None
    _attr_swing_horizontal_mode: str | None
    _attr_swing_horizontal_modes: list[str] | None
    _attr_target_humidity: float | None
    _attr_target_temperature_high: float | None
    _attr_target_temperature_low: float | None
    _attr_target_temperature_step: float | None
    _attr_target_temperature: float | None
    _attr_temperature_unit: str
    @final
    @property
    def state(self) -> str | None: ...
    @property
    def precision(self) -> float: ...
    @property
    def capability_attributes(self) -> dict[str, Any] | None: ...
    @final
    @property
    def state_attributes(self) -> dict[str, Any]: ...
    @cached_property
    def temperature_unit(self) -> str: ...
    @cached_property
    def current_humidity(self) -> float | None: ...
    @cached_property
    def target_humidity(self) -> float | None: ...
    @cached_property
    def hvac_mode(self) -> HVACMode | None: ...
    @cached_property
    def hvac_modes(self) -> list[HVACMode]: ...
    @cached_property
    def hvac_action(self) -> HVACAction | None: ...
    @cached_property
    def current_temperature(self) -> float | None: ...
    @cached_property
    def target_temperature(self) -> float | None: ...
    @cached_property
    def target_temperature_step(self) -> float | None: ...
    @cached_property
    def target_temperature_high(self) -> float | None: ...
    @cached_property
    def target_temperature_low(self) -> float | None: ...
    @cached_property
    def preset_mode(self) -> str | None: ...
    @cached_property
    def preset_modes(self) -> list[str] | None: ...
    @cached_property
    def fan_mode(self) -> str | None: ...
    @cached_property
    def fan_modes(self) -> list[str] | None: ...
    @cached_property
    def swing_mode(self) -> str | None: ...
    @cached_property
    def swing_modes(self) -> list[str] | None: ...
    @cached_property
    def swing_horizontal_mode(self) -> str | None: ...
    @cached_property
    def swing_horizontal_modes(self) -> list[str] | None: ...
    @final
    @callback
    def _valid_mode_or_raise(self, mode_type: Literal['preset', 'horizontal_swing', 'swing', 'fan', 'hvac'], mode: str | HVACMode, modes: list[str] | list[HVACMode] | None) -> None: ...
    def set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    def set_humidity(self, humidity: int) -> None: ...
    async def async_set_humidity(self, humidity: int) -> None: ...
    @final
    async def async_handle_set_fan_mode_service(self, fan_mode: str) -> None: ...
    def set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    @final
    async def async_handle_set_hvac_mode_service(self, hvac_mode: HVACMode) -> None: ...
    def set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @final
    async def async_handle_set_swing_mode_service(self, swing_mode: str) -> None: ...
    def set_swing_mode(self, swing_mode: str) -> None: ...
    async def async_set_swing_mode(self, swing_mode: str) -> None: ...
    @final
    async def async_handle_set_swing_horizontal_mode_service(self, swing_horizontal_mode: str) -> None: ...
    def set_swing_horizontal_mode(self, swing_horizontal_mode: str) -> None: ...
    async def async_set_swing_horizontal_mode(self, swing_horizontal_mode: str) -> None: ...
    @final
    async def async_handle_set_preset_mode_service(self, preset_mode: str) -> None: ...
    def set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    def turn_on(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    def turn_off(self) -> None: ...
    async def async_turn_off(self) -> None: ...
    def toggle(self) -> None: ...
    async def async_toggle(self) -> None: ...
    @cached_property
    def supported_features(self) -> ClimateEntityFeature: ...
    @cached_property
    def min_temp(self) -> float: ...
    @cached_property
    def max_temp(self) -> float: ...
    @cached_property
    def min_humidity(self) -> float: ...
    @cached_property
    def max_humidity(self) -> float: ...

async def async_service_humidity_set(entity: ClimateEntity, service_call: ServiceCall) -> None: ...
async def async_service_temperature_set(entity: ClimateEntity, service_call: ServiceCall) -> None: ...
