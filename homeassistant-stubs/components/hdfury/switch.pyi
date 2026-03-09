from .const import DOMAIN as DOMAIN
from .coordinator import HDFuryConfigEntry as HDFuryConfigEntry
from .entity import HDFuryEntity as HDFuryEntity
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from hdfury import HDFuryAPI as HDFuryAPI
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class HDFurySwitchEntityDescription(SwitchEntityDescription):
    set_value_fn: Callable[[HDFuryAPI, str], Awaitable[None]]

SWITCHES: tuple[HDFurySwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: HDFuryConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HDFurySwitch(HDFuryEntity, SwitchEntity):
    entity_description: HDFurySwitchEntityDescription
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
