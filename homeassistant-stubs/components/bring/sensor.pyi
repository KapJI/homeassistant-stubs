from .coordinator import BringConfigEntry as BringConfigEntry, BringData as BringData, BringDataUpdateCoordinator as BringDataUpdateCoordinator
from .entity import BringBaseEntity as BringBaseEntity
from .util import list_language as list_language, sum_attributes as sum_attributes
from _typeshed import Incomplete
from bring_api import BringList as BringList, BringUserSettingsResponse as BringUserSettingsResponse
from collections.abc import Callable as Callable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class BringSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[BringData, BringUserSettingsResponse], StateType]

class BringSensor(StrEnum):
    URGENT = 'urgent'
    CONVENIENT = 'convenient'
    DISCOUNTED = 'discounted'
    LIST_LANGUAGE = 'list_language'
    LIST_ACCESS = 'list_access'

SENSOR_DESCRIPTIONS: tuple[BringSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: BringConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BringSensorEntity(BringBaseEntity, SensorEntity):
    entity_description: BringSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: BringDataUpdateCoordinator, bring_list: BringList, entity_description: BringSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
