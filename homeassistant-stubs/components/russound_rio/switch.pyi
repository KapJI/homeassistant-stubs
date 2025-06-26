from . import RussoundConfigEntry as RussoundConfigEntry
from .entity import RussoundBaseEntity as RussoundBaseEntity, command as command
from _typeshed import Incomplete
from aiorussound.rio import Controller as Controller, ZoneControlSurface as ZoneControlSurface
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RussoundZoneSwitchEntityDescription(SwitchEntityDescription):
    value_fn: Callable[[ZoneControlSurface], bool]
    set_value_fn: Callable[[ZoneControlSurface, bool], Awaitable[None]]

CONTROL_ENTITIES: tuple[RussoundZoneSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: RussoundConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RussoundSwitchEntity(RussoundBaseEntity, SwitchEntity):
    entity_description: RussoundZoneSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, controller: Controller, zone_id: int, description: RussoundZoneSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @command
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @command
    async def async_turn_off(self, **kwargs: Any) -> None: ...
