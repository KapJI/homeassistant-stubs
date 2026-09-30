from .coordinator import LibrenmsCentralData as LibrenmsCentralData, LibrenmsCentralDataUpdateCoordinator as LibrenmsCentralDataUpdateCoordinator, LibrenmsConfigEntry as LibrenmsConfigEntry
from .entity import LibrenmsSystemEntity as LibrenmsSystemEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LibrenmsSystemSensorEntityDescription(SensorEntityDescription):
    value: Callable[[LibrenmsCentralData], StateType]
    is_suitable: Callable[[LibrenmsCentralData], bool] = ...

SYSTEM_SENSOR_TYPES: tuple[LibrenmsSystemSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LibrenmsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LibrenmsSystemSensorEntity(LibrenmsSystemEntity, SensorEntity):
    entity_description: LibrenmsSystemSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LibrenmsCentralDataUpdateCoordinator, description: LibrenmsSystemSensorEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> StateType: ...
