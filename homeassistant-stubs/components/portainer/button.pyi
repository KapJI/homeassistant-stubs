import abc
from . import PortainerConfigEntry as PortainerConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import PortainerContainerData as PortainerContainerData, PortainerCoordinator as PortainerCoordinator, PortainerCoordinatorData as PortainerCoordinatorData
from .entity import PortainerContainerEntity as PortainerContainerEntity, PortainerEndpointEntity as PortainerEndpointEntity
from abc import abstractmethod
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyportainer import Portainer as Portainer
from pyportainer.models.docker import DockerContainer as DockerContainer
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PortainerEndpointButtonDescription(ButtonEntityDescription):
    press_action: Callable[[Portainer, int], Coroutine[Any, Any, DockerContainer | None]]

@dataclass(frozen=True, kw_only=True)
class PortainerContainerButtonDescription(ButtonEntityDescription):
    press_action: Callable[[Portainer, int, str], Coroutine[Any, Any, DockerContainer | None]]
    available_fn: Callable[[PortainerContainerData], bool]

ENDPOINT_BUTTONS: tuple[PortainerEndpointButtonDescription, ...]
CONTAINER_BUTTONS: tuple[PortainerContainerButtonDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PortainerConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PortainerBaseButton(ButtonEntity, metaclass=abc.ABCMeta):
    coordinator: PortainerCoordinator
    @abstractmethod
    async def _async_press_call(self) -> None: ...
    @override
    async def async_press(self) -> None: ...

class PortainerEndpointButton(PortainerEndpointEntity, PortainerBaseButton):
    entity_description: PortainerEndpointButtonDescription
    @override
    async def _async_press_call(self) -> None: ...

class PortainerContainerButton(PortainerContainerEntity, PortainerBaseButton):
    entity_description: PortainerContainerButtonDescription
    @property
    @override
    def available(self) -> bool: ...
    @override
    async def _async_press_call(self) -> None: ...
