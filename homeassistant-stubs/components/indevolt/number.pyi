from . import IndevoltConfigEntry as IndevoltConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import IndevoltCoordinator as IndevoltCoordinator
from .entity import IndevoltEntity as IndevoltEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class IndevoltNumberEntityDescription(NumberEntityDescription):
    read_key: str
    write_key: str
    generation: tuple[int, ...] = ...

NUMBERS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: IndevoltConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IndevoltNumberEntity(IndevoltEntity, NumberEntity):
    entity_description: IndevoltNumberEntityDescription
    _attr_mode: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: IndevoltCoordinator, description: IndevoltNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> int | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
