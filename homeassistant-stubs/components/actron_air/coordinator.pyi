from .const import DOMAIN as DOMAIN, _LOGGER as _LOGGER
from _typeshed import Incomplete
from actron_neo_api import ActronAirAPI as ActronAirAPI, ActronAirStatus
from actron_neo_api.models.system import ActronAirSystemInfo as ActronAirSystemInfo
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

SCAN_INTERVAL: Incomplete
STALE_DEVICE_TIMEOUT: Incomplete
ERROR_NO_SYSTEMS_FOUND: str
ERROR_UNKNOWN: str

@dataclass
class ActronAirRuntimeData:
    api: ActronAirAPI
    system_coordinators: dict[str, ActronAirSystemCoordinator]
type ActronAirConfigEntry = ConfigEntry[ActronAirRuntimeData]

class ActronAirSystemCoordinator(DataUpdateCoordinator[ActronAirStatus]):
    system: Incomplete
    serial_number: Incomplete
    api: Incomplete
    status: Incomplete
    last_seen: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ActronAirConfigEntry, api: ActronAirAPI, system: ActronAirSystemInfo) -> None: ...
    async def _async_update_data(self) -> ActronAirStatus: ...
    def is_device_stale(self) -> bool: ...
