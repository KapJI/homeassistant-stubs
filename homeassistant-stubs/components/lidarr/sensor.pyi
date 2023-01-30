from . import LidarrEntity as LidarrEntity
from .const import BYTE_SIZES as BYTE_SIZES, DOMAIN as DOMAIN
from .coordinator import LidarrDataUpdateCoordinator as LidarrDataUpdateCoordinator, T as T
from _typeshed import Incomplete
from aiopyarr import LidarrQueueItem as LidarrQueueItem, LidarrRootFolder as LidarrRootFolder
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

def get_space(data: list[LidarrRootFolder], name: str) -> str: ...
def get_modified_description(description: LidarrSensorEntityDescription[T], mount: LidarrRootFolder) -> tuple[LidarrSensorEntityDescription[T], str]: ...

class LidarrSensorEntityDescriptionMixIn:
    value_fn: Callable[[T, str], Union[str, int]]
    def __init__(self, value_fn) -> None: ...

class LidarrSensorEntityDescription(SensorEntityDescription, LidarrSensorEntityDescriptionMixIn[T]):
    attributes_fn: Callable[[T], Union[dict[str, str], None]]
    description_fn: Union[Callable[[LidarrSensorEntityDescription[T], LidarrRootFolder], Union[tuple[LidarrSensorEntityDescription[T], str], None]], None]
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_precision, native_unit_of_measurement, options, state_class, suggested_unit_of_measurement, attributes_fn, description_fn) -> None: ...

SENSOR_TYPES: dict[str, LidarrSensorEntityDescription[Any]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LidarrSensor(LidarrEntity[T], SensorEntity):
    entity_description: LidarrSensorEntityDescription[T]
    folder_name: Incomplete
    def __init__(self, coordinator: LidarrDataUpdateCoordinator[T], description: LidarrSensorEntityDescription[T], folder_name: str = ...) -> None: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, str], None]: ...
    @property
    def native_value(self) -> Union[str, int]: ...

def queue_str(item: LidarrQueueItem) -> str: ...
