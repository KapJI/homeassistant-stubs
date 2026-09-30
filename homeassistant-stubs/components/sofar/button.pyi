from .coordinator import SofarConfigEntry as SofarConfigEntry
from .entity import SofarEntity as SofarEntity, SofarEntityDescription as SofarEntityDescription
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from sofar_modbus.modern.device import SofarInverter as SofarInverter
from sofar_modbus.variants import InverterType as InverterType
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class SofarButtonEntityDescription(ButtonEntityDescription, SofarEntityDescription):
    applies_to: InverterType
    press_fn: Callable[[SofarInverter], Awaitable[None]]
    refresh_after: bool = ...

BUTTON_DESCRIPTIONS: tuple[SofarButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SofarConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SofarButton(SofarEntity, ButtonEntity):
    entity_description: SofarButtonEntityDescription
    @override
    async def async_press(self) -> None: ...
