from .coordinator import RoborockConfigEntry as RoborockConfigEntry, RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .entity import RoborockCoordinatedEntityV1 as RoborockCoordinatedEntityV1
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import ATTR_BATTERY_CHARGING as ATTR_BATTERY_CHARGING, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from roborock.roborock_typing import DeviceProp as DeviceProp

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RoborockBinarySensorDescription(BinarySensorEntityDescription):
    value_fn: Callable[[DeviceProp], bool | int | None]
    is_dock_entity: bool = ...

BINARY_SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RoborockBinarySensorEntity(RoborockCoordinatedEntityV1, BinarySensorEntity):
    entity_description: RoborockBinarySensorDescription
    def __init__(self, coordinator: RoborockDataUpdateCoordinator, description: RoborockBinarySensorDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
