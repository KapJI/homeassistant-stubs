from .coordinator import FumisConfigEntry as FumisConfigEntry, FumisDataUpdateCoordinator as FumisDataUpdateCoordinator
from .entity import FumisEntity as FumisEntity
from .helpers import fumis_exception_handler as fumis_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from fumis import Fumis as Fumis, FumisInfo as FumisInfo
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class FumisSwitchEntityDescription(SwitchEntityDescription):
    has_fn: Callable[[FumisInfo], bool] = ...
    is_on_fn: Callable[[FumisInfo], bool]
    turn_on_fn: Callable[[Fumis], Awaitable[Any]]
    turn_off_fn: Callable[[Fumis], Awaitable[Any]]

SWITCHES: tuple[FumisSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: FumisConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FumisSwitchEntity(FumisEntity, SwitchEntity):
    entity_description: FumisSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FumisDataUpdateCoordinator, description: FumisSwitchEntityDescription) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
    @fumis_exception_handler
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @fumis_exception_handler
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
