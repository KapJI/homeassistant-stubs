from .const import DOMAIN as DOMAIN
from .coordinator import PortainerConfigEntry as PortainerConfigEntry, PortainerContainerData as PortainerContainerData, PortainerCoordinator as PortainerCoordinator, PortainerCoordinatorData as PortainerCoordinatorData
from .entity import PortainerContainerEntity as PortainerContainerEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.update import UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyportainer import Portainer as Portainer
from pyportainer.models.docker import DockerContainer as DockerContainer, LocalImageInformation as LocalImageInformation, PortainerImageUpdateStatus as PortainerImageUpdateStatus
from typing import Any, override

@dataclass(frozen=True, kw_only=True)
class PortainerContainerUpdateEntityDescription(UpdateEntityDescription):
    installed_version: Callable[[LocalImageInformation], str | None]
    latest_version: Callable[[PortainerImageUpdateStatus | None], str | None]
    update_func: Callable[[Portainer, int, str], Awaitable[DockerContainer]]

PARALLEL_UPDATES: int
DEFAULT_RECREATE_TIMEOUT: Incomplete

def _short_digest(digest: str) -> str: ...

CONTAINER_IMAGE: tuple[PortainerContainerUpdateEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: PortainerConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PortainerContainerImageUpdateEntity(PortainerContainerEntity, UpdateEntity):
    _attr_supported_features: Incomplete
    entity_description: PortainerContainerUpdateEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PortainerCoordinator, entity_description: PortainerContainerUpdateEntityDescription, device_info: PortainerContainerData, via_device: PortainerCoordinatorData) -> None: ...
    @override
    @property
    def title(self) -> str | None: ...
    @override
    @property
    def installed_version(self) -> str | None: ...
    @override
    @property
    def latest_version(self) -> str | None: ...
    @override
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
