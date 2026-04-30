from .coordinator import FumisConfigEntry as FumisConfigEntry, FumisDataUpdateCoordinator as FumisDataUpdateCoordinator
from .entity import FumisEntity as FumisEntity
from .helpers import fumis_exception_handler as fumis_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from fumis import Fumis as Fumis
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class FumisButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[Fumis], Awaitable[Any]]

BUTTONS: tuple[FumisButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: FumisConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FumisButtonEntity(FumisEntity, ButtonEntity):
    entity_description: FumisButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FumisDataUpdateCoordinator, description: FumisButtonEntityDescription) -> None: ...
    @fumis_exception_handler
    async def async_press(self) -> None: ...
