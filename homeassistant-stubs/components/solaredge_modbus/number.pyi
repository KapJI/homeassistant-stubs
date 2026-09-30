from .coordinator import SolarEdgeModbusConfigEntry as SolarEdgeModbusConfigEntry
from .entity import ControlComponent as ControlComponent, SolarEdgeModbusControlEntity as SolarEdgeModbusControlEntity
from .helpers import solaredge_exception_handler as solaredge_exception_handler
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from solaredged import ExportControl as ExportControl, PowerControl as PowerControl, StorageControl as StorageControl
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class SolarEdgeModbusNumberEntityDescription[ComponentT](NumberEntityDescription):
    value_fn: Callable[[ComponentT], float | None]
    set_fn: Callable[[ComponentT, float], Awaitable[Any]]

STORAGE_NUMBERS: tuple[SolarEdgeModbusNumberEntityDescription[StorageControl], ...]
EXPORT_NUMBERS: tuple[SolarEdgeModbusNumberEntityDescription[ExportControl], ...]
POWER_NUMBERS: tuple[SolarEdgeModbusNumberEntityDescription[PowerControl], ...]

async def async_setup_entry(hass: HomeAssistant, entry: SolarEdgeModbusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SolarEdgeModbusNumberEntity[ComponentT: ControlComponent](SolarEdgeModbusControlEntity[ComponentT], NumberEntity):
    entity_description: SolarEdgeModbusNumberEntityDescription[ComponentT]
    @property
    @override
    def native_value(self) -> float | None: ...
    @solaredge_exception_handler
    @override
    async def async_set_native_value(self, value: float) -> None: ...
