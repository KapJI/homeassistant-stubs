from . import AirobotConfigEntry as AirobotConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import AirobotDataUpdateCoordinator as AirobotDataUpdateCoordinator
from .entity import AirobotEntity as AirobotEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class AirobotNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[AirobotDataUpdateCoordinator], float]
    set_value_fn: Callable[[AirobotDataUpdateCoordinator, float], Awaitable[None]]

NUMBERS: tuple[AirobotNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AirobotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AirobotNumber(AirobotEntity, NumberEntity):
    entity_description: AirobotNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirobotDataUpdateCoordinator, description: AirobotNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...
