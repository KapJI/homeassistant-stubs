from . import AutomowerConfigEntry as AutomowerConfigEntry
from .coordinator import AutomowerDataUpdateCoordinator as AutomowerDataUpdateCoordinator
from .entity import AutomowerBaseEntity as AutomowerBaseEntity, WorkAreaAvailableEntity as WorkAreaAvailableEntity, _work_area_translation_key as _work_area_translation_key
from _typeshed import Incomplete
from aioautomower.model import MowerAttributes as MowerAttributes, WorkArea as WorkArea
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfLength as UnitOfLength, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any

_LOGGER: Incomplete
ATTR_WORK_AREA_ID_ASSIGNMENT: str
ERROR_KEY_LIST: Incomplete
ERROR_STATES: Incomplete
RESTRICTED_REASONS: list
STATE_NO_WORK_AREA_ACTIVE: str

def _get_work_area_names(data: MowerAttributes) -> list[str]: ...
def _get_current_work_area_name(data: MowerAttributes) -> str: ...
def _get_current_work_area_dict(data: MowerAttributes) -> Mapping[str, Any]: ...
def _get_error_string(data: MowerAttributes) -> str: ...

@dataclass(frozen=True, kw_only=True)
class AutomowerSensorEntityDescription(SensorEntityDescription):
    exists_fn: Callable[[MowerAttributes], bool] = ...
    extra_state_attributes_fn: Callable[[MowerAttributes], Mapping[str, Any] | None] = ...
    option_fn: Callable[[MowerAttributes], list[str] | None] = ...
    value_fn: Callable[[MowerAttributes], StateType | datetime]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., exists_fn=..., extra_state_attributes_fn=..., option_fn=..., value_fn) -> None: ...

MOWER_SENSOR_TYPES: tuple[AutomowerSensorEntityDescription, ...]

@dataclass(frozen=True, kw_only=True)
class WorkAreaSensorEntityDescription(SensorEntityDescription):
    exists_fn: Callable[[WorkArea], bool] = ...
    value_fn: Callable[[WorkArea], StateType | datetime]
    translation_key_fn: Callable[[int, str], str]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., exists_fn=..., value_fn, translation_key_fn) -> None: ...

WORK_AREA_SENSOR_TYPES: tuple[WorkAreaSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AutomowerConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AutomowerSensorEntity(AutomowerBaseEntity, SensorEntity):
    entity_description: AutomowerSensorEntityDescription
    _unrecorded_attributes: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator, description: AutomowerSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType | datetime: ...
    @property
    def options(self) -> list[str] | None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...

class WorkAreaSensorEntity(WorkAreaAvailableEntity, SensorEntity):
    entity_description: WorkAreaSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator, description: WorkAreaSensorEntityDescription, work_area_id: int) -> None: ...
    @property
    def native_value(self) -> StateType | datetime: ...
    @property
    def translation_key(self) -> str: ...
