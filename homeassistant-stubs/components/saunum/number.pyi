from . import LeilSaunaConfigEntry as LeilSaunaConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import LeilSaunaCoordinator as LeilSaunaCoordinator
from .entity import LeilSaunaEntity as LeilSaunaEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pysaunum import SaunumClient as SaunumClient, SaunumData as SaunumData

PARALLEL_UPDATES: int
DEFAULT_DURATION_MIN: int
DEFAULT_FAN_DURATION_MIN: int

@dataclass(frozen=True, kw_only=True)
class LeilSaunaNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[SaunumData], int | float | None]
    set_value_fn: Callable[[SaunumClient, float], Awaitable[None]]

NUMBERS: tuple[LeilSaunaNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LeilSaunaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LeilSaunaNumber(LeilSaunaEntity, NumberEntity):
    entity_description: LeilSaunaNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LeilSaunaCoordinator, description: LeilSaunaNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
