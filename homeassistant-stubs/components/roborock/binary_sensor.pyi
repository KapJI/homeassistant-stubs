from .coordinator import RoborockConfigEntry as RoborockConfigEntry, RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator, RoborockDataUpdateCoordinatorA01 as RoborockDataUpdateCoordinatorA01, RoborockWashingMachineUpdateCoordinator as RoborockWashingMachineUpdateCoordinator
from .entity import RoborockCoordinatedEntityA01 as RoborockCoordinatedEntityA01, RoborockCoordinatedEntityV1 as RoborockCoordinatedEntityV1
from .models import DeviceState as DeviceState
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import ATTR_BATTERY_CHARGING as ATTR_BATTERY_CHARGING, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from roborock.roborock_message import RoborockZeoProtocol

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RoborockBinarySensorDescription(BinarySensorEntityDescription):
    value_fn: Callable[[DeviceState], bool | int | None]
    is_dock_entity: bool = ...

@dataclass(frozen=True, kw_only=True)
class RoborockBinarySensorDescriptionA01(BinarySensorEntityDescription):
    data_protocol: RoborockZeoProtocol
    value_fn: Callable[[StateType], bool]

BINARY_SENSOR_DESCRIPTIONS: Incomplete
ZEO_BINARY_SENSOR_DESCRIPTIONS: list[RoborockBinarySensorDescriptionA01]

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RoborockBinarySensorEntity(RoborockCoordinatedEntityV1, BinarySensorEntity):
    entity_description: RoborockBinarySensorDescription
    def __init__(self, coordinator: RoborockDataUpdateCoordinator, description: RoborockBinarySensorDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...

class RoborockBinarySensorEntityA01(RoborockCoordinatedEntityA01, BinarySensorEntity):
    entity_description: RoborockBinarySensorDescriptionA01
    def __init__(self, coordinator: RoborockDataUpdateCoordinatorA01, description: RoborockBinarySensorDescriptionA01) -> None: ...
    @property
    def is_on(self) -> bool: ...
