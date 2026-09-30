from .coordinator import SolarEdgeModbusConfigEntry as SolarEdgeModbusConfigEntry
from .entity import SolarEdgeModbusControlEntity as SolarEdgeModbusControlEntity
from .helpers import solaredge_exception_handler as solaredge_exception_handler
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from solaredged import ExportControl
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class SolarEdgeModbusSwitchEntityDescription(SwitchEntityDescription):
    is_on_fn: Callable[[ExportControl], bool | None]
    set_fn: Callable[[ExportControl, bool], Awaitable[Any]]

EXPORT_SWITCHES: tuple[SolarEdgeModbusSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SolarEdgeModbusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SolarEdgeModbusSwitchEntity(SolarEdgeModbusControlEntity[ExportControl], SwitchEntity):
    entity_description: SolarEdgeModbusSwitchEntityDescription
    @property
    @override
    def is_on(self) -> bool | None: ...
    @solaredge_exception_handler
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @solaredge_exception_handler
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
