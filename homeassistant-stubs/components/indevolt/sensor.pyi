from . import IndevoltConfigEntry as IndevoltConfigEntry
from .coordinator import IndevoltCoordinator as IndevoltCoordinator
from .entity import IndevoltEntity as IndevoltEntity
from _typeshed import Incomplete
from dataclasses import dataclass, field
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from indevolt_api import IndevoltEnergyMode
from typing import Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class IndevoltSensorEntityDescription(SensorEntityDescription):
    state_mapping: dict[str | int, str] = field(default_factory=dict)
    generation: tuple[int, ...] = ...
    energy_mode: IndevoltEnergyMode | None = ...

SENSORS: Final[Incomplete]
BATTERY_PACK_SENSOR_KEYS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: IndevoltConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IndevoltSensorEntity(IndevoltEntity, SensorEntity):
    entity_description: IndevoltSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    def __init__(self, coordinator: IndevoltCoordinator, description: IndevoltSensorEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> str | int | float | None: ...
