from .const import DOMAIN as DOMAIN, MieleAppliance as MieleAppliance
from .coordinator import MieleConfigEntry as MieleConfigEntry
from .entity import MieleDevice as MieleDevice, MieleEntity as MieleEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from enum import IntEnum
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Final

PARALLEL_UPDATES: int
_LOGGER: Incomplete

class MieleModes(IntEnum):
    NORMAL = 0
    SABBATH = 1
    PARTY = 2
    HOLIDAY = 3

@dataclass(frozen=True, kw_only=True)
class MieleSelectDescription(SelectEntityDescription):
    value_fn: Callable[[MieleDevice], StateType]

@dataclass
class MieleSelectDefinition:
    types: tuple[MieleAppliance, ...]
    description: MieleSelectDescription

SELECT_TYPES: Final[tuple[MieleSelectDefinition, ...]]

async def async_setup_entry(hass: HomeAssistant, config_entry: MieleConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MieleSelectMode(MieleEntity, SelectEntity):
    entity_description: MieleSelectDescription
    @property
    def options(self) -> list[str]: ...
    @property
    def current_option(self) -> str: ...
    async def async_select_option(self, option: str) -> None: ...
