from .const import DOMAIN as DOMAIN
from .coordinator import LaMetricDataUpdateCoordinator as LaMetricDataUpdateCoordinator
from .entity import LaMetricEntity as LaMetricEntity
from .helpers import lametric_exception_handler as lametric_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from demetriek import Device as Device, LaMetricDevice as LaMetricDevice
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class LaMetricEntityDescriptionMixin:
    current_fn: Callable[[Device], str]
    select_fn: Callable[[LaMetricDevice, str], Awaitable[Any]]
    def __init__(self, current_fn, select_fn) -> None: ...

class LaMetricSelectEntityDescription(SelectEntityDescription, LaMetricEntityDescriptionMixin):
    def __init__(self, current_fn, select_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, options) -> None: ...

SELECTS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMetricSelectEntity(LaMetricEntity, SelectEntity):
    entity_description: LaMetricSelectEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LaMetricDataUpdateCoordinator, description: LaMetricSelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> Union[str, None]: ...
    async def async_select_option(self, option: str) -> None: ...
