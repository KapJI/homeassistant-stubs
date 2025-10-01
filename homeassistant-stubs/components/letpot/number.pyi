from .coordinator import LetPotConfigEntry as LetPotConfigEntry, LetPotDeviceCoordinator as LetPotDeviceCoordinator
from .entity import LetPotEntity as LetPotEntity, LetPotEntityDescription as LetPotEntityDescription, exception_handler as exception_handler
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.const import EntityCategory as EntityCategory, PRECISION_WHOLE as PRECISION_WHOLE, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from letpot.deviceclient import LetPotDeviceClient as LetPotDeviceClient
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LetPotNumberEntityDescription(LetPotEntityDescription, NumberEntityDescription):
    max_value_fn: Callable[[LetPotDeviceCoordinator], float]
    value_fn: Callable[[LetPotDeviceCoordinator], float | None]
    set_value_fn: Callable[[LetPotDeviceClient, str, float], Coroutine[Any, Any, None]]

NUMBERS: tuple[LetPotNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LetPotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LetPotNumberEntity(LetPotEntity, NumberEntity):
    entity_description: LetPotNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LetPotDeviceCoordinator, description: LetPotNumberEntityDescription) -> None: ...
    @property
    def native_max_value(self) -> float: ...
    @property
    def native_value(self) -> float | None: ...
    @exception_handler
    async def async_set_native_value(self, value: float) -> None: ...
