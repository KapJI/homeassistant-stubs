from .const import DOMAIN as DOMAIN
from .coordinator import LaMetricDataUpdateCoordinator as LaMetricDataUpdateCoordinator
from .entity import LaMetricEntity as LaMetricEntity
from .helpers import lametric_exception_handler as lametric_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from demetriek import Device as Device, LaMetricDevice as LaMetricDevice
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class LaMetricEntityDescriptionMixin:
    value_fn: Callable[[Device], Union[int, None]]
    set_value_fn: Callable[[LaMetricDevice, float], Awaitable[Any]]
    def __init__(self, value_fn, set_value_fn) -> None: ...

class LaMetricNumberEntityDescription(NumberEntityDescription, LaMetricEntityDescriptionMixin):
    def __init__(self, value_fn, set_value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, max_value, min_value, native_max_value, native_min_value, native_unit_of_measurement, native_step, step) -> None: ...

NUMBERS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMetricNumberEntity(LaMetricEntity, NumberEntity):
    entity_description: LaMetricNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LaMetricDataUpdateCoordinator, description: LaMetricNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[int, None]: ...
    async def async_set_native_value(self, value: float) -> None: ...
