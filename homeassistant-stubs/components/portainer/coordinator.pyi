from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyportainer import Portainer as Portainer
from pyportainer.models.docker import DockerContainer as DockerContainer
from pyportainer.models.portainer import Endpoint as Endpoint

type PortainerConfigEntry = ConfigEntry[PortainerCoordinator]
_LOGGER: Incomplete
DEFAULT_SCAN_INTERVAL: Incomplete

@dataclass
class PortainerCoordinatorData:
    id: int
    name: str | None
    endpoint: Endpoint
    containers: dict[str, DockerContainer]

class PortainerCoordinator(DataUpdateCoordinator[dict[int, PortainerCoordinatorData]]):
    config_entry: PortainerConfigEntry
    portainer: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: PortainerConfigEntry, portainer: Portainer) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> dict[int, PortainerCoordinatorData]: ...
