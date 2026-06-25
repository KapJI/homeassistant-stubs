from . import IndevoltConfigEntry as IndevoltConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import IndevoltCoordinator as IndevoltCoordinator
from .entity import IndevoltEntity as IndevoltEntity
from _typeshed import Incomplete
from dataclasses import dataclass, field
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from indevolt_api import IndevoltEnergyMode
from typing import Final, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class IndevoltSelectEntityDescription(SelectEntityDescription):
    read_key: str
    write_key: str
    value_to_option: dict[IndevoltEnergyMode, str]
    unavailable_values: list[IndevoltEnergyMode] = field(default_factory=list)
    generation: tuple[int, ...] = ...

SELECTS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: IndevoltConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IndevoltSelectEntity(IndevoltEntity, SelectEntity):
    entity_description: IndevoltSelectEntityDescription
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    _option_to_value: Incomplete
    def __init__(self, coordinator: IndevoltCoordinator, description: IndevoltSelectEntityDescription) -> None: ...
    @property
    @override
    def current_option(self) -> str | None: ...
    @property
    @override
    def available(self) -> bool: ...
    @override
    async def async_select_option(self, option: str) -> None: ...
