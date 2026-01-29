from . import LeilSaunaConfigEntry as LeilSaunaConfigEntry
from .coordinator import LeilSaunaCoordinator as LeilSaunaCoordinator
from .entity import LeilSaunaEntity as LeilSaunaEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pysaunum import SaunumData as SaunumData

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LeilSaunaBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[SaunumData], bool | None]

BINARY_SENSORS: tuple[LeilSaunaBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LeilSaunaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LeilSaunaBinarySensorEntity(LeilSaunaEntity, BinarySensorEntity):
    entity_description: LeilSaunaBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LeilSaunaCoordinator, description: LeilSaunaBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
