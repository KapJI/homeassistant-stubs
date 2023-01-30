import asyncio
from .const import ATTR_LAST_RESET as ATTR_LAST_RESET, ATTR_OPTIONS as ATTR_OPTIONS, ATTR_STATE_CLASS as ATTR_STATE_CLASS, CONF_STATE_CLASS as CONF_STATE_CLASS, DOMAIN as DOMAIN, SensorDeviceClass as SensorDeviceClass, SensorStateClass as SensorStateClass
from collections.abc import Mapping
from datetime import date, datetime
from decimal import Decimal
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity, EntityDescription
from homeassistant.helpers.entity_platform import EntityPlatform
from homeassistant.helpers.restore_state import ExtraStoredData, RestoreEntity
from homeassistant.helpers.typing import StateType, UndefinedType
from typing import Any

class SensorEntityDescription(EntityDescription):
    device_class: Union[SensorDeviceClass, None]
    last_reset: Union[datetime, None]
    native_precision: Union[int, None]
    native_unit_of_measurement: Union[str, None]
    options: Union[list[str], None]
    state_class: Union[SensorStateClass, str, None]
    suggested_unit_of_measurement: Union[str, None]
    unit_of_measurement: None
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_precision, native_unit_of_measurement, options, state_class, suggested_unit_of_measurement) -> None: ...

class SensorEntity(Entity):
    entity_description: SensorEntityDescription
    _attr_device_class: Union[SensorDeviceClass, None]
    _attr_last_reset: Union[datetime, None]
    _attr_native_precision: Union[int, None]
    _attr_native_unit_of_measurement: Union[str, None]
    _attr_native_value: Union[StateType, date, datetime, Decimal]
    _attr_options: Union[list[str], None]
    _attr_state_class: Union[SensorStateClass, str, None]
    _attr_state: None
    _attr_suggested_unit_of_measurement: Union[str, None]
    _attr_unit_of_measurement: None
    _invalid_numeric_value_reported: bool
    _invalid_state_class_reported: bool
    _invalid_unit_of_measurement_reported: bool
    _last_reset_reported: bool
    _sensor_option_precision: Union[int, None]
    _sensor_option_unit_of_measurement: Union[str, None, UndefinedType]
    def add_to_platform_start(self, hass: HomeAssistant, platform: EntityPlatform, parallel_updates: Union[asyncio.Semaphore, None]) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    @property
    def device_class(self) -> Union[SensorDeviceClass, None]: ...
    @property
    def options(self) -> Union[list[str], None]: ...
    @property
    def state_class(self) -> Union[SensorStateClass, str, None]: ...
    @property
    def last_reset(self) -> Union[datetime, None]: ...
    @property
    def capability_attributes(self) -> Union[Mapping[str, Any], None]: ...
    def get_initial_entity_options(self) -> Union[er.EntityOptionsType, None]: ...
    @property
    def state_attributes(self) -> Union[dict[str, Any], None]: ...
    @property
    def native_value(self) -> Union[StateType, date, datetime, Decimal]: ...
    @property
    def native_precision(self) -> Union[int, None]: ...
    @property
    def precision(self) -> Union[int, None]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def suggested_unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def state(self) -> Any: ...
    def __repr__(self) -> str: ...
    def _custom_precision_or_none(self) -> Union[int, None]: ...
    def _custom_unit_or_undef(self, primary_key: str, secondary_key: str) -> Union[str, None, UndefinedType]: ...
    def async_registry_entry_updated(self) -> None: ...

class SensorExtraStoredData(ExtraStoredData):
    native_value: Union[StateType, date, datetime, Decimal]
    native_unit_of_measurement: Union[str, None]
    def as_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_dict(cls, restored: dict[str, Any]) -> Union[SensorExtraStoredData, None]: ...
    def __init__(self, native_value, native_unit_of_measurement) -> None: ...

class RestoreSensor(SensorEntity, RestoreEntity):
    @property
    def extra_restore_state_data(self) -> SensorExtraStoredData: ...
    async def async_get_last_sensor_data(self) -> Union[SensorExtraStoredData, None]: ...
