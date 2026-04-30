from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from arcam.fmj.client import AmxDuetResponse as AmxDuetResponse, Client as Client, ResponsePacket
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete

@dataclass
class ArcamFmjRuntimeData:
    client: Client
    coordinators: dict[int, ArcamFmjCoordinator]
type ArcamFmjConfigEntry = ConfigEntry[ArcamFmjRuntimeData]

class ArcamFmjCoordinator(DataUpdateCoordinator[None]):
    config_entry: ArcamFmjConfigEntry
    client: Incomplete
    state: Incomplete
    update_in_progress: bool
    device_info: Incomplete
    zone_unique_id: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ArcamFmjConfigEntry, client: Client, zone: int) -> None: ...
    async def _async_update_data(self) -> None: ...
    @callback
    def _async_notify_packet(self, packet: ResponsePacket | AmxDuetResponse) -> None: ...
    @asynccontextmanager
    async def async_monitor_client(self) -> AsyncGenerator[None]: ...
