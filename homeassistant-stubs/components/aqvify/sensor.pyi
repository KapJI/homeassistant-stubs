from .coordinator import AqvifyConfigEntry as AqvifyConfigEntry
from .entity import AqvifyAggrEntity as AqvifyAggrEntity, AqvifyEntity as AqvifyEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass, StateType as StateType
from homeassistant.const import UnitOfLength as UnitOfLength, UnitOfTemperature as UnitOfTemperature, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyaqvify import AqvifyDeviceData as AqvifyDeviceData, AqvifyHourAggregatedValues as AqvifyHourAggregatedValues
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class AqvifySensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[AqvifyDeviceData], float | int | None]

@dataclass(frozen=True, kw_only=True)
class AqvifySensorAggrEntityDescription(SensorEntityDescription):
    value_fn: Callable[[AqvifyHourAggregatedValues], float | int | None]

ENTITIES: tuple[AqvifySensorEntityDescription, ...]
ENTITIES_AGGR: tuple[AqvifySensorAggrEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AqvifyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AqvifySensor(AqvifyEntity, SensorEntity):
    entity_description: AqvifySensorEntityDescription
    @property
    @override
    def native_value(self) -> StateType | datetime | None: ...

class AqvifyAggrSensor(AqvifyAggrEntity, SensorEntity):
    entity_description: AqvifySensorAggrEntityDescription
    @property
    @override
    def native_value(self) -> StateType | datetime | None: ...
