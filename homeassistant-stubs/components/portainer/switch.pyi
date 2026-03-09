from . import PortainerConfigEntry as PortainerConfigEntry
from .const import DOMAIN as DOMAIN, STACK_STATUS_ACTIVE as STACK_STATUS_ACTIVE
from .coordinator import PortainerContainerData as PortainerContainerData, PortainerCoordinator as PortainerCoordinator, PortainerStackData as PortainerStackData
from .entity import PortainerContainerEntity as PortainerContainerEntity, PortainerCoordinatorData as PortainerCoordinatorData, PortainerStackEntity as PortainerStackEntity
from _typeshed import Incomplete
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
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PortainerCoordinator, entity_description: PortainerSwitchEntityDescription, device_info: PortainerContainerData, via_device: PortainerCoordinatorData) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class PortainerStackSwitch(PortainerStackEntity, SwitchEntity):
    entity_description: PortainerStackSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PortainerCoordinator, entity_description: PortainerStackSwitchEntityDescription, device_info: PortainerStackData, via_device: PortainerCoordinatorData) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
