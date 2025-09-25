from . import HomeeConfigEntry as HomeeConfigEntry
from .const import DOMAIN as DOMAIN, HOMEE_UNIT_TO_HA_UNIT as HOMEE_UNIT_TO_HA_UNIT, OPEN_CLOSE_MAP as OPEN_CLOSE_MAP, OPEN_CLOSE_MAP_REVERSED as OPEN_CLOSE_MAP_REVERSED, WINDOW_MAP as WINDOW_MAP, WINDOW_MAP_REVERSED as WINDOW_MAP_REVERSED
from .entity import HomeeEntity as HomeeEntity, HomeeNodeEntity as HomeeNodeEntity
from .helpers import get_name_for_enum as get_name_for_enum, setup_homee_platform as setup_homee_platform
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.automation import automations_with_entity as automations_with_entity
from homeassistant.components.script import scripts_with_entity as scripts_with_entity
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue
from pyHomee.const import AttributeType
from pyHomee.model import HomeeAttribute as HomeeAttribute, HomeeNode as HomeeNode

PARALLEL_UPDATES: int

def get_open_close_value(attribute: HomeeAttribute) -> str | None: ...
def get_window_value(attribute: HomeeAttribute) -> str | None: ...
def get_brightness_device_class(attribute: HomeeAttribute, device_class: SensorDeviceClass | None) -> SensorDeviceClass | None: ...

@dataclass(frozen=True, kw_only=True)
class HomeeSensorEntityDescription(SensorEntityDescription):
    device_class_fn: Callable[[HomeeAttribute, SensorDeviceClass | None], SensorDeviceClass | None] = ...
    value_fn: Callable[[HomeeAttribute], str | float | None] = ...
    native_unit_of_measurement_fn: Callable[[str], str | None] = ...

SENSOR_DESCRIPTIONS: dict[AttributeType, HomeeSensorEntityDescription]

@dataclass(frozen=True, kw_only=True)
class HomeeNodeSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[HomeeNode], str | None]

NODE_SENSOR_DESCRIPTIONS: tuple[HomeeNodeSensorEntityDescription, ...]

def entity_used_in(hass: HomeAssistant, entity_id: str) -> list[str]: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: HomeeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeeSensor(HomeeEntity, SensorEntity):
    entity_description: HomeeSensorEntityDescription
    _attr_translation_key: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_device_class: Incomplete
    def __init__(self, attribute: HomeeAttribute, entry: HomeeConfigEntry, description: HomeeSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | str | None: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...

class HomeeNodeSensor(HomeeNodeEntity, SensorEntity):
    entity_description: HomeeNodeSensorEntityDescription
    _node: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, node: HomeeNode, entry: HomeeConfigEntry, description: HomeeNodeSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> str | None: ...
