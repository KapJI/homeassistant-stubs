from .coordinator import LaMetricConfigEntry as LaMetricConfigEntry, LaMetricDataUpdateCoordinator as LaMetricDataUpdateCoordinator
from .entity import LaMetricEntity as LaMetricEntity
from .helpers import lametric_exception_handler as lametric_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from demetriek import LaMetricDevice as LaMetricDevice
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class LaMetricButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[LaMetricDevice], Awaitable[Any]]

BUTTONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LaMetricConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LaMetricButtonEntity(LaMetricEntity, ButtonEntity):
    entity_description: LaMetricButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LaMetricDataUpdateCoordinator, description: LaMetricButtonEntityDescription) -> None: ...
    @lametric_exception_handler
    async def async_press(self) -> None: ...
