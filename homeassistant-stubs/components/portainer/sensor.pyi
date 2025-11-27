from .coordinator import PortainerConfigEntry as PortainerConfigEntry, PortainerContainerData as PortainerContainerData, PortainerCoordinator as PortainerCoordinator
from .entity import PortainerContainerEntity as PortainerContainerEntity, PortainerCoordinatorData as PortainerCoordinatorData, PortainerEndpointEntity as PortainerEndpointEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import EntityCategory as EntityCategory, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass, StateType as StateType
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class PortainerContainerSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[PortainerContainerData], StateType]

@dataclass(frozen=True, kw_only=True)
class PortainerEndpointSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[PortainerCoordinatorData], StateType]

CONTAINER_SENSORS: tuple[PortainerContainerSensorEntityDescription, ...]
ENDPOINT_SENSORS: tuple[PortainerEndpointSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PortainerConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PortainerContainerSensor(PortainerContainerEntity, SensorEntity):
    entity_description: PortainerContainerSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PortainerCoordinator, entity_description: PortainerContainerSensorEntityDescription, device_info: PortainerContainerData, via_device: PortainerCoordinatorData) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> StateType: ...

class PortainerEndpointSensor(PortainerEndpointEntity, SensorEntity):
    entity_description: PortainerEndpointSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PortainerCoordinator, entity_description: PortainerEndpointSensorEntityDescription, device_info: PortainerCoordinatorData) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> StateType: ...
