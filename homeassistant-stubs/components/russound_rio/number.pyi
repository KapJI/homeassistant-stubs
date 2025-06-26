from . import RussoundConfigEntry as RussoundConfigEntry
from .entity import RussoundBaseEntity as RussoundBaseEntity, command as command
from _typeshed import Incomplete
from aiorussound.rio import Controller as Controller, ZoneControlSurface as ZoneControlSurface
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RussoundZoneNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[ZoneControlSurface], float]
    set_value_fn: Callable[[ZoneControlSurface, float], Awaitable[None]]

CONTROL_ENTITIES: tuple[RussoundZoneNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: RussoundConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RussoundNumberEntity(RussoundBaseEntity, NumberEntity):
    entity_description: RussoundZoneNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, controller: Controller, zone_id: int, description: RussoundZoneNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float: ...
    @command
    async def async_set_native_value(self, value: float) -> None: ...
