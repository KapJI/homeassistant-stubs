from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from arcam.fmj.client import Client as Client
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
    last_update_success: bool
    device_info: Incomplete
    zone_unique_id: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ArcamFmjConfigEntry, client: Client, zone: int) -> None: ...
    async def _async_update_data(self) -> None: ...
    @callback
    def async_notify_data_updated(self) -> None: ...
    @callback
    def async_notify_connected(self) -> None: ...
    @callback
    def async_notify_disconnected(self) -> None: ...
