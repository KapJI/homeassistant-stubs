from .entity import DOMAIN as DOMAIN, SkybellEntity as SkybellEntity
from aioskybell import SkybellDevice as SkybellDevice
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

class SkybellSensorEntityDescriptionMixIn:
    value_fn: Callable[[SkybellDevice], StateType | datetime]
    def __init__(self, value_fn) -> None: ...

class SkybellSensorEntityDescription(SensorEntityDescription, SkybellSensorEntityDescriptionMixIn):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

SENSOR_TYPES: tuple[SkybellSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SkybellSensor(SkybellEntity, SensorEntity):
    entity_description: SkybellSensorEntityDescription
    @property
    def native_value(self) -> StateType | datetime: ...
