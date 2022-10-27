from .const import DOMAIN as DOMAIN
from .coordinator import LaMetricDataUpdateCoordinator as LaMetricDataUpdateCoordinator
from .entity import LaMetricEntity as LaMetricEntity
from .helpers import lametric_exception_handler as lametric_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from demetriek import LaMetricDevice as LaMetricDevice
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class LaMetricButtonEntityDescriptionMixin:
    press_fn: Callable[[LaMetricDevice], Awaitable[Any]]
    def __init__(self, press_fn) -> None: ...

class LaMetricButtonEntityDescription(ButtonEntityDescription, LaMetricButtonEntityDescriptionMixin):
    def __init__(self, press_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement) -> None: ...

BUTTONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMetricButtonEntity(LaMetricEntity, ButtonEntity):
    entity_description: LaMetricButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LaMetricDataUpdateCoordinator, description: LaMetricButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
