from . import PortainerConfigEntry as PortainerConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import PortainerContainerData as PortainerContainerData, PortainerCoordinator as PortainerCoordinator, PortainerStackData as PortainerStackData
from .entity import PortainerContainerEntity as PortainerContainerEntity, PortainerCoordinatorData as PortainerCoordinatorData, PortainerStackEntity as PortainerStackEntity
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyportainer import Portainer as Portainer
from typing import Any

@dataclass(frozen=True, kw_only=True)
class PortainerSwitchEntityDescription(SwitchEntityDescription):
    is_on_fn: Callable[[PortainerContainerData], bool | None]
    turn_on_fn: Callable[[Portainer], Callable[[int, str], Coroutine[Any, Any, None]]]
    turn_off_fn: Callable[[Portainer], Callable[[int, str], Coroutine[Any, Any, None]]]

@dataclass(frozen=True, kw_only=True)
class PortainerStackSwitchEntityDescription(SwitchEntityDescription):
    is_on_fn: Callable[[PortainerStackData], bool | None]
    turn_on_fn: Callable[[Portainer], Callable[..., Coroutine[Any, Any, Any]]]
    turn_off_fn: Callable[[Portainer], Callable[..., Coroutine[Any, Any, Any]]]

PARALLEL_UPDATES: int

async def _perform_action(coordinator: PortainerCoordinator, coroutine: Coroutine[Any, Any, Any]) -> None: ...

CONTAINER_SWITCHES: tuple[PortainerSwitchEntityDescription, ...]
STACK_SWITCHES: tuple[PortainerStackSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PortainerConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PortainerContainerSwitch(PortainerContainerEntity, SwitchEntity):
    entity_description: PortainerSwitchEntityDescription
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class PortainerStackSwitch(PortainerStackEntity, SwitchEntity):
    entity_description: PortainerStackSwitchEntityDescription
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
