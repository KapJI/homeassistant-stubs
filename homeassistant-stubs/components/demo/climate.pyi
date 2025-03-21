from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

SUPPORT_FLAGS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DemoClimate(ClimateEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_should_poll: bool
    _attr_translation_key: str
    _unique_id: Incomplete
    _attr_supported_features: Incomplete
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
    _current_swing_mode: Incomplete
    _current_swing_horizontal_mode: Incomplete
    _fan_modes: Incomplete
    _hvac_modes: Incomplete
    _swing_modes: Incomplete
    _swing_horizontal_modes: Incomplete
    _target_temperature_high: Incomplete
    _target_temperature_low: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, unique_id: str, device_name: str, target_temperature: float | None, unit_of_measurement: str, preset: str | None, current_temperature: float, fan_mode: str | None, target_humidity: float | None, current_humidity: float | None, swing_mode: str | None, swing_horizontal_mode: str | None, hvac_mode: HVACMode, hvac_action: HVACAction | None, target_temp_high: float | None, target_temp_low: float | None, hvac_modes: list[HVACMode], preset_modes: list[str] | None = None) -> None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def temperature_unit(self) -> str: ...
    @property
    def current_temperature(self) -> float: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def target_temperature_high(self) -> float | None: ...
    @property
    def target_temperature_low(self) -> float | None: ...
    @property
    def current_humidity(self) -> float | None: ...
    @property
    def target_humidity(self) -> float | None: ...
    @property
    def hvac_action(self) -> HVACAction | None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def hvac_modes(self) -> list[HVACMode]: ...
    @property
    def preset_mode(self) -> str | None: ...
    @property
    def preset_modes(self) -> list[str] | None: ...
    @property
    def fan_mode(self) -> str | None: ...
    @property
    def fan_modes(self) -> list[str]: ...
    @property
    def swing_mode(self) -> str | None: ...
    @property
    def swing_modes(self) -> list[str]: ...
    @property
    def swing_horizontal_mode(self) -> str | None: ...
    @property
    def swing_horizontal_modes(self) -> list[str]: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_humidity(self, humidity: int) -> None: ...
    async def async_set_swing_mode(self, swing_mode: str) -> None: ...
    async def async_set_swing_horizontal_mode(self, swing_horizontal_mode: str) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
