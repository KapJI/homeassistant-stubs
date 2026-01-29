from . import AirobotConfigEntry as AirobotConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import AirobotDataUpdateCoordinator as AirobotDataUpdateCoordinator
from .entity import AirobotEntity as AirobotEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class AirobotSwitchEntityDescription(SwitchEntityDescription):
    is_on_fn: Callable[[AirobotDataUpdateCoordinator], bool]
    turn_on_fn: Callable[[AirobotDataUpdateCoordinator], Coroutine[Any, Any, None]]
    turn_off_fn: Callable[[AirobotDataUpdateCoordinator], Coroutine[Any, Any, None]]

SWITCH_TYPES: tuple[AirobotSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AirobotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AirobotSwitch(AirobotEntity, SwitchEntity):
    entity_description: AirobotSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirobotDataUpdateCoordinator, description: AirobotSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
