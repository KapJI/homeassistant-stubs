from .coordinator import OpenEVSEConfigEntry as OpenEVSEConfigEntry
from .entity import OpenEVSEEntity as OpenEVSEEntity
from .helpers import openevse_exception_handler as openevse_exception_handler
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from openevsehttp import OpenEVSE as OpenEVSE
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OpenEVSESwitchDescription(SwitchEntityDescription):
    is_on_fn: Callable[[OpenEVSE], bool | None]
    turn_on_fn: Callable[[OpenEVSE], Awaitable[Any]]
    turn_off_fn: Callable[[OpenEVSE], Awaitable[Any]]

SWITCH_TYPES: tuple[OpenEVSESwitchDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: OpenEVSEConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpenEVSESwitch(OpenEVSEEntity, SwitchEntity):
    entity_description: OpenEVSESwitchDescription
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
