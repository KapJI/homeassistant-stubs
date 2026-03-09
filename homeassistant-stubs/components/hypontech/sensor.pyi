from .coordinator import HypontechConfigEntry as HypontechConfigEntry, HypontechDataCoordinator as HypontechDataCoordinator
from .entity import HypontechEntity as HypontechEntity, HypontechPlantEntity as HypontechPlantEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from hyponcloud import OverviewData as OverviewData, PlantData as PlantData

@dataclass(frozen=True, kw_only=True)
class HypontechSensorDescription(SensorEntityDescription):
    value_fn: Callable[[OverviewData], float | None]

@dataclass(frozen=True, kw_only=True)
class HypontechPlantSensorDescription(SensorEntityDescription):
    value_fn: Callable[[PlantData], float | None]

OVERVIEW_SENSORS: tuple[HypontechSensorDescription, ...]
PLANT_SENSORS: tuple[HypontechPlantSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: HypontechConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HypontechOverviewSensor(HypontechEntity, SensorEntity):
    entity_description: HypontechSensorDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: HypontechDataCoordinator, description: HypontechSensorDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...

class HypontechPlantSensor(HypontechPlantEntity, SensorEntity):
    entity_description: HypontechPlantSensorDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: HypontechDataCoordinator, plant_id: str, description: HypontechPlantSensorDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
