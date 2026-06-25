from .coordinator import YotoConfigEntry as YotoConfigEntry, YotoDataUpdateCoordinator as YotoDataUpdateCoordinator
from .entity import YotoConfigEntity as YotoConfigEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override
from yoto_api import Capabilities as Capabilities, PlayerConfig as PlayerConfig, YotoPlayer as YotoPlayer

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class YotoSelectEntityDescription(SelectEntityDescription):
    value_fn: Callable[[PlayerConfig], str | None]
    config_field: str
    options: list[str]
    supported_fn: Callable[[Capabilities], bool]

SELECTS: tuple[YotoSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: YotoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class YotoSelect(YotoConfigEntity, SelectEntity):
    entity_description: YotoSelectEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: YotoDataUpdateCoordinator, player: YotoPlayer, description: YotoSelectEntityDescription) -> None: ...
    @property
    @override
    def current_option(self) -> str | None: ...
    @override
    async def async_select_option(self, option: str) -> None: ...
