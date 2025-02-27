from .helpers import PingDataICMPLib as PingDataICMPLib, PingDataSubProcess as PingDataSubProcess
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

_LOGGER: Incomplete
type PingConfigEntry = ConfigEntry[PingUpdateCoordinator]

@dataclass(slots=True, frozen=True)
class PingResult:
    ip_address: str
    is_alive: bool
    data: dict[str, Any]

class PingUpdateCoordinator(DataUpdateCoordinator[PingResult]):
    config_entry: PingConfigEntry
    ping: PingDataSubProcess | PingDataICMPLib
    def __init__(self, hass: HomeAssistant, config_entry: PingConfigEntry, ping: PingDataSubProcess | PingDataICMPLib) -> None: ...
    async def _async_update_data(self) -> PingResult: ...
