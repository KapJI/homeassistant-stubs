from .const import DOMAIN as DOMAIN, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from airos.airos6 import AirOS6, AirOS6Data
from airos.airos8 import AirOS8, AirOS8Data
from airos.helpers import DetectDeviceData as DetectDeviceData
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
AirOSDeviceDetect = AirOS8 | AirOS6
AirOSDataDetect = AirOS8Data | AirOS6Data
type AirOSConfigEntry = ConfigEntry[AirOSDataUpdateCoordinator]

class AirOSDataUpdateCoordinator(DataUpdateCoordinator[AirOSDataDetect]):
    airos_device: AirOSDeviceDetect
    config_entry: AirOSConfigEntry
    device_data: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: AirOSConfigEntry, device_data: DetectDeviceData, airos_device: AirOSDeviceDetect) -> None: ...
    async def _async_update_data(self) -> AirOSDataDetect: ...
