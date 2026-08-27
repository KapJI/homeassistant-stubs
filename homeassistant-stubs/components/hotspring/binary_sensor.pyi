from .coordinator import HotSpringConfigEntry as HotSpringConfigEntry, HotSpringDataUpdateCoordinator as HotSpringDataUpdateCoordinator
from .entity import HotSpringEntity as HotSpringEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from hotspring import Spa as Spa
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class HotSpringBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[Spa], bool | None]

def _is_problem(spa: Spa) -> bool | None: ...

BINARY_SENSORS: tuple[HotSpringBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: HotSpringConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HotSpringBinarySensorEntity(HotSpringEntity, BinarySensorEntity):
    entity_description: HotSpringBinarySensorEntityDescription
    def __init__(self, coordinator: HotSpringDataUpdateCoordinator, description: HotSpringBinarySensorEntityDescription) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
