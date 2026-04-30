from .coordinator import RitualsConfigEntry as RitualsConfigEntry
from .entity import DiffuserEntity as DiffuserEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyrituals import Diffuser as Diffuser
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RitualsNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[Diffuser], int]
    set_value_fn: Callable[[Diffuser, int], Awaitable[Any]]

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: RitualsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RitualsNumberEntity(DiffuserEntity, NumberEntity):
    entity_description: RitualsNumberEntityDescription
    @property
    def native_value(self) -> int: ...
    async def async_set_native_value(self, value: float) -> None: ...
