import datetime
from .coordinator import RoborockConfigEntry as RoborockConfigEntry, RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator, RoborockDataUpdateCoordinatorA01 as RoborockDataUpdateCoordinatorA01
from .entity import RoborockCoordinatedEntityA01 as RoborockCoordinatedEntityA01, RoborockCoordinatedEntityV1 as RoborockCoordinatedEntityV1, RoborockEntity as RoborockEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfArea as UnitOfArea, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from roborock.roborock_message import RoborockDataProtocol, RoborockDyadDataProtocol, RoborockZeoProtocol
from roborock.roborock_typing import DeviceProp as DeviceProp

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RoborockSensorDescription(SensorEntityDescription):
    value_fn: Callable[[DeviceProp], StateType | datetime.datetime]
    protocol_listener: RoborockDataProtocol | None = ...
    is_dock_entity: bool = ...

@dataclass(frozen=True, kw_only=True)
class RoborockSensorDescriptionA01(SensorEntityDescription):
    data_protocol: RoborockDyadDataProtocol | RoborockZeoProtocol

def _dock_error_value_fn(properties: DeviceProp) -> str | None: ...

SENSOR_DESCRIPTIONS: Incomplete
A01_SENSOR_DESCRIPTIONS: list[RoborockSensorDescriptionA01]

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RoborockSensorEntity(RoborockCoordinatedEntityV1, SensorEntity):
    entity_description: RoborockSensorDescription
    def __init__(self, coordinator: RoborockDataUpdateCoordinator, description: RoborockSensorDescription) -> None: ...
    @property
    def native_value(self) -> StateType | datetime.datetime: ...

class RoborockCurrentRoom(RoborockCoordinatedEntityV1, SensorEntity):
    _attr_device_class: Incomplete
    _attr_translation_key: str
    _attr_entity_category: Incomplete
    def __init__(self, coordinator: RoborockDataUpdateCoordinator) -> None: ...
    @property
    def options(self) -> list[str]: ...
    @property
    def native_value(self) -> str | None: ...

class RoborockSensorEntityA01(RoborockCoordinatedEntityA01, SensorEntity):
    entity_description: RoborockSensorDescriptionA01
    def __init__(self, coordinator: RoborockDataUpdateCoordinatorA01, description: RoborockSensorDescriptionA01) -> None: ...
    @property
    def native_value(self) -> StateType: ...
