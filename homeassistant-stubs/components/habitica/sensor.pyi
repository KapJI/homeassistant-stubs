from .const import ASSETS_URL as ASSETS_URL, DOMAIN as DOMAIN
from .coordinator import HabiticaConfigEntry as HabiticaConfigEntry, HabiticaDataUpdateCoordinator as HabiticaDataUpdateCoordinator
from .entity import HabiticaBase as HabiticaBase
from .util import get_attribute_points as get_attribute_points, get_attributes_total as get_attributes_total, inventory_list as inventory_list
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from enum import StrEnum
from habiticalib import ContentData as ContentData, TaskData as TaskData, UserData as UserData
from homeassistant.components.automation import automations_with_entity as automations_with_entity
from homeassistant.components.script import scripts_with_entity as scripts_with_entity
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue
from homeassistant.helpers.typing import StateType as StateType
from typing import Any

_LOGGER: Incomplete
SVG_CLASS: Incomplete
PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class HabiticaSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[UserData, ContentData], StateType]
    attributes_fn: Callable[[UserData, ContentData], dict[str, Any] | None] | None = ...
    entity_picture: str | None = ...

@dataclass(kw_only=True, frozen=True)
class HabiticaTaskSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[list[TaskData]], list[TaskData]]

class HabiticaSensorEntity(StrEnum):
    DISPLAY_NAME = 'display_name'
    HEALTH = 'health'
    HEALTH_MAX = 'health_max'
    MANA = 'mana'
    MANA_MAX = 'mana_max'
    EXPERIENCE = 'experience'
    EXPERIENCE_MAX = 'experience_max'
    LEVEL = 'level'
    GOLD = 'gold'
    CLASS = 'class'
    HABITS = 'habits'
    REWARDS = 'rewards'
    GEMS = 'gems'
    TRINKETS = 'trinkets'
    STRENGTH = 'strength'
    INTELLIGENCE = 'intelligence'
    CONSTITUTION = 'constitution'
    PERCEPTION = 'perception'
    EGGS_TOTAL = 'eggs_total'
    HATCHING_POTIONS_TOTAL = 'hatching_potions_total'
    FOOD_TOTAL = 'food_total'
    SADDLE = 'saddle'
    QUEST_SCROLLS = 'quest_scrolls'

SENSOR_DESCRIPTIONS: tuple[HabiticaSensorEntityDescription, ...]
TASKS_MAP_ID: str
TASKS_MAP: Incomplete
TASK_SENSOR_DESCRIPTION: tuple[HabiticaTaskSensorEntityDescription, ...]

def entity_used_in(hass: HomeAssistant, entity_id: str) -> list[str]: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: HabiticaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HabiticaSensor(HabiticaBase, SensorEntity):
    entity_description: HabiticaSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> dict[str, float | None] | None: ...
    @property
    def entity_picture(self) -> str | None: ...

class HabiticaTaskSensor(HabiticaBase, SensorEntity):
    entity_description: HabiticaTaskSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
