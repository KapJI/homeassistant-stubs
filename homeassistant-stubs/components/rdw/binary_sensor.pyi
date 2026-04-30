from .coordinator import RDWConfigEntry as RDWConfigEntry, RDWDataUpdateCoordinator as RDWDataUpdateCoordinator
from .entity import RDWEntity as RDWEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from vehicle import Vehicle as Vehicle

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RDWBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[Vehicle], bool | None]

BINARY_SENSORS: tuple[RDWBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: RDWConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RDWBinarySensorEntity(RDWEntity, BinarySensorEntity):
    entity_description: RDWBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: RDWDataUpdateCoordinator, description: RDWBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
