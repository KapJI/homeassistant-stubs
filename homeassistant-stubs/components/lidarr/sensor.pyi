import dataclasses
from . import LidarrConfigEntry as LidarrConfigEntry
from .const import BYTE_SIZES as BYTE_SIZES
from .coordinator import LidarrDataUpdateCoordinator as LidarrDataUpdateCoordinator, T as T
from .entity import LidarrEntity as LidarrEntity
from _typeshed import Incomplete
from aiopyarr import LidarrQueueItem as LidarrQueueItem, LidarrRootFolder as LidarrRootFolder
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Generic

def get_space(data: list[LidarrRootFolder], name: str) -> str: ...
def get_modified_description(description: LidarrSensorEntityDescription[T], mount: LidarrRootFolder) -> tuple[LidarrSensorEntityDescription[T], str]: ...

@dataclasses.dataclass(frozen=True)
class LidarrSensorEntityDescriptionMixIn(Generic[T]):
    value_fn: Callable[[T, str], str | int]
    def __init__(self, value_fn) -> None: ...

@dataclasses.dataclass(frozen=True)
class LidarrSensorEntityDescription(SensorEntityDescription, LidarrSensorEntityDescriptionMixIn[T], Generic[T]):
    attributes_fn: Callable[[T], dict[str, str] | None] = ...
    description_fn: Callable[[LidarrSensorEntityDescription[T], LidarrRootFolder], tuple[LidarrSensorEntityDescription[T], str] | None] | None = ...
    def __init__(self, value_fn, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., attributes_fn=..., description_fn=...) -> None: ...

SENSOR_TYPES: dict[str, LidarrSensorEntityDescription[Any]]

async def async_setup_entry(hass: HomeAssistant, entry: LidarrConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LidarrSensor(LidarrEntity[T], SensorEntity):
    entity_description: LidarrSensorEntityDescription[T]
    folder_name: Incomplete
    def __init__(self, coordinator: LidarrDataUpdateCoordinator[T], description: LidarrSensorEntityDescription[T], folder_name: str = '') -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str] | None: ...
    @property
    def native_value(self) -> str | int: ...

def queue_str(item: LidarrQueueItem) -> str: ...
