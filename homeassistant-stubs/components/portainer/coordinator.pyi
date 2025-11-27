from .const import DOMAIN as DOMAIN, ENDPOINT_STATUS_DOWN as ENDPOINT_STATUS_DOWN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyportainer import Portainer as Portainer
from pyportainer.models.docker import DockerContainer as DockerContainer, DockerContainerStats as DockerContainerStats
from pyportainer.models.docker_inspect import DockerInfo as DockerInfo, DockerVersion as DockerVersion
from pyportainer.models.portainer import Endpoint as Endpoint

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

@dataclass(slots=True)
class PortainerContainerData:
    container: DockerContainer
    stats: DockerContainerStats
    stats_pre: DockerContainerStats | None

class PortainerCoordinator(DataUpdateCoordinator[dict[int, PortainerCoordinatorData]]):
    config_entry: PortainerConfigEntry
    portainer: Incomplete
    known_endpoints: set[int]
    known_containers: set[tuple[int, str]]
    new_endpoints_callbacks: list[Callable[[list[PortainerCoordinatorData]], None]]
    new_containers_callbacks: list[Callable[[list[tuple[PortainerCoordinatorData, PortainerContainerData]]], None]]
    def __init__(self, hass: HomeAssistant, config_entry: PortainerConfigEntry, portainer: Portainer) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> dict[int, PortainerCoordinatorData]: ...
    def _async_add_remove_endpoints(self, mapped_endpoints: dict[int, PortainerCoordinatorData]) -> None: ...
