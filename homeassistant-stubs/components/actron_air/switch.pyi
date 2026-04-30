from .coordinator import ActronAirConfigEntry as ActronAirConfigEntry, ActronAirSystemCoordinator as ActronAirSystemCoordinator
from .entity import ActronAirAcEntity as ActronAirAcEntity, actron_air_command as actron_air_command
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ActronAirSwitchEntityDescription(SwitchEntityDescription):
    is_on_fn: Callable[[ActronAirSystemCoordinator], bool]
    set_fn: Callable[[ActronAirSystemCoordinator, bool], Awaitable[None]]
    is_supported_fn: Callable[[ActronAirSystemCoordinator], bool] = ...

SWITCHES: tuple[ActronAirSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ActronAirConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ActronAirSwitch(ActronAirAcEntity, SwitchEntity):
    _attr_entity_category: Incomplete
    entity_description: ActronAirSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ActronAirSystemCoordinator, description: ActronAirSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @actron_air_command
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @actron_air_command
    async def async_turn_off(self, **kwargs: Any) -> None: ...
