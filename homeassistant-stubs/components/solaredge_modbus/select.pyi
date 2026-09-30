from .coordinator import SolarEdgeModbusConfigEntry as SolarEdgeModbusConfigEntry
from .entity import ControlComponent as ControlComponent, SolarEdgeModbusControlEntity as SolarEdgeModbusControlEntity
from .helpers import solaredge_exception_handler as solaredge_exception_handler
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from solaredged import ExportControl as ExportControl, SolarEdge as SolarEdge, StorageControl as StorageControl
from typing import Any, override

PARALLEL_UPDATES: int
EXPORT_MODE_DISABLED: str

@dataclass(frozen=True, kw_only=True)
class SolarEdgeModbusSelectEntityDescription[ComponentT](SelectEntityDescription):
    current_fn: Callable[[ComponentT], str | None]
    options_fn: Callable[[SolarEdge], list[str]] | None = ...
    select_fn: Callable[[ComponentT, str], Awaitable[Any]]

STORAGE_SELECTS: tuple[SolarEdgeModbusSelectEntityDescription[StorageControl], ...]
EXPORT_SELECTS: tuple[SolarEdgeModbusSelectEntityDescription[ExportControl], ...]

async def async_setup_entry(hass: HomeAssistant, entry: SolarEdgeModbusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SolarEdgeModbusSelectEntity[ComponentT: ControlComponent](SolarEdgeModbusControlEntity[ComponentT], SelectEntity):
    entity_description: SolarEdgeModbusSelectEntityDescription[ComponentT]
    @property
    @override
    def options(self) -> list[str]: ...
    @property
    @override
    def current_option(self) -> str | None: ...
    @solaredge_exception_handler
    @override
    async def async_select_option(self, option: str) -> None: ...
