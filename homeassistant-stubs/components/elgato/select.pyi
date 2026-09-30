from .coordinator import ElgatoConfigEntry as ElgatoConfigEntry, ElgatoData as ElgatoData, ElgatoDataUpdateCoordinator as ElgatoDataUpdateCoordinator
from .entity import ElgatoEntity as ElgatoEntity
from .helpers import elgato_device_action as elgato_device_action
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from elgato import Elgato as Elgato
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int
POWER_ON_BEHAVIORS: Incomplete
POWER_ON_BEHAVIOR_OPTIONS: Incomplete

@dataclass(frozen=True, kw_only=True)
class ElgatoSelectEntityDescription(SelectEntityDescription):
    has_fn: Callable[[ElgatoData], bool] = ...
    current_fn: Callable[[ElgatoData], str | None]
    select_fn: Callable[[Elgato, str], Awaitable[Any]]

SELECTS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ElgatoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ElgatoSelectEntity(ElgatoEntity, SelectEntity):
    entity_description: ElgatoSelectEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ElgatoDataUpdateCoordinator, description: ElgatoSelectEntityDescription) -> None: ...
    @property
    @override
    def current_option(self) -> str | None: ...
    @elgato_device_action
    @override
    async def async_select_option(self, option: str) -> None: ...
