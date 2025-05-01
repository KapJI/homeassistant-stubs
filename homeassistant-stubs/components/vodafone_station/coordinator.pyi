from .const import DOMAIN as DOMAIN, SCAN_INTERVAL as SCAN_INTERVAL, _LOGGER as _LOGGER
from .helpers import cleanup_device_tracker as cleanup_device_tracker
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from aiovodafone import VodafoneStationDevice as VodafoneStationDevice
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.device_tracker import DEFAULT_CONSIDER_HOME as DEFAULT_CONSIDER_HOME
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

CONSIDER_HOME_SECONDS: Incomplete
type VodafoneConfigEntry = ConfigEntry[VodafoneStationRouter]

@dataclass(slots=True)
class VodafoneStationDeviceInfo:
    device: VodafoneStationDevice
    update_time: datetime | None
    home: bool

@dataclass(slots=True)
class UpdateCoordinatorDataType:
    devices: dict[str, VodafoneStationDeviceInfo]
    sensors: dict[str, Any]

class VodafoneStationRouter(DataUpdateCoordinator[UpdateCoordinatorDataType]):
    config_entry: VodafoneConfigEntry
    _host: Incomplete
    api: Incomplete
    _id: Incomplete
    previous_devices: Incomplete
    def __init__(self, hass: HomeAssistant, host: str, username: str, password: str, config_entry: VodafoneConfigEntry, session: ClientSession) -> None: ...
    def _calculate_update_time_and_consider_home(self, device: VodafoneStationDevice, utc_point_in_time: datetime) -> tuple[datetime | None, bool]: ...
    async def _async_update_data(self) -> UpdateCoordinatorDataType: ...
    @property
    def signal_device_new(self) -> str: ...
    @property
    def serial_number(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
