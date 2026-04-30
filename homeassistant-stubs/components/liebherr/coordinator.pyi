from .const import DOMAIN as DOMAIN, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from dataclasses import dataclass, field
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyliebherrhomeapi import DeviceState, LiebherrClient as LiebherrClient

_LOGGER: Incomplete

@dataclass
class LiebherrData:
    client: LiebherrClient
    coordinators: dict[str, LiebherrCoordinator] = field(default_factory=dict)
type LiebherrConfigEntry = ConfigEntry[LiebherrData]

class LiebherrCoordinator(DataUpdateCoordinator[DeviceState]):
    client: Incomplete
    device_id: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: LiebherrConfigEntry, client: LiebherrClient, device_id: str) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> DeviceState: ...
