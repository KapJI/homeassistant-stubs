import asyncio
from .const import DOMAIN as DOMAIN, SCAN_INTERVAL as SCAN_INTERVAL
from .validation import UnsupportedBoardError as UnsupportedBoardError, async_get_supported_board_info as async_get_supported_board_info
from _typeshed import Incomplete
from dataclasses import dataclass
from duco_connectivity import DucoClient as DucoClient, VentilationState as VentilationState
from duco_connectivity.exceptions import DucoError
from duco_connectivity.models import BoardInfo as BoardInfo, BypassSupplyTemperatureTarget as BypassSupplyTemperatureTarget, DiagStatus as DiagStatus, Node as Node, NodeListActionItemList, VentilationTemperatureInfo as VentilationTemperatureInfo
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

_LOGGER: Incomplete
type DucoConfigEntry = ConfigEntry[DucoCoordinator]

@dataclass(slots=True, kw_only=True)
class DucoData:
    nodes: dict[int, Node]
    node_actions: NodeListActionItemList
    diagnostics_available: bool
    diagnostic_subsystems: dict[str, DiagStatus | None]
    rssi_wifi: int | None
    time_filter_remain: int | None
    ventilation_temperatures: VentilationTemperatureInfo | None
    bypass_supply_temperature_targets: dict[int, BypassSupplyTemperatureTarget]

class DucoCoordinator(DataUpdateCoordinator[DucoData]):
    config_entry: DucoConfigEntry
    board_info: BoardInfo
    _configured_node_names: dict[int, str]
    _full_update_failed: bool
    _node_update_errors: dict[int, DucoError]
    _request_lock: asyncio.Lock
    client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: DucoConfigEntry, client: DucoClient) -> None: ...
    async def async_set_ventilation_state(self, node_id: int, state: str | VentilationState) -> None: ...
    async def async_set_node_identify(self, node_id: int, identify: bool) -> None: ...
    data: Incomplete
    last_update_success: bool
    async def _async_refresh_node(self, node_id: int) -> None: ...
    async def _async_load_node_names(self) -> None: ...
    @override
    async def _async_setup(self) -> None: ...
    @override
    async def _async_update_data(self) -> DucoData: ...
    async def _async_fetch_data(self) -> DucoData: ...
