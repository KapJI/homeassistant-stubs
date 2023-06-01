from . import Sun as Sun
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEGREE as DEGREE, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

ENTITY_ID_SENSOR_FORMAT: Incomplete

class SunEntityDescriptionMixin:
    value_fn: Callable[[Sun], StateType | datetime]
    def __init__(self, value_fn) -> None: ...

class SunSensorEntityDescription(SensorEntityDescription, SunEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

SENSOR_TYPES: tuple[SunSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SunSensor(SensorEntity):
    _attr_has_entity_name: bool
    _attr_entity_category: Incomplete
    entity_description: SunSensorEntityDescription
    entity_id: Incomplete
    _attr_unique_id: Incomplete
    sun: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, sun: Sun, entity_description: SunSensorEntityDescription, entry_id: str) -> None: ...
    @property
    def native_value(self) -> StateType | datetime: ...
