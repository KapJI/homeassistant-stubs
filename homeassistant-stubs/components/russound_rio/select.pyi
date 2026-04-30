from . import RussoundConfigEntry as RussoundConfigEntry
from .entity import RussoundBaseEntity as RussoundBaseEntity, command as command
from _typeshed import Incomplete
from aiorussound.rio.client import Controller as Controller, ZoneControlSurface as ZoneControlSurface
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RussoundZoneSelectEntityDescription(SelectEntityDescription):
    value_fn: Callable[[ZoneControlSurface], str | None]
    set_value_fn: Callable[[ZoneControlSurface, str], Awaitable[None]]

CONTROL_ENTITIES: tuple[RussoundZoneSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: RussoundConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RussoundSelectEntity(RussoundBaseEntity, SelectEntity):
    entity_description: RussoundZoneSelectEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, controller: Controller, zone_id: int, description: RussoundZoneSelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    @command
    async def async_select_option(self, option: str) -> None: ...
