from .const import DOMAIN as DOMAIN
from .coordinator import FlexitConfigEntry as FlexitConfigEntry, FlexitCoordinator as FlexitCoordinator
from .entity import FlexitEntity as FlexitEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from flexit_bacnet import FlexitBACnet as FlexitBACnet
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_MAX_FAN_SETPOINT: int
_MIN_FAN_SETPOINT: int
_MAX_RUNTIME_DURATION: int
_MIN_RUNTIME_DURATION: int

@dataclass(kw_only=True, frozen=True)
class FlexitNumberEntityDescription(NumberEntityDescription):
    native_value_fn: Callable[[FlexitBACnet], float]
    native_max_value_fn: Callable[[FlexitBACnet], int]
    native_min_value_fn: Callable[[FlexitBACnet], int]
    set_native_value_fn: Callable[[FlexitBACnet], Callable[[int], Awaitable[None]]]

NUMBERS: tuple[FlexitNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: FlexitConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

PARALLEL_UPDATES: int

class FlexitNumber(FlexitEntity, NumberEntity):
    entity_description: FlexitNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FlexitCoordinator, entity_description: FlexitNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float: ...
    @property
    def native_max_value(self) -> float: ...
    @property
    def native_min_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...
