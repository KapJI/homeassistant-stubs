from . import SensiboConfigEntry as SensiboConfigEntry
from .coordinator import SensiboDataUpdateCoordinator as SensiboDataUpdateCoordinator
from .entity import SensiboDeviceBaseEntity as SensiboDeviceBaseEntity, SensiboMotionBaseEntity as SensiboMotionBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfDensity as UnitOfDensity, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfRatio as UnitOfRatio, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pysensibo.model import MotionSensor as MotionSensor, PureAQI, SensiboDevice as SensiboDevice
from typing import Any, override

PARALLEL_UPDATES: int

def _smart_type_name(_type: str | None) -> str | None: ...

@dataclass(frozen=True, kw_only=True)
class SensiboMotionSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[MotionSensor], StateType]

@dataclass(frozen=True, kw_only=True)
class SensiboDeviceSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[SensiboDevice], StateType | datetime]
    extra_fn: Callable[[SensiboDevice], dict[str, str | bool | None] | None] | None

FILTER_LAST_RESET_DESCRIPTION: Incomplete
MOTION_SENSOR_TYPES: tuple[SensiboMotionSensorEntityDescription, ...]

def _pure_aqi(pm25_pure: PureAQI | None) -> str | None: ...

PURE_SENSOR_TYPES: tuple[SensiboDeviceSensorEntityDescription, ...]
DEVICE_SENSOR_TYPES: tuple[SensiboDeviceSensorEntityDescription, ...]
AIRQ_SENSOR_TYPES: tuple[SensiboDeviceSensorEntityDescription, ...]
ELEMENT_SENSOR_TYPES: tuple[SensiboDeviceSensorEntityDescription, ...]
DESCRIPTION_BY_MODELS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SensiboConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SensiboMotionSensor(SensiboMotionBaseEntity, SensorEntity):
    entity_description: SensiboMotionSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str, sensor_id: str, sensor_data: MotionSensor, entity_description: SensiboMotionSensorEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> StateType: ...

class SensiboDeviceSensor(SensiboDeviceBaseEntity, SensorEntity):
    entity_description: SensiboDeviceSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SensiboDataUpdateCoordinator, device_id: str, entity_description: SensiboDeviceSensorEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> StateType | datetime: ...
    @property
    @override
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
