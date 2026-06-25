from . import IndevoltConfigEntry as IndevoltConfigEntry
from .coordinator import IndevoltCoordinator as IndevoltCoordinator
from .entity import IndevoltEntity as IndevoltEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class IndevoltBinarySensorEntityDescription(BinarySensorEntityDescription):
    on_value: int = ...
    off_value: int = ...
    generation: tuple[int, ...] = ...

BINARY_SENSORS: Final[Incomplete]
BATTERY_PACK_SENSOR_KEYS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: IndevoltConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IndevoltBinarySensorEntity(IndevoltEntity, BinarySensorEntity):
    entity_description: IndevoltBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: IndevoltCoordinator, description: IndevoltBinarySensorEntityDescription) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
