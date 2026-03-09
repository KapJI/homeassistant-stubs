from .const import STACK_TYPE_COMPOSE as STACK_TYPE_COMPOSE, STACK_TYPE_KUBERNETES as STACK_TYPE_KUBERNETES, STACK_TYPE_SWARM as STACK_TYPE_SWARM
from .coordinator import PortainerConfigEntry as PortainerConfigEntry, PortainerContainerData as PortainerContainerData, PortainerStackData as PortainerStackData
from .entity import PortainerContainerEntity as PortainerContainerEntity, PortainerCoordinatorData as PortainerCoordinatorData, PortainerEndpointEntity as PortainerEndpointEntity, PortainerStackEntity as PortainerStackEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import EntityCategory as EntityCategory, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass, StateType as StateType
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PortainerContainerSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[PortainerContainerData], StateType]

@dataclass(frozen=True, kw_only=True)
class PortainerEndpointSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[PortainerCoordinatorData], StateType]

@dataclass(frozen=True, kw_only=True)
class PortainerStackSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[PortainerStackData], StateType]

CONTAINER_SENSORS: tuple[PortainerContainerSensorEntityDescription, ...]
ENDPOINT_SENSORS: tuple[PortainerEndpointSensorEntityDescription, ...]
STACK_SENSORS: tuple[PortainerStackSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PortainerConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PortainerContainerSensor(PortainerContainerEntity, SensorEntity):
    entity_description: PortainerContainerSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...

class PortainerEndpointSensor(PortainerEndpointEntity, SensorEntity):
    entity_description: PortainerEndpointSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...

class PortainerStackSensor(PortainerStackEntity, SensorEntity):
    entity_description: PortainerStackSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...
