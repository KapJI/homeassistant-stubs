from .coordinator import SofarConfigEntry as SofarConfigEntry
from .entity import SofarEntity as SofarEntity, SofarEntityDescription as SofarEntityDescription
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from enum import IntEnum
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from sofar_modbus.modern.device import SofarInverter as SofarInverter
from typing import override

PARALLEL_UPDATES: int

def _enum_options(enum_type: type[IntEnum]) -> list[str]: ...

@dataclass(frozen=True, kw_only=True)
class SofarSelectEntityDescription(SelectEntityDescription, SofarEntityDescription):
    options_enum: type[IntEnum]
    value_fn: Callable[[SofarInverter], IntEnum | None]
    write_fn: Callable[[SofarInverter, int], Awaitable[None]]

SELECT_DESCRIPTIONS: tuple[SofarSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SofarConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SofarSelect(SofarEntity, SelectEntity):
    entity_description: SofarSelectEntityDescription
    @property
    @override
    def current_option(self) -> str | None: ...
    @override
    async def async_select_option(self, option: str) -> None: ...
