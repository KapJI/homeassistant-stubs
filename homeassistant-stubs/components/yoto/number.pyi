from .coordinator import YotoConfigEntry as YotoConfigEntry, YotoDataUpdateCoordinator as YotoDataUpdateCoordinator
from .entity import YotoConfigEntity as YotoConfigEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override
from yoto_api import PlayerConfig as PlayerConfig, YotoPlayer as YotoPlayer

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class YotoNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[PlayerConfig], int | None]
    config_field: str
    available_fn: Callable[[PlayerConfig], bool] = ...

NUMBERS: tuple[YotoNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: YotoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class YotoNumber(YotoConfigEntity, NumberEntity):
    entity_description: YotoNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: YotoDataUpdateCoordinator, player: YotoPlayer, description: YotoNumberEntityDescription) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def native_value(self) -> float | None: ...
    @override
    async def async_set_native_value(self, value: float) -> None: ...
