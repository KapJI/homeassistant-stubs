from . import RadarrEntity as RadarrEntity
from .const import DOMAIN as DOMAIN
from .coordinator import RadarrDataUpdateCoordinator as RadarrDataUpdateCoordinator, T as T
from _typeshed import Incomplete
from aiopyarr import Diskspace as Diskspace, RootFolder as RootFolder
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

def get_space(data: list[Diskspace], name: str) -> str: ...
def get_modified_description(description: RadarrSensorEntityDescription[T], mount: RootFolder) -> tuple[RadarrSensorEntityDescription[T], str]: ...

class RadarrSensorEntityDescriptionMixIn:
    value_fn: Callable[[T, str], Union[str, int, datetime]]
    def __init__(self, value_fn) -> None: ...

class RadarrSensorEntityDescription(SensorEntityDescription, RadarrSensorEntityDescriptionMixIn[T]):
    description_fn: Union[Callable[[RadarrSensorEntityDescription[T], RootFolder], Union[tuple[RadarrSensorEntityDescription[T], str], None]], None]
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_precision, native_unit_of_measurement, options, state_class, suggested_unit_of_measurement, description_fn) -> None: ...

SENSOR_TYPES: dict[str, RadarrSensorEntityDescription[Any]]
BYTE_SIZES: Incomplete
PARALLEL_UPDATES: int

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RadarrSensor(RadarrEntity[T], SensorEntity):
    coordinator: RadarrDataUpdateCoordinator[T]
    entity_description: RadarrSensorEntityDescription[T]
    folder_name: Incomplete
    def __init__(self, coordinator: RadarrDataUpdateCoordinator[T], description: RadarrSensorEntityDescription[T], folder_name: str = ...) -> None: ...
    @property
    def native_value(self) -> Union[str, int, datetime]: ...
