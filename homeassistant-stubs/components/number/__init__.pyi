import dataclasses
from .const import ATTR_MAX as ATTR_MAX, ATTR_MIN as ATTR_MIN, ATTR_STEP as ATTR_STEP, ATTR_VALUE as ATTR_VALUE, DEFAULT_MAX_VALUE as DEFAULT_MAX_VALUE, DEFAULT_MIN_VALUE as DEFAULT_MIN_VALUE, DEFAULT_STEP as DEFAULT_STEP, DOMAIN as DOMAIN, NumberDeviceClass as NumberDeviceClass, NumberMode as NumberMode
from _typeshed import Incomplete
from collections.abc import Callable
from homeassistant.core import callback
from homeassistant.helpers.entity import Entity, EntityDescription
from homeassistant.helpers.restore_state import ExtraStoredData, RestoreEntity
from propcache import cached_property
from typing import Any, Self, final

__all__ = ['ATTR_MAX', 'ATTR_MIN', 'ATTR_STEP', 'ATTR_VALUE', 'DEFAULT_MAX_VALUE', 'DEFAULT_MIN_VALUE', 'DEFAULT_STEP', 'DOMAIN', 'PLATFORM_SCHEMA_BASE', 'PLATFORM_SCHEMA', 'NumberDeviceClass', 'NumberEntity', 'NumberEntityDescription', 'NumberExtraStoredData', 'NumberMode', 'RestoreNumber']

PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete

class NumberEntityDescription(EntityDescription, frozen_or_thawed=True):
    device_class: NumberDeviceClass | None = ...
    max_value: None = ...
    min_value: None = ...
    mode: NumberMode | None = ...
    native_max_value: float | None = ...
    native_min_value: float | None = ...
    native_step: float | None = ...
    native_unit_of_measurement: str | None = ...
    step: None = ...
    unit_of_measurement: None = ...

class NumberEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    _entity_component_unrecorded_attributes: Incomplete
    entity_description: NumberEntityDescription
    _attr_device_class: NumberDeviceClass | None
    _attr_max_value: None
    _attr_min_value: None
    _attr_mode: NumberMode
    _attr_state: None
    _attr_step: None
    _attr_unit_of_measurement: None
    _attr_value: None
    _attr_native_max_value: float
    _attr_native_min_value: float
    _attr_native_step: float
    _attr_native_unit_of_measurement: str | None
    _attr_native_value: float | None
    _deprecated_number_entity_reported: bool
    _number_option_unit_of_measurement: str | None
    def __init_subclass__(cls, **kwargs: Any) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    @property
    def capability_attributes(self) -> dict[str, Any]: ...
    def _default_to_device_class_name(self) -> bool: ...
    @cached_property
    def device_class(self) -> NumberDeviceClass | None: ...
    @cached_property
    def native_min_value(self) -> float: ...
    @property
    @final
    def min_value(self) -> float: ...
    @cached_property
    def native_max_value(self) -> float: ...
    @property
    @final
    def max_value(self) -> float: ...
    @cached_property
    def native_step(self) -> float | None: ...
    @property
    @final
    def step(self) -> float: ...
    def _calculate_step(self, min_value: float, max_value: float) -> float: ...
    @cached_property
    def mode(self) -> NumberMode: ...
    @property
    @final
    def state(self) -> float | None: ...
    @cached_property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    @final
    def unit_of_measurement(self) -> str | None: ...
    @cached_property
    def native_value(self) -> float | None: ...
    @property
    @final
    def value(self) -> float | None: ...
    def set_native_value(self, value: float) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
    @final
    def set_value(self, value: float) -> None: ...
    @final
    async def async_set_value(self, value: float) -> None: ...
    def _convert_to_state_value(self, value: float, method: Callable[[float, int], float], device_class: NumberDeviceClass | None) -> float: ...
    def convert_to_native_value(self, value: float) -> float: ...
    @callback
    def async_registry_entry_updated(self) -> None: ...

@dataclasses.dataclass
class NumberExtraStoredData(ExtraStoredData):
    native_max_value: float | None
    native_min_value: float | None
    native_step: float | None
    native_unit_of_measurement: str | None
    native_value: float | None
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, restored: dict[str, Any]) -> Self | None: ...

class RestoreNumber(NumberEntity, RestoreEntity):
    @property
    def extra_restore_state_data(self) -> NumberExtraStoredData: ...
    async def async_get_last_number_data(self) -> NumberExtraStoredData | None: ...
