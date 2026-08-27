from .coordinator import ActronAirConfigEntry as ActronAirConfigEntry, ActronAirSystemCoordinator as ActronAirSystemCoordinator
from .entity import ActronAirAcEntity as ActronAirAcEntity
from _typeshed import Incomplete
from actron_neo_api import ActronAirStatus as ActronAirStatus
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ActronAirBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[ActronAirStatus], bool]

BINARY_SENSORS: tuple[ActronAirBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ActronAirConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ActronAirBinarySensor(ActronAirAcEntity, BinarySensorEntity):
    entity_description: ActronAirBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ActronAirSystemCoordinator, description: ActronAirBinarySensorEntityDescription) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
