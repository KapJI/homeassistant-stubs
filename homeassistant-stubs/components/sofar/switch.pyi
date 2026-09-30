from .coordinator import SofarConfigEntry as SofarConfigEntry
from .entity import SofarEntity as SofarEntity, SofarEntityDescription as SofarEntityDescription
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from sofar_modbus.modern.device import SofarInverter as SofarInverter
from sofar_modbus.modern.enums import RemoteSwitchOnOff
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class SofarSwitchEntityDescription(SwitchEntityDescription, SofarEntityDescription):
    value_fn: Callable[[SofarInverter], RemoteSwitchOnOff | None]
    write_fn: Callable[[SofarInverter, bool], Awaitable[None]]

SWITCH_DESCRIPTIONS: tuple[SofarSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SofarConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SofarSwitch(SofarEntity, SwitchEntity):
    entity_description: SofarSwitchEntityDescription
    @property
    @override
    def is_on(self) -> bool | None: ...
    async def _async_write(self, value: bool) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
