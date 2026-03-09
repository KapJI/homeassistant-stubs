from .coordinator import NRGkickConfigEntry as NRGkickConfigEntry, NRGkickData as NRGkickData, NRGkickDataUpdateCoordinator as NRGkickDataUpdateCoordinator
from .entity import NRGkickEntity as NRGkickEntity
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.const import UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfEnergy as UnitOfEnergy
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int
MIN_CHARGING_CURRENT: int

def _get_current_set_max(data: NRGkickData) -> float: ...
def _get_phase_count_max(data: NRGkickData) -> float: ...

@dataclass(frozen=True, kw_only=True)
class NRGkickNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[NRGkickData], float | None]
    set_value_fn: Callable[[NRGkickDataUpdateCoordinator, float], Awaitable[Any]]
    max_value_fn: Callable[[NRGkickData], float] | None = ...

NUMBERS: tuple[NRGkickNumberEntityDescription, ...]

async def async_setup_entry(_hass: HomeAssistant, entry: NRGkickConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NRGkickNumber(NRGkickEntity, NumberEntity):
    entity_description: NRGkickNumberEntityDescription
    def __init__(self, coordinator: NRGkickDataUpdateCoordinator, description: NRGkickNumberEntityDescription) -> None: ...
    @property
    def native_max_value(self) -> float: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
