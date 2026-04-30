from .const import DOMAIN as DOMAIN, SCAN_INTERVAL as SCAN_INTERVAL, UPDATE_SCAN_INTERVAL as UPDATE_SCAN_INTERVAL
from _typeshed import Incomplete
from airos.airos6 import AirOS6, AirOS6Data
from airos.airos8 import AirOS8, AirOS8Data
from airos.helpers import DetectDeviceData as DetectDeviceData
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any, TypeVar

_LOGGER: Incomplete
type AirOSDeviceDetect = AirOS8 | AirOS6
type AirOSDataDetect = AirOS8Data | AirOS6Data
type AirOSUpdateData = dict[str, Any]
type AirOSConfigEntry = ConfigEntry[AirOSRuntimeData]
T = TypeVar('T', bound=AirOSDataDetect | AirOSUpdateData)

@dataclass
class AirOSRuntimeData:
    status: AirOSDataUpdateCoordinator
    firmware: AirOSFirmwareUpdateCoordinator | None

async def async_fetch_airos_data(airos_device: AirOSDeviceDetect, update_method: Callable[[], Awaitable[T]]) -> T: ...

class AirOSDataUpdateCoordinator(DataUpdateCoordinator[AirOSDataDetect]):
    config_entry: AirOSConfigEntry
    airos_device: Incomplete
    device_data: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: AirOSConfigEntry, device_data: DetectDeviceData, airos_device: AirOSDeviceDetect) -> None: ...
    async def _async_update_data(self) -> AirOSDataDetect: ...

class AirOSFirmwareUpdateCoordinator(DataUpdateCoordinator[AirOSUpdateData]):
    config_entry: AirOSConfigEntry
    airos_device: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: AirOSConfigEntry, airos_device: AirOSDeviceDetect) -> None: ...
    async def _async_update_data(self) -> AirOSUpdateData: ...
