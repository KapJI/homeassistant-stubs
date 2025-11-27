from . import PortainerConfigEntry as PortainerConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import PortainerContainerData as PortainerContainerData, PortainerCoordinator as PortainerCoordinator
from .entity import PortainerContainerEntity as PortainerContainerEntity, PortainerCoordinatorData as PortainerCoordinatorData
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
    turn_on_fn: Callable[[str, Portainer, int, str], Coroutine[Any, Any, None]]
    turn_off_fn: Callable[[str, Portainer, int, str], Coroutine[Any, Any, None]]

async def perform_action(action: str, portainer: Portainer, endpoint_id: int, container_id: str) -> None: ...

SWITCHES: tuple[PortainerSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PortainerConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PortainerContainerSwitch(PortainerContainerEntity, SwitchEntity):
    entity_description: PortainerSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PortainerCoordinator, entity_description: PortainerSwitchEntityDescription, device_info: PortainerContainerData, via_device: PortainerCoordinatorData) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
