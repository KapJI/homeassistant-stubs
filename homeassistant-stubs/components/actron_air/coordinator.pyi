from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from actron_neo_api import ActronAirAPI as ActronAirAPI, ActronAirPeripheral as ActronAirPeripheral, ActronAirStatus
from actron_neo_api.models.system import ActronAirSystemInfo as ActronAirSystemInfo
from actron_neo_api.rt import RealtimeConnectionEvent as RealtimeConnectionEvent
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

POLL_INTERVAL: Incomplete
PUSH_POLL_INTERVAL: Incomplete
ERROR_NO_SYSTEMS_FOUND: str
ERROR_UNKNOWN: str
OUTAGE_STATES: Incomplete

@dataclass
class ActronAirRuntimeData:
    api: ActronAirAPI
    system_coordinators: dict[str, ActronAirSystemCoordinator]
type ActronAirConfigEntry = ConfigEntry[ActronAirRuntimeData]

class ActronAirSystemCoordinator(DataUpdateCoordinator[ActronAirStatus]):
    config_entry: ActronAirConfigEntry
    system: Incomplete
    serial_number: Incomplete
    api: Incomplete
    push_enabled: Incomplete
    status: Incomplete
    peripherals: dict[str, ActronAirPeripheral]
    _missed_updates: bool
    def __init__(self, hass: HomeAssistant, entry: ActronAirConfigEntry, api: ActronAirAPI, system: ActronAirSystemInfo, *, push_enabled: bool) -> None: ...
    @override
    async def _async_setup(self) -> None: ...
    @callback
    def _handle_push_update(self, status: ActronAirStatus) -> None: ...
    async def _handle_connection_event(self, event: RealtimeConnectionEvent) -> None: ...
    @override
    async def _async_update_data(self) -> ActronAirStatus: ...
