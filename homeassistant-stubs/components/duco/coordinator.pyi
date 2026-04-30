from .const import DOMAIN as DOMAIN, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from dataclasses import dataclass
from duco import DucoClient as DucoClient
from duco.models import BoardInfo as BoardInfo, Node as Node
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
type DucoConfigEntry = ConfigEntry[DucoCoordinator]

@dataclass
class DucoData:
    nodes: dict[int, Node]
    rssi_wifi: int | None

class DucoCoordinator(DataUpdateCoordinator[DucoData]):
    config_entry: DucoConfigEntry
    board_info: BoardInfo
    client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: DucoConfigEntry, client: DucoClient) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> DucoData: ...
