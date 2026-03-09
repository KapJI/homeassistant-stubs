from .coordinator import ZinvoltConfigEntry as ZinvoltConfigEntry, ZinvoltDeviceCoordinator as ZinvoltDeviceCoordinator
from .entity import ZinvoltEntity as ZinvoltEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfPower as UnitOfPower, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from zinvolt import ZinvoltClient as ZinvoltClient
from zinvolt.models import BatteryState as BatteryState

@dataclass(kw_only=True, frozen=True)
class ZinvoltBatteryStateDescription(NumberEntityDescription):
    max_fn: Callable[[BatteryState], int] | None = ...
    value_fn: Callable[[BatteryState], int]
    set_value_fn: Callable[[ZinvoltClient, str, int], Awaitable[None]]

NUMBERS: tuple[ZinvoltBatteryStateDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ZinvoltConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ZinvoltBatteryStateNumber(ZinvoltEntity, NumberEntity):
    entity_description: ZinvoltBatteryStateDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ZinvoltDeviceCoordinator, description: ZinvoltBatteryStateDescription) -> None: ...
    @property
    def native_max_value(self) -> float: ...
    @property
    def native_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...
