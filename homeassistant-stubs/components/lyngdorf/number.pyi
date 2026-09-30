from .entity import LyngdorfEntity as LyngdorfEntity
from .models import LyngdorfConfigEntry as LyngdorfConfigEntry
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, UnitOfSoundPressure as UnitOfSoundPressure, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from lyngdorf import LyngdorfReceiver as LyngdorfReceiver, NumericControl as NumericControl, NumericRange as NumericRange
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LyngdorfNumberEntityDescription(NumberEntityDescription):
    control_fn: Callable[[LyngdorfReceiver], NumericControl | None]
    set_value_fn: Callable[[NumericControl, float], Awaitable[None]]

NUMBER_ENTITIES: tuple[LyngdorfNumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: LyngdorfConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LyngdorfNumber(LyngdorfEntity, NumberEntity):
    entity_description: LyngdorfNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, receiver: LyngdorfReceiver, config_entry: LyngdorfConfigEntry, device_info: DeviceInfo, description: LyngdorfNumberEntityDescription) -> None: ...
    @property
    def _range(self) -> NumericRange: ...
    @override
    @property
    def native_min_value(self) -> float: ...
    @override
    @property
    def native_max_value(self) -> float: ...
    @override
    @property
    def native_step(self) -> float: ...
    @override
    @property
    def native_value(self) -> float | None: ...
    @override
    async def async_set_native_value(self, value: float) -> None: ...
