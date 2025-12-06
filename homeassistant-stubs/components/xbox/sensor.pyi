from .const import DOMAIN as DOMAIN
from .coordinator import XboxConfigEntry as XboxConfigEntry, XboxConsolesCoordinator as XboxConsolesCoordinator
from .entity import MAP_MODEL as MAP_MODEL, XboxBaseEntity as XboxBaseEntity, XboxBaseEntityDescription as XboxBaseEntityDescription, check_deprecated_entity as check_deprecated_entity, to_https as to_https
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from homeassistant.components.sensor import EntityCategory as EntityCategory, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONF_NAME as CONF_NAME, UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pythonxbox.api.provider.people.models import Person as Person
from pythonxbox.api.provider.smartglass.models import SmartglassConsole as SmartglassConsole, StorageDevice as StorageDevice
from pythonxbox.api.provider.titlehub.models import Title as Title
from typing import Any

PARALLEL_UPDATES: int
MAP_JOIN_RESTRICTIONS: Incomplete

class XboxSensor(StrEnum):
    STATUS = 'status'
    GAMER_SCORE = 'gamer_score'
    ACCOUNT_TIER = 'account_tier'
    GOLD_TENURE = 'gold_tenure'
    LAST_ONLINE = 'last_online'
    FOLLOWING = 'following'
    FOLLOWER = 'follower'
    NOW_PLAYING = 'now_playing'
    FRIENDS = 'friends'
    IN_PARTY = 'in_party'
    JOIN_RESTRICTIONS = 'join_restrictions'
    TOTAL_STORAGE = 'total_storage'
    FREE_STORAGE = 'free_storage'

@dataclass(kw_only=True, frozen=True)
class XboxSensorEntityDescription(XboxBaseEntityDescription, SensorEntityDescription):
    value_fn: Callable[[Person, Title | None], StateType | datetime]

@dataclass(kw_only=True, frozen=True)
class XboxStorageDeviceSensorEntityDescription(XboxBaseEntityDescription, SensorEntityDescription):
    value_fn: Callable[[StorageDevice], StateType]

def now_playing_attributes(_: Person, title: Title | None) -> dict[str, Any]: ...
def join_restrictions(person: Person, _: Title | None = None) -> str | None: ...
def title_logo(_: Person, title: Title | None) -> str | None: ...

SENSOR_DESCRIPTIONS: tuple[XboxSensorEntityDescription, ...]
STORAGE_SENSOR_DESCRIPTIONS: tuple[XboxStorageDeviceSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: XboxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class XboxSensorEntity(XboxBaseEntity, SensorEntity):
    entity_description: XboxSensorEntityDescription
    @property
    def native_value(self) -> StateType | datetime: ...

class XboxStorageDeviceSensorEntity(CoordinatorEntity[XboxConsolesCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: XboxStorageDeviceSensorEntityDescription
    client: Incomplete
    _console: Incomplete
    _storage_device: Incomplete
    _attr_unique_id: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, console: SmartglassConsole, storage_device: StorageDevice, coordinator: XboxConsolesCoordinator, entity_description: XboxStorageDeviceSensorEntityDescription) -> None: ...
    @property
    def data(self) -> StorageDevice | None: ...
    @property
    def native_value(self) -> StateType: ...
