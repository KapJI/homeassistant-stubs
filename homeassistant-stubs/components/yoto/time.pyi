from .coordinator import YotoConfigEntry as YotoConfigEntry, YotoDataUpdateCoordinator as YotoDataUpdateCoordinator
from .entity import YotoConfigEntity as YotoConfigEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import time
from homeassistant.components.time import TimeEntity as TimeEntity, TimeEntityDescription as TimeEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override
from yoto_api import PlayerConfig as PlayerConfig, YotoPlayer as YotoPlayer

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class YotoTimeEntityDescription(TimeEntityDescription):
    value_fn: Callable[[PlayerConfig], time | None]
    config_field: str

TIME_ENTITIES: tuple[YotoTimeEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: YotoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class YotoTime(YotoConfigEntity, TimeEntity):
    entity_description: YotoTimeEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: YotoDataUpdateCoordinator, player: YotoPlayer, description: YotoTimeEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> time | None: ...
    @override
    async def async_set_value(self, value: time) -> None: ...
