from .coordinator import ElgatoConfigEntry as ElgatoConfigEntry, ElgatoData as ElgatoData, ElgatoDataUpdateCoordinator as ElgatoDataUpdateCoordinator
from .entity import ElgatoEntity as ElgatoEntity
from .helpers import elgato_exception_handler as elgato_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from elgato import Elgato as Elgato
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ElgatoSwitchEntityDescription(SwitchEntityDescription):
    has_fn: Callable[[ElgatoData], bool] = ...
    is_on_fn: Callable[[ElgatoData], bool | None]
    set_fn: Callable[[Elgato, bool], Awaitable[Any]]

SWITCHES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ElgatoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ElgatoSwitchEntity(ElgatoEntity, SwitchEntity):
    entity_description: ElgatoSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ElgatoDataUpdateCoordinator, description: ElgatoSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    @elgato_exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @elgato_exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...
