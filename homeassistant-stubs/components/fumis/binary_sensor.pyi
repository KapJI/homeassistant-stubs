from .coordinator import FumisConfigEntry as FumisConfigEntry, FumisDataUpdateCoordinator as FumisDataUpdateCoordinator
from .entity import FumisEntity as FumisEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from fumis import FumisInfo as FumisInfo
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class FumisBinarySensorEntityDescription(BinarySensorEntityDescription):
    has_fn: Callable[[FumisInfo], bool] = ...
    is_on_fn: Callable[[FumisInfo], bool | None]

BINARY_SENSORS: tuple[FumisBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: FumisConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FumisBinarySensorEntity(FumisEntity, BinarySensorEntity):
    entity_description: FumisBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FumisDataUpdateCoordinator, description: FumisBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
