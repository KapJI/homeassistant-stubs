from .const import ACTUATOR as ACTUATOR, DOMAIN as DOMAIN, ENTITY_TYPES as ENTITY_TYPES, FIRMNESS as FIRMNESS, ICON_OCCUPIED as ICON_OCCUPIED
from .coordinator import SleepIQData as SleepIQData, SleepIQDataUpdateCoordinator as SleepIQDataUpdateCoordinator
from .entity import SleepIQBedEntity as SleepIQBedEntity
from _typeshed import Incomplete
from asyncsleepiq import SleepIQActuator as SleepIQActuator, SleepIQBed as SleepIQBed, SleepIQSleeper as SleepIQSleeper
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class SleepIQNumberEntityDescriptionMixin:
    value_fn: Callable[[Any], float]
    set_value_fn: Callable[[Any, int], Coroutine[None, None, None]]
    get_name_fn: Callable[[SleepIQBed, Any], str]
    get_unique_id_fn: Callable[[SleepIQBed, Any], str]
    def __init__(self, value_fn, set_value_fn, get_name_fn, get_unique_id_fn) -> None: ...

class SleepIQNumberEntityDescription(NumberEntityDescription, SleepIQNumberEntityDescriptionMixin):
    def __init__(self, value_fn, set_value_fn, get_name_fn, get_unique_id_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, max_value, min_value, mode, native_max_value, native_min_value, native_step, native_unit_of_measurement, step) -> None: ...

async def _async_set_firmness(sleeper: SleepIQSleeper, firmness: int) -> None: ...
async def _async_set_actuator_position(actuator: SleepIQActuator, position: int) -> None: ...
def _get_actuator_name(bed: SleepIQBed, actuator: SleepIQActuator) -> str: ...
def _get_actuator_unique_id(bed: SleepIQBed, actuator: SleepIQActuator) -> str: ...
def _get_sleeper_name(bed: SleepIQBed, sleeper: SleepIQSleeper) -> str: ...
def _get_sleeper_unique_id(bed: SleepIQBed, sleeper: SleepIQSleeper) -> str: ...

NUMBER_DESCRIPTIONS: dict[str, SleepIQNumberEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SleepIQNumberEntity(SleepIQBedEntity[SleepIQDataUpdateCoordinator], NumberEntity):
    entity_description: SleepIQNumberEntityDescription
    _attr_icon: str
    device: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SleepIQDataUpdateCoordinator, bed: SleepIQBed, device: Any, description: SleepIQNumberEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    def _async_update_attrs(self) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
