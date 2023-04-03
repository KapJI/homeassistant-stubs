from .const import DOMAIN as DOMAIN
from .coordinator import SensiboDataUpdateCoordinator as SensiboDataUpdateCoordinator
from .entity import SensiboDeviceBaseEntity as SensiboDeviceBaseEntity, SensiboMotionBaseEntity as SensiboMotionBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_BILLION as CONCENTRATION_PARTS_PER_BILLION, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pysensibo.model import MotionSensor as MotionSensor, SensiboDevice as SensiboDevice
from typing import Any

PARALLEL_UPDATES: int

class MotionBaseEntityDescriptionMixin:
    value_fn: Callable[[MotionSensor], StateType]
    def __init__(self, value_fn) -> None: ...

class DeviceBaseEntityDescriptionMixin:
    value_fn: Callable[[SensiboDevice], StateType | datetime]
    extra_fn: Callable[[SensiboDevice], dict[str, str | bool | None] | None] | None
    def __init__(self, value_fn, extra_fn) -> None: ...

class SensiboMotionSensorEntityDescription(SensorEntityDescription, MotionBaseEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

class SensiboDeviceSensorEntityDescription(SensorEntityDescription, DeviceBaseEntityDescriptionMixin):
    def __init__(self, value_fn, extra_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

FILTER_LAST_RESET_DESCRIPTION: Incomplete
MOTION_SENSOR_TYPES: tuple[SensiboMotionSensorEntityDescription, ...]
PURE_SENSOR_TYPES: tuple[SensiboDeviceSensorEntityDescription, ...]
DEVICE_SENSOR_TYPES: tuple[SensiboDeviceSensorEntityDescription, ...]
AIRQ_SENSOR_TYPES: tuple[SensiboDeviceSensorEntityDescription, ...]
ELEMENT_SENSOR_TYPES: tuple[SensiboDeviceSensorEntityDescription, ...]
DESCRIPTION_BY_MODELS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensiboMotionSensor(SensiboMotionBaseEntity, SensorEntity):
    entity_description: SensiboMotionSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str, sensor_id: str, sensor_data: MotionSensor, entity_description: SensiboMotionSensorEntityDescription) -> None: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def native_value(self) -> StateType: ...

class SensiboDeviceSensor(SensiboDeviceBaseEntity, SensorEntity):
    entity_description: SensiboDeviceSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str, entity_description: SensiboDeviceSensorEntityDescription) -> None: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def native_value(self) -> StateType | datetime: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
