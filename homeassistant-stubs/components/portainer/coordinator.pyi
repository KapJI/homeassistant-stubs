import abc
from .const import CONTAINER_STATE_ACTIONS as CONTAINER_STATE_ACTIONS, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .util import sanitize_container_name as sanitize_container_name
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime, timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyportainer import Portainer as Portainer, PortainerEventListener, PortainerEventListenerResult as PortainerEventListenerResult
from pyportainer.models.docker import DockerContainer as DockerContainer, DockerContainerStats as DockerContainerStats, DockerSystemDF, DockerVolume as DockerVolume, LocalImageInformation as LocalImageInformation, PortainerImageUpdateStatus as PortainerImageUpdateStatus
from pyportainer.models.docker_inspect import DockerInfo as DockerInfo, DockerInspect as DockerInspect, DockerVersion as DockerVersion
from pyportainer.models.portainer import Endpoint as Endpoint
from pyportainer.models.stacks import Stack as Stack
from pyportainer.watcher import PortainerImageWatcher as PortainerImageWatcher
from typing import override

type PortainerConfigEntry = ConfigEntry[PortainerCoordinator]
_LOGGER: Incomplete
DEFAULT_SCAN_INTERVAL: Incomplete
DEFAULT_DF_SCAN_INTERVAL: Incomplete

@dataclass
class PortainerCoordinatorData:
    id: int
    name: str | None
    endpoint: Endpoint
    containers: dict[str, PortainerContainerData]
    docker_version: DockerVersion
    docker_info: DockerInfo
    stacks: dict[str, PortainerStackData]
    volumes: dict[str, PortainerVolumeData]

@dataclass(slots=True, frozen=True)
class ContainerDockerEvent:
    action: str
    occurred_at: datetime

@dataclass(slots=True)
class PortainerContainerData:
    container: DockerContainer
    container_inspect: DockerInspect
    local_image: LocalImageInformation
    stack: Stack | None
    stats: DockerContainerStats | None
    stats_pre: DockerContainerStats | None
    image_status: PortainerImageUpdateStatus | None = ...
    last_docker_event: ContainerDockerEvent | None = ...

@dataclass(slots=True)
class PortainerStackData:
    stack: Stack
    container_count: int = ...

@dataclass(slots=True)
class PortainerVolumeData:
    volume: DockerVolume

class PortainerBaseCoordinator[_DataT](DataUpdateCoordinator[_DataT], metaclass=abc.ABCMeta):
    config_entry: PortainerConfigEntry
    _update_interval: timedelta
    portainer: Incomplete
    known_endpoints: set[int]
    known_containers: set[tuple[int, str]]
    known_stacks: set[tuple[int, str, int]]
    known_volumes: set[tuple[int, str]]
    new_endpoints_callbacks: list[Callable[[list[PortainerCoordinatorData]], None]]
    new_containers_callbacks: list[Callable[[list[tuple[PortainerCoordinatorData, PortainerContainerData]]], None]]
    new_stacks_callbacks: list[Callable[[list[tuple[PortainerCoordinatorData, PortainerStackData]]], None]]
    new_volumes_callbacks: list[Callable[[list[tuple[PortainerCoordinatorData, PortainerVolumeData]]], None]]
    def __init__(self, hass: HomeAssistant, config_entry: PortainerConfigEntry, portainer: Portainer) -> None: ...
    @override
    async def _async_setup(self) -> None: ...
    @abstractmethod
    async def update_data(self) -> _DataT: ...
    @override
    async def _async_update_data(self) -> _DataT: ...

class PortainerCoordinator(PortainerBaseCoordinator[dict[int, PortainerCoordinatorData]]):
    config_entry: PortainerConfigEntry
    docker_disk_space: PortainerDockerDiskSpaceCoordinator | None
    watcher: PortainerImageWatcher | None
    _update_interval = DEFAULT_SCAN_INTERVAL
    _image_cache: dict[tuple[int, str], tuple[float, LocalImageInformation]]
    _event_listeners: dict[int, PortainerEventListener]
    _event_listeners_enabled: bool
    _container_ids_by_endpoint: dict[int, dict[str, str]]
    def __init__(self, hass: HomeAssistant, config_entry: PortainerConfigEntry, portainer: Portainer) -> None: ...
    @override
    async def update_data(self) -> dict[int, PortainerCoordinatorData]: ...
    def async_register_endpoint_and_stack_devices(self, mapped_endpoints: dict[int, PortainerCoordinatorData], endpoint_ids: set[int], stack_keys: set[tuple[int, str, int]]) -> None: ...
    def _async_add_remove_endpoints(self, mapped_endpoints: dict[int, PortainerCoordinatorData]) -> None: ...
    async def _get_local_image(self, endpoint_id: int, image: str) -> LocalImageInformation: ...
    def _async_sync_event_listeners(self, mapped_endpoints: dict[int, PortainerCoordinatorData]) -> None: ...
    @callback
    def async_start_event_listeners(self) -> None: ...
    @callback
    def async_stop_event_listeners(self) -> None: ...
    data: Incomplete
    async def _async_handle_docker_event(self, result: PortainerEventListenerResult) -> None: ...

class PortainerDockerDiskSpaceCoordinator(PortainerBaseCoordinator[dict[int, DockerSystemDF]]):
    config_entry: PortainerConfigEntry
    _update_interval = DEFAULT_DF_SCAN_INTERVAL
    @override
    async def update_data(self) -> dict[int, DockerSystemDF]: ...
