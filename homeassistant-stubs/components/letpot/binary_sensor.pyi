from .coordinator import LetPotConfigEntry as LetPotConfigEntry, LetPotDeviceCoordinator as LetPotDeviceCoordinator
from .entity import LetPotEntity as LetPotEntity, LetPotEntityDescription as LetPotEntityDescription
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from letpot.models import LetPotDeviceStatus as LetPotDeviceStatus

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LetPotBinarySensorEntityDescription(LetPotEntityDescription, BinarySensorEntityDescription):
    is_on_fn: Callable[[LetPotDeviceStatus], bool]

BINARY_SENSORS: tuple[LetPotBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LetPotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LetPotBinarySensorEntity(LetPotEntity, BinarySensorEntity):
    entity_description: LetPotBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LetPotDeviceCoordinator, description: LetPotBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
