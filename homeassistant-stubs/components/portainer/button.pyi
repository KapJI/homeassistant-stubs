import abc
from . import PortainerConfigEntry as PortainerConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import PortainerContainerData as PortainerContainerData, PortainerCoordinator as PortainerCoordinator, PortainerCoordinatorData as PortainerCoordinatorData
from .entity import PortainerContainerEntity as PortainerContainerEntity, PortainerEndpointEntity as PortainerEndpointEntity
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyportainer import Portainer as Portainer
from typing import Any

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class PortainerButtonDescription(ButtonEntityDescription):
    press_action: Callable[[Portainer, int, str], Coroutine[Any, Any, None]]

ENDPOINT_BUTTONS: tuple[PortainerButtonDescription, ...]
CONTAINER_BUTTONS: tuple[PortainerButtonDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PortainerConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PortainerBaseButton(ButtonEntity, metaclass=abc.ABCMeta):
    entity_description: PortainerButtonDescription
    coordinator: PortainerCoordinator
    @abstractmethod
    async def _async_press_call(self) -> None: ...
    async def async_press(self) -> None: ...

class PortainerEndpointButton(PortainerEndpointEntity, PortainerBaseButton):
    entity_description: PortainerButtonDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PortainerCoordinator, entity_description: PortainerButtonDescription, device_info: PortainerCoordinatorData) -> None: ...
    async def _async_press_call(self) -> None: ...

class PortainerContainerButton(PortainerContainerEntity, PortainerBaseButton):
    entity_description: PortainerButtonDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PortainerCoordinator, entity_description: PortainerButtonDescription, device_info: PortainerContainerData, via_device: PortainerCoordinatorData) -> None: ...
    async def _async_press_call(self) -> None: ...
