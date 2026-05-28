from . import IndevoltConfigEntry as IndevoltConfigEntry
from .coordinator import IndevoltCoordinator as IndevoltCoordinator
from .entity import IndevoltEntity as IndevoltEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class IndevoltButtonEntityDescription(ButtonEntityDescription):
    generation: tuple[int, ...] = ...

BUTTONS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: IndevoltConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IndevoltButtonEntity(IndevoltEntity, ButtonEntity):
    entity_description: IndevoltButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: IndevoltCoordinator, description: IndevoltButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
