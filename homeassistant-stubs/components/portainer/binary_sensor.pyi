from . import PortainerConfigEntry as PortainerConfigEntry
from .coordinator import PortainerContainerData as PortainerContainerData, PortainerCoordinator as PortainerCoordinator
from .entity import PortainerContainerEntity as PortainerContainerEntity, PortainerCoordinatorData as PortainerCoordinatorData, PortainerEndpointEntity as PortainerEndpointEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class PortainerContainerBinarySensorEntityDescription(BinarySensorEntityDescription):
    state_fn: Callable[[PortainerContainerData], bool | None]

@dataclass(frozen=True, kw_only=True)
class PortainerEndpointBinarySensorEntityDescription(BinarySensorEntityDescription):
    state_fn: Callable[[PortainerCoordinatorData], bool | None]

CONTAINER_SENSORS: tuple[PortainerContainerBinarySensorEntityDescription, ...]
ENDPOINT_SENSORS: tuple[PortainerEndpointBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PortainerConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PortainerEndpointSensor(PortainerEndpointEntity, BinarySensorEntity):
    entity_description: PortainerEndpointBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PortainerCoordinator, entity_description: PortainerEndpointBinarySensorEntityDescription, device_info: PortainerCoordinatorData) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool | None: ...

class PortainerContainerSensor(PortainerContainerEntity, BinarySensorEntity):
    entity_description: PortainerContainerBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PortainerCoordinator, entity_description: PortainerContainerBinarySensorEntityDescription, device_info: PortainerContainerData, via_device: PortainerCoordinatorData) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool | None: ...
