from .const import DOMAIN as DOMAIN, MieleActions as MieleActions, MieleAppliance as MieleAppliance, POWER_OFF as POWER_OFF, POWER_ON as POWER_ON, PROCESS_ACTION as PROCESS_ACTION, StateStatus as StateStatus
from .coordinator import MieleConfigEntry as MieleConfigEntry
from .entity import MieleEntity as MieleEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pymiele import MieleDevice as MieleDevice
from typing import Any, Final

PARALLEL_UPDATES: int
_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class MieleSwitchDescription(SwitchEntityDescription):
    value_fn: Callable[[MieleDevice], StateType]
    on_value: int = ...
    off_value: int = ...
    on_cmd_data: dict[str, str | int | bool]
    off_cmd_data: dict[str, str | int | bool]

@dataclass
class MieleSwitchDefinition:
    types: tuple[MieleAppliance, ...]
    description: MieleSwitchDescription

SWITCH_TYPES: Final[tuple[MieleSwitchDefinition, ...]]

async def async_setup_entry(hass: HomeAssistant, config_entry: MieleConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MieleSwitch(MieleEntity, SwitchEntity):
    entity_description: MieleSwitchDescription
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_switch(self, mode: dict[str, str | int | bool]) -> None: ...

class MielePowerSwitch(MieleSwitch):
    entity_description: MieleSwitchDescription
    @property
    def is_on(self) -> bool | None: ...
    @property
    def available(self) -> bool: ...
    async def async_turn_switch(self, mode: dict[str, str | int | bool]) -> None: ...

class MieleSuperSwitch(MieleSwitch):
    entity_description: MieleSwitchDescription
    @property
    def is_on(self) -> bool | None: ...
