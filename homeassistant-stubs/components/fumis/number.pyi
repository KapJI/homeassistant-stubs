from .coordinator import FumisConfigEntry as FumisConfigEntry, FumisDataUpdateCoordinator as FumisDataUpdateCoordinator
from .entity import FumisEntity as FumisEntity
from .helpers import fumis_exception_handler as fumis_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from fumis import Fumis as Fumis, FumisInfo as FumisInfo
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class FumisNumberEntityDescription(NumberEntityDescription):
    has_fn: Callable[[FumisInfo], bool] = ...
    value_fn: Callable[[FumisInfo], float | None]
    set_fn: Callable[[Fumis, float], Awaitable[Any]]

NUMBERS: tuple[FumisNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: FumisConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FumisNumberEntity(FumisEntity, NumberEntity):
    entity_description: FumisNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FumisDataUpdateCoordinator, description: FumisNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    @fumis_exception_handler
    async def async_set_native_value(self, value: float) -> None: ...
