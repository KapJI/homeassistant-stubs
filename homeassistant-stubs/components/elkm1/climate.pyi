from . import ElkEntity as ElkEntity, create_elk_entities as create_elk_entities
from .const import DOMAIN as DOMAIN
from elkm1_lib.elements import Element as Element
from elkm1_lib.elk import Elk as Elk
from elkm1_lib.thermostats import Thermostat as Thermostat
from homeassistant.components.climate import ClimateEntity as ClimateEntity
from homeassistant.components.climate.const import ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_ON as FAN_ON, HVACMode as HVACMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PRECISION_WHOLE as PRECISION_WHOLE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SUPPORT_HVAC: Any
HASS_TO_ELK_HVAC_MODES: Any
ELK_TO_HASS_HVAC_MODES: Any
HASS_TO_ELK_FAN_MODES: Any
ELK_TO_HASS_FAN_MODES: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElkThermostat(ElkEntity, ClimateEntity):
    _attr_supported_features: Any
    _element: Thermostat
    _state: Any
    def __init__(self, element: Element, elk: Elk, elk_data: dict[str, Any]) -> None: ...
    @property
    def temperature_unit(self) -> str: ...
    @property
    def current_temperature(self) -> Union[float, None]: ...
    @property
    def target_temperature(self) -> Union[float, None]: ...
    @property
    def target_temperature_high(self) -> Union[float, None]: ...
    @property
    def target_temperature_low(self) -> Union[float, None]: ...
    @property
    def target_temperature_step(self) -> float: ...
    @property
    def current_humidity(self) -> Union[int, None]: ...
    @property
    def hvac_mode(self) -> str: ...
    @property
    def hvac_modes(self) -> list[HVACMode]: ...
    @property
    def precision(self) -> int: ...
    @property
    def is_aux_heat(self) -> bool: ...
    @property
    def min_temp(self) -> float: ...
    @property
    def max_temp(self) -> float: ...
    @property
    def fan_mode(self) -> str: ...
    def _elk_set(self, mode: Union[int, None], fan: Union[int, None]) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_turn_aux_heat_on(self) -> None: ...
    async def async_turn_aux_heat_off(self) -> None: ...
    @property
    def fan_modes(self) -> list[str]: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    def _element_changed(self, element: Element, changeset: Any) -> None: ...
