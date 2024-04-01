from . import ToloSaunaCoordinatorEntity as ToloSaunaCoordinatorEntity, ToloSaunaUpdateCoordinator as ToloSaunaUpdateCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tololib import ToloClient as ToloClient, ToloSettings as ToloSettings
from typing import Any

@dataclass(frozen=True, kw_only=True)
class ToloNumberEntityDescription(NumberEntityDescription):
    getter: Callable[[ToloSettings], int | None]
    setter: Callable[[ToloClient, int | None], Any]
    entity_category = ...
    native_min_value = ...
    native_step = ...
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, max_value, min_value, mode, native_max_value, native_min_value, native_step, native_unit_of_measurement, step, getter, setter) -> None: ...

NUMBERS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ToloNumberEntity(ToloSaunaCoordinatorEntity, NumberEntity):
    entity_description: ToloNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ConfigEntry, entity_description: ToloNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float: ...
    def set_native_value(self, value: float) -> None: ...
