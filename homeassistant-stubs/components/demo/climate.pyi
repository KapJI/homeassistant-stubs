from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.climate import ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

SUPPORT_FLAGS: int

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DemoClimate(ClimateEntity):
    _attr_should_poll: bool
    _unique_id: Incomplete
    _attr_name: Incomplete
    _support_flags: Incomplete
    _target_temperature: Incomplete
    _target_humidity: Incomplete
    _unit_of_measurement: Incomplete
    _preset: Incomplete
    _preset_modes: Incomplete
    _current_temperature: Incomplete
    _current_humidity: Incomplete
    _current_fan_mode: Incomplete
    _hvac_action: Incomplete
    _hvac_mode: Incomplete
    _aux: Incomplete
    _current_swing_mode: Incomplete
    _fan_modes: Incomplete
    _hvac_modes: Incomplete
    _swing_modes: Incomplete
    _target_temperature_high: Incomplete
    _target_temperature_low: Incomplete
    def __init__(self, unique_id: str, name: str, target_temperature: Union[float, None], unit_of_measurement: str, preset: Union[str, None], current_temperature: float, fan_mode: Union[str, None], target_humidity: Union[int, None], current_humidity: Union[int, None], swing_mode: Union[str, None], hvac_mode: HVACMode, hvac_action: Union[HVACAction, None], aux: Union[bool, None], target_temp_high: Union[float, None], target_temp_low: Union[float, None], hvac_modes: list[HVACMode], preset_modes: Union[list[str], None] = ...) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def supported_features(self) -> int: ...
    @property
    def temperature_unit(self) -> str: ...
    @property
    def current_temperature(self) -> float: ...
    @property
    def target_temperature(self) -> Union[float, None]: ...
    @property
    def target_temperature_high(self) -> Union[float, None]: ...
    @property
    def target_temperature_low(self) -> Union[float, None]: ...
    @property
    def current_humidity(self) -> Union[int, None]: ...
    @property
    def target_humidity(self) -> Union[int, None]: ...
    @property
    def hvac_action(self) -> Union[HVACAction, None]: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def hvac_modes(self) -> list[HVACMode]: ...
    @property
    def preset_mode(self) -> Union[str, None]: ...
    @property
    def preset_modes(self) -> Union[list[str], None]: ...
    @property
    def is_aux_heat(self) -> Union[bool, None]: ...
    @property
    def fan_mode(self) -> Union[str, None]: ...
    @property
    def fan_modes(self) -> list[str]: ...
    @property
    def swing_mode(self) -> Union[str, None]: ...
    @property
    def swing_modes(self) -> list[str]: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_humidity(self, humidity: int) -> None: ...
    async def async_set_swing_mode(self, swing_mode: str) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_turn_aux_heat_on(self) -> None: ...
    async def async_turn_aux_heat_off(self) -> None: ...
