import asyncio
from .const import ATTR_LAST_RESET as ATTR_LAST_RESET, ATTR_OPTIONS as ATTR_OPTIONS, ATTR_STATE_CLASS as ATTR_STATE_CLASS, CONF_STATE_CLASS as CONF_STATE_CLASS, DEVICE_CLASS_STATE_CLASSES as DEVICE_CLASS_STATE_CLASSES, DOMAIN as DOMAIN, SensorDeviceClass as SensorDeviceClass, SensorStateClass as SensorStateClass
from _typeshed import Incomplete
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from functools import cached_property
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity, EntityDescription
from homeassistant.helpers.entity_platform import EntityPlatform
from homeassistant.helpers.restore_state import ExtraStoredData, RestoreEntity
from homeassistant.helpers.typing import StateType, UndefinedType
from typing import Any, Self

__all__ = ['ATTR_LAST_RESET', 'ATTR_OPTIONS', 'ATTR_STATE_CLASS', 'CONF_STATE_CLASS', 'DEVICE_CLASS_STATE_CLASSES', 'DOMAIN', 'PLATFORM_SCHEMA_BASE', 'PLATFORM_SCHEMA', 'RestoreSensor', 'SensorDeviceClass', 'SensorEntity', 'SensorEntityDescription', 'SensorExtraStoredData', 'SensorStateClass']

class SensorEntityDescription(EntityDescription, frozen_or_thawed=True):
    device_class: SensorDeviceClass | None
    last_reset: datetime | None
    native_unit_of_measurement: str | None
    options: list[str] | None
    state_class: SensorStateClass | str | None
    suggested_display_precision: int | None
    suggested_unit_of_measurement: str | None
    unit_of_measurement: None
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

class SensorEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    _entity_component_unrecorded_attributes: Incomplete
    entity_description: SensorEntityDescription
    _attr_device_class: SensorDeviceClass | None
    _attr_last_reset: datetime | None
    _attr_native_unit_of_measurement: str | None
    _attr_native_value: StateType | date | datetime | Decimal
    _attr_options: list[str] | None
    _attr_state_class: SensorStateClass | str | None
    _attr_state: None
    _attr_suggested_display_precision: int | None
    _attr_suggested_unit_of_measurement: str | None
    _attr_unit_of_measurement: None
    _invalid_state_class_reported: bool
    _invalid_unit_of_measurement_reported: bool
    _last_reset_reported: bool
    _sensor_option_display_precision: int | None
    _sensor_option_unit_of_measurement: str | None | UndefinedType
    _invalid_suggested_unit_of_measurement_reported: bool
    registry_entry: Incomplete
    def add_to_platform_start(self, hass: HomeAssistant, platform: EntityPlatform, parallel_updates: asyncio.Semaphore | None) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    def _default_to_device_class_name(self) -> bool: ...
    @cached_property
    def device_class(self) -> SensorDeviceClass | None: ...
    @property
    def _numeric_state_expected(self) -> bool: ...
    @cached_property
    def options(self) -> list[str] | None: ...
    @cached_property
    def state_class(self) -> SensorStateClass | str | None: ...
    @cached_property
    def last_reset(self) -> datetime | None: ...
    @property
    def capability_attributes(self) -> Mapping[str, Any] | None: ...
    def _is_valid_suggested_unit(self, suggested_unit_of_measurement: str) -> bool: ...
    def _get_initial_suggested_unit(self) -> str | UndefinedType: ...
    def get_initial_entity_options(self) -> er.EntityOptionsType | None: ...
    @property
    def state_attributes(self) -> dict[str, Any] | None: ...
    @cached_property
    def native_value(self) -> StateType | date | datetime | Decimal: ...
    @cached_property
    def suggested_display_precision(self) -> int | None: ...
    @cached_property
    def native_unit_of_measurement(self) -> str | None: ...
    @cached_property
    def suggested_unit_of_measurement(self) -> str | None: ...
    @property
    def unit_of_measurement(self) -> str | None: ...
    @property
    def state(self) -> Any: ...
    def _display_precision_or_none(self) -> int | None: ...
    def _update_suggested_precision(self) -> None: ...
    def _custom_unit_or_undef(self, primary_key: str, secondary_key: str) -> str | None | UndefinedType: ...
    def async_registry_entry_updated(self) -> None: ...
    def _async_read_entity_options(self) -> None: ...

@dataclass
class SensorExtraStoredData(ExtraStoredData):
    native_value: StateType | date | datetime | Decimal
    native_unit_of_measurement: str | None
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, restored: dict[str, Any]) -> Self | None: ...
    def __init__(self, native_value, native_unit_of_measurement) -> None: ...

class RestoreSensor(SensorEntity, RestoreEntity):
    @property
    def extra_restore_state_data(self) -> SensorExtraStoredData: ...
    async def async_get_last_sensor_data(self) -> SensorExtraStoredData | None: ...
