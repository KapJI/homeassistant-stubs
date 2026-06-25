from .const import DOMAIN as DOMAIN, SCAN_INTERVAL as SCAN_INTERVAL
from .validation import UnsupportedBoardError as UnsupportedBoardError, async_get_supported_board_info as async_get_supported_board_info
from _typeshed import Incomplete
from dataclasses import dataclass
from duco_connectivity import DucoClient as DucoClient
from duco_connectivity.models import BoardInfo as BoardInfo, Node as Node, NodeListActionItemList
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

_LOGGER: Incomplete
type DucoConfigEntry = ConfigEntry[DucoCoordinator]

@dataclass
class DucoData:
    nodes: dict[int, Node]
    node_actions: NodeListActionItemList
    rssi_wifi: int | None
    time_filter_remain: int | None

class DucoCoordinator(DataUpdateCoordinator[DucoData]):
    config_entry: DucoConfigEntry
    board_info: BoardInfo
    _supports_time_filter_remain: bool
    client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: DucoConfigEntry, client: DucoClient) -> None: ...
    @override
    async def _async_setup(self) -> None: ...
    @override
    async def _async_update_data(self) -> DucoData: ...
