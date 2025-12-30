import datetime
from .coordinator import RoborockConfigEntry as RoborockConfigEntry, RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator, RoborockDataUpdateCoordinatorA01 as RoborockDataUpdateCoordinatorA01, RoborockDataUpdateCoordinatorB01 as RoborockDataUpdateCoordinatorB01
from .entity import RoborockCoordinatedEntityA01 as RoborockCoordinatedEntityA01, RoborockCoordinatedEntityB01 as RoborockCoordinatedEntityB01, RoborockCoordinatedEntityV1 as RoborockCoordinatedEntityV1, RoborockEntity as RoborockEntity
from .models import DeviceState as DeviceState
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfArea as UnitOfArea, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from roborock.data import B01Props as B01Props
from roborock.roborock_message import RoborockDyadDataProtocol, RoborockZeoProtocol

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RoborockSensorDescription(SensorEntityDescription):
    value_fn: Callable[[DeviceState], StateType | datetime.datetime]
    is_dock_entity: bool = ...

@dataclass(frozen=True, kw_only=True)
class RoborockSensorDescriptionA01(SensorEntityDescription):
    data_protocol: RoborockDyadDataProtocol | RoborockZeoProtocol

@dataclass(frozen=True, kw_only=True)
class RoborockSensorDescriptionB01(SensorEntityDescription):
    value_fn: Callable[[B01Props], StateType]

def _dock_error_value_fn(state: DeviceState) -> str | None: ...

SENSOR_DESCRIPTIONS: Incomplete
A01_SENSOR_DESCRIPTIONS: list[RoborockSensorDescriptionA01]
Q7_B01_SENSOR_DESCRIPTIONS: Incomplete

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
    _home_trait: Incomplete
    _map_content_trait: Incomplete
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

class RoborockSensorEntityB01(RoborockCoordinatedEntityB01, SensorEntity):
    entity_description: RoborockSensorDescriptionB01
    def __init__(self, coordinator: RoborockDataUpdateCoordinatorB01, description: RoborockSensorDescriptionB01) -> None: ...
    @property
    def native_value(self) -> StateType: ...
