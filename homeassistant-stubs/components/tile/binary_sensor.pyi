from .coordinator import TileConfigEntry as TileConfigEntry, TileCoordinator as TileCoordinator
from .entity import TileEntity as TileEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pytile.tile import Tile as Tile

@dataclass(frozen=True, kw_only=True)
class TileBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[Tile], bool]

ENTITIES: tuple[TileBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TileConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TileBinarySensor(TileEntity, BinarySensorEntity):
    entity_description: TileBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: TileCoordinator, description: TileBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
