from . import PortainerConfigEntry as PortainerConfigEntry
from .coordinator import PortainerCoordinator as PortainerCoordinator
from .entity import PortainerContainerEntity as PortainerContainerEntity, PortainerCoordinatorData as PortainerCoordinatorData, PortainerEndpointEntity as PortainerEndpointEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyportainer.models.docker import DockerContainer as DockerContainer
from typing import Any

@dataclass(frozen=True, kw_only=True)
class PortainerBinarySensorEntityDescription(BinarySensorEntityDescription):
    state_fn: Callable[[Any], bool]

CONTAINER_SENSORS: tuple[PortainerBinarySensorEntityDescription, ...]
ENDPOINT_SENSORS: tuple[PortainerBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PortainerConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PortainerEndpointSensor(PortainerEndpointEntity, BinarySensorEntity):
    entity_description: PortainerBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PortainerCoordinator, entity_description: PortainerBinarySensorEntityDescription, device_info: PortainerCoordinatorData) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool | None: ...

class PortainerContainerSensor(PortainerContainerEntity, BinarySensorEntity):
    entity_description: PortainerBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PortainerCoordinator, entity_description: PortainerBinarySensorEntityDescription, device_info: DockerContainer, via_device: PortainerCoordinatorData) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool | None: ...
