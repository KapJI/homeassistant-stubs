from . import VistapoolConfigEntry as VistapoolConfigEntry
from .const import DOMAIN as DOMAIN, PATH_HASHIDRO as PATH_HASHIDRO, PATH_HASPH as PATH_HASPH, PATH_HASRX as PATH_HASRX
from .coordinator import VistapoolDataUpdateCoordinator as VistapoolDataUpdateCoordinator
from .entity import VistapoolEntity as VistapoolEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int
_TEMP_MIN: float
_TEMP_MAX: float

@dataclass(frozen=True, kw_only=True)
class VistapoolNumberEntityDescription(NumberEntityDescription):
    value_path: str
    scale: int = ...
    exists_path: str | tuple[str, ...] | None = ...
    max_value_fn: Callable[[VistapoolDataUpdateCoordinator], float] | None = ...

def _max_electrolysis(coordinator: VistapoolDataUpdateCoordinator) -> float: ...

NUMBER_DESCRIPTIONS: tuple[VistapoolNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: VistapoolConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VistapoolNumber(VistapoolEntity, NumberEntity):
    entity_description: VistapoolNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: VistapoolDataUpdateCoordinator, description: VistapoolNumberEntityDescription) -> None: ...
    @property
    @override
    def native_max_value(self) -> float: ...
    @property
    @override
    def native_value(self) -> float | None: ...
    @override
    async def async_set_native_value(self, value: float) -> None: ...
