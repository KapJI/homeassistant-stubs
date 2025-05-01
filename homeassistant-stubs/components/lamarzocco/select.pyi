from .const import DOMAIN as DOMAIN
from .coordinator import LaMarzoccoConfigEntry as LaMarzoccoConfigEntry
from .entity import LaMarzoccoEntity as LaMarzoccoEntity, LaMarzoccoEntityDescription as LaMarzoccoEntityDescription
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pylamarzocco.devices import LaMarzoccoMachine as LaMarzoccoMachine
from typing import Any

PARALLEL_UPDATES: int
STEAM_LEVEL_HA_TO_LM: Incomplete
STEAM_LEVEL_LM_TO_HA: Incomplete
PREBREW_MODE_HA_TO_LM: Incomplete
PREBREW_MODE_LM_TO_HA: Incomplete
STANDBY_MODE_HA_TO_LM: Incomplete
STANDBY_MODE_LM_TO_HA: Incomplete

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoSelectEntityDescription(LaMarzoccoEntityDescription, SelectEntityDescription):
    current_option_fn: Callable[[LaMarzoccoMachine], str | None]
    select_option_fn: Callable[[LaMarzoccoMachine, str], Coroutine[Any, Any, bool]]

ENTITIES: tuple[LaMarzoccoSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LaMarzoccoSelectEntity(LaMarzoccoEntity, SelectEntity):
    entity_description: LaMarzoccoSelectEntityDescription
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
