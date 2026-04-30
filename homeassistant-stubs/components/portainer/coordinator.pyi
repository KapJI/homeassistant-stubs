from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyportainer import Portainer as Portainer
from pyportainer.models.docker import DockerContainer as DockerContainer, DockerContainerStats as DockerContainerStats, DockerSystemDF as DockerSystemDF, DockerVolume as DockerVolume
from pyportainer.models.docker_inspect import DockerInfo as DockerInfo, DockerVersion as DockerVersion
from pyportainer.models.portainer import Endpoint as Endpoint
from pyportainer.models.stacks import Stack as Stack

type PortainerConfigEntry = ConfigEntry[PortainerCoordinator]
_LOGGER: Incomplete
DEFAULT_SCAN_INTERVAL: Incomplete

@dataclass
class PortainerCoordinatorData:
    id: int
    name: str | None
    endpoint: Endpoint
    containers: dict[str, PortainerContainerData]
    docker_version: DockerVersion
    docker_info: DockerInfo
    docker_system_df: DockerSystemDF
    stacks: dict[str, PortainerStackData]
    volumes: dict[str, PortainerVolumeData]

@dataclass(slots=True)
class PortainerContainerData:
    container: DockerContainer
    stats: DockerContainerStats | None
    stats_pre: DockerContainerStats | None
    stack: Stack | None

@dataclass(slots=True)
class PortainerStackData:
    stack: Stack
    container_count: int = ...

@dataclass(slots=True)
class PortainerVolumeData:
    volume: DockerVolume

class PortainerCoordinator(DataUpdateCoordinator[dict[int, PortainerCoordinatorData]]):
    config_entry: PortainerConfigEntry
    portainer: Incomplete
    known_endpoints: set[int]
    known_containers: set[tuple[int, str]]
    known_stacks: set[tuple[int, str]]
    known_volumes: set[tuple[int, str]]
    new_endpoints_callbacks: list[Callable[[list[PortainerCoordinatorData]], None]]
    new_containers_callbacks: list[Callable[[list[tuple[PortainerCoordinatorData, PortainerContainerData]]], None]]
    new_stacks_callbacks: list[Callable[[list[tuple[PortainerCoordinatorData, PortainerStackData]]], None]]
    new_volumes_callbacks: list[Callable[[list[tuple[PortainerCoordinatorData, PortainerVolumeData]]], None]]
    def __init__(self, hass: HomeAssistant, config_entry: PortainerConfigEntry, portainer: Portainer) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> dict[int, PortainerCoordinatorData]: ...
    def _async_add_remove_endpoints(self, mapped_endpoints: dict[int, PortainerCoordinatorData]) -> None: ...
    def _get_container_name(self, container_name: str) -> str: ...
