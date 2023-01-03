from . import ToloSaunaCoordinatorEntity as ToloSaunaCoordinatorEntity, ToloSaunaUpdateCoordinator as ToloSaunaUpdateCoordinator
from .const import DOMAIN as DOMAIN, FAN_TIMER_MAX as FAN_TIMER_MAX, POWER_TIMER_MAX as POWER_TIMER_MAX, SALT_BATH_TIMER_MAX as SALT_BATH_TIMER_MAX
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tololib import ToloClient as ToloClient
from tololib.message_info import SettingsInfo as SettingsInfo
from typing import Any

class ToloNumberEntityDescriptionBase:
    getter: Callable[[SettingsInfo], Union[int, None]]
    setter: Callable[[ToloClient, Union[int, None]], Any]
    def __init__(self, getter, setter) -> None: ...

class ToloNumberEntityDescription(NumberEntityDescription, ToloNumberEntityDescriptionBase):
    entity_category: Incomplete
    native_min_value: int
    native_step: int
    def __init__(self, getter, setter, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, max_value, min_value, native_max_value, native_min_value, native_unit_of_measurement, native_step, step) -> None: ...

NUMBERS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ToloNumberEntity(ToloSaunaCoordinatorEntity, NumberEntity):
    entity_description: ToloNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ConfigEntry, entity_description: ToloNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float: ...
    def set_native_value(self, value: float) -> None: ...
