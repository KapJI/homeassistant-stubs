from . import AutomowerConfigEntry as AutomowerConfigEntry
from .const import EXECUTION_TIME_DELAY as EXECUTION_TIME_DELAY
from .coordinator import AutomowerDataUpdateCoordinator as AutomowerDataUpdateCoordinator
from .entity import AutomowerControlEntity as AutomowerControlEntity
from _typeshed import Incomplete
from aioautomower.model import MowerAttributes as MowerAttributes, WorkArea as WorkArea
from aioautomower.session import AutomowerSession as AutomowerSession
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

def _async_get_cutting_height(data: MowerAttributes) -> int: ...
def _work_area_translation_key(work_area_id: int) -> str: ...
async def async_set_work_area_cutting_height(coordinator: AutomowerDataUpdateCoordinator, mower_id: str, cheight: float, work_area_id: int) -> None: ...
async def async_set_cutting_height(session: AutomowerSession, mower_id: str, cheight: float) -> None: ...

@dataclass(frozen=True, kw_only=True)
class AutomowerNumberEntityDescription(NumberEntityDescription):
    exists_fn: Callable[[MowerAttributes], bool] = ...
    value_fn: Callable[[MowerAttributes], int]
    set_value_fn: Callable[[AutomowerSession, str, float], Awaitable[Any]]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, max_value, min_value, mode, native_max_value, native_min_value, native_step, native_unit_of_measurement, step, exists_fn, value_fn, set_value_fn) -> None: ...

NUMBER_TYPES: tuple[AutomowerNumberEntityDescription, ...]

@dataclass(frozen=True, kw_only=True)
class AutomowerWorkAreaNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[WorkArea], int]
    translation_key_fn: Callable[[int], str]
    set_value_fn: Callable[[AutomowerDataUpdateCoordinator, str, float, int], Awaitable[Any]]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, max_value, min_value, mode, native_max_value, native_min_value, native_step, native_unit_of_measurement, step, value_fn, translation_key_fn, set_value_fn) -> None: ...

WORK_AREA_NUMBER_TYPES: tuple[AutomowerWorkAreaNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AutomowerConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AutomowerNumberEntity(AutomowerControlEntity, NumberEntity):
    entity_description: AutomowerNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator, description: AutomowerNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...

class AutomowerWorkAreaNumberEntity(AutomowerControlEntity, NumberEntity):
    entity_description: AutomowerWorkAreaNumberEntityDescription
    work_area_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator, description: AutomowerWorkAreaNumberEntityDescription, work_area_id: int) -> None: ...
    @property
    def work_area(self) -> WorkArea: ...
    @property
    def translation_key(self) -> str: ...
    @property
    def native_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...

def async_remove_entities(hass: HomeAssistant, coordinator: AutomowerDataUpdateCoordinator, entry: AutomowerConfigEntry, mower_id: str) -> None: ...
