from .coordinator import LaMetricConfigEntry as LaMetricConfigEntry, LaMetricDataUpdateCoordinator as LaMetricDataUpdateCoordinator
from .entity import LaMetricEntity as LaMetricEntity
from .helpers import lametric_exception_handler as lametric_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from demetriek import Device as Device, LaMetricDevice as LaMetricDevice
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class LaMetricSelectEntityDescription(SelectEntityDescription):
    current_fn: Callable[[Device], str]
    select_fn: Callable[[LaMetricDevice, str], Awaitable[Any]]

SELECTS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LaMetricConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LaMetricSelectEntity(LaMetricEntity, SelectEntity):
    entity_description: LaMetricSelectEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LaMetricDataUpdateCoordinator, description: LaMetricSelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    @lametric_exception_handler
    async def async_select_option(self, option: str) -> None: ...
