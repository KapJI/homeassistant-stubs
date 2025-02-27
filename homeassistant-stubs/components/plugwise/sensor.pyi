from .coordinator import PlugwiseConfigEntry as PlugwiseConfigEntry, PlugwiseDataUpdateCoordinator as PlugwiseDataUpdateCoordinator
from .entity import PlugwiseEntity as PlugwiseEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from plugwise.constants import SensorType as SensorType

PARALLEL_UPDATES: int

@dataclass(frozen=True)
class PlugwiseSensorEntityDescription(SensorEntityDescription):
    key: SensorType

SENSORS: tuple[PlugwiseSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PlugwiseConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PlugwiseSensorEntity(PlugwiseEntity, SensorEntity):
    entity_description: PlugwiseSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PlugwiseDataUpdateCoordinator, device_id: str, description: PlugwiseSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> int | float: ...
