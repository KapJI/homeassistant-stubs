from . import PortainerConfigEntry as PortainerConfigEntry
from .const import CONTAINER_STATE_RUNNING as CONTAINER_STATE_RUNNING, STACK_STATUS_ACTIVE as STACK_STATUS_ACTIVE
from .coordinator import PortainerContainerData as PortainerContainerData
from .entity import PortainerContainerEntity as PortainerContainerEntity, PortainerCoordinatorData as PortainerCoordinatorData, PortainerEndpointEntity as PortainerEndpointEntity, PortainerStackData as PortainerStackData, PortainerStackEntity as PortainerStackEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PortainerContainerBinarySensorEntityDescription(BinarySensorEntityDescription):
    state_fn: Callable[[PortainerContainerData], bool | None]

@dataclass(frozen=True, kw_only=True)
class PortainerEndpointBinarySensorEntityDescription(BinarySensorEntityDescription):
    state_fn: Callable[[PortainerCoordinatorData], bool | None]

@dataclass(frozen=True, kw_only=True)
class PortainerStackBinarySensorEntityDescription(BinarySensorEntityDescription):
    state_fn: Callable[[PortainerStackData], bool | None]

CONTAINER_SENSORS: tuple[PortainerContainerBinarySensorEntityDescription, ...]
ENDPOINT_SENSORS: tuple[PortainerEndpointBinarySensorEntityDescription, ...]
STACK_SENSORS: tuple[PortainerStackBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PortainerConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PortainerEndpointSensor(PortainerEndpointEntity, BinarySensorEntity):
    entity_description: PortainerEndpointBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...

class PortainerContainerSensor(PortainerContainerEntity, BinarySensorEntity):
    entity_description: PortainerContainerBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...

class PortainerStackSensor(PortainerStackEntity, BinarySensorEntity):
    entity_description: PortainerStackBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...
