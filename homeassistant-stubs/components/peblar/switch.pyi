from .coordinator import PeblarConfigEntry as PeblarConfigEntry, PeblarData as PeblarData, PeblarDataUpdateCoordinator as PeblarDataUpdateCoordinator, PeblarRuntimeData as PeblarRuntimeData, PeblarUserConfigurationDataUpdateCoordinator as PeblarUserConfigurationDataUpdateCoordinator
from .entity import PeblarEntity as PeblarEntity
from .helpers import peblar_exception_handler as peblar_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from peblar import Peblar as Peblar, PeblarEVInterface as PeblarEVInterface, PeblarUserConfiguration as PeblarUserConfiguration
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PeblarSwitchEntityDescription(SwitchEntityDescription):
    has_fn: Callable[[PeblarRuntimeData], bool] = ...
    is_on_fn: Callable[[PeblarData], bool]
    set_fn: Callable[[PeblarDataUpdateCoordinator, bool], Awaitable[Any]]

@dataclass(frozen=True, kw_only=True)
class PeblarUserConfigSwitchEntityDescription(SwitchEntityDescription):
    has_fn: Callable[[PeblarRuntimeData], bool] = ...
    is_on_fn: Callable[[PeblarUserConfiguration], bool]
    set_fn: Callable[[Peblar, bool], Awaitable[Any]]

def _async_peblar_charge(coordinator: PeblarDataUpdateCoordinator, on: bool) -> Awaitable[PeblarEVInterface]: ...

DATA_DESCRIPTIONS: Incomplete
USER_CONFIG_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PeblarConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PeblarSwitchEntity(PeblarEntity[PeblarDataUpdateCoordinator], SwitchEntity):
    entity_description: PeblarSwitchEntityDescription
    @property
    @override
    def is_on(self) -> bool: ...
    @peblar_exception_handler
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @peblar_exception_handler
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class PeblarUserConfigSwitchEntity(PeblarEntity[PeblarUserConfigurationDataUpdateCoordinator], SwitchEntity):
    entity_description: PeblarUserConfigSwitchEntityDescription
    @property
    @override
    def is_on(self) -> bool: ...
    @peblar_exception_handler
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @peblar_exception_handler
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
