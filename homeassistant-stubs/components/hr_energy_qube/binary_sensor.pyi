from . import QubeConfigEntry as QubeConfigEntry
from .coordinator import QubeCoordinator as QubeCoordinator
from .entity import QubeEntity as QubeEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from python_qube_heatpump.models import QubeState as QubeState

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class QubeBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[QubeState], bool | None]

BINARY_SENSOR_TYPES: tuple[QubeBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: QubeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class QubeBinarySensor(QubeEntity, BinarySensorEntity):
    entity_description: QubeBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: QubeCoordinator, entry: QubeConfigEntry, description: QubeBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
