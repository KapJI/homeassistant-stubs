from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from lunatone_rest_api_client import Device, Devices as Devices, Info as Info
from lunatone_rest_api_client.models import InfoData

_LOGGER: Incomplete
DEFAULT_DEVICES_SCAN_INTERVAL: Incomplete

@dataclass
class LunatoneData:
    coordinator_info: LunatoneInfoDataUpdateCoordinator
    coordinator_devices: LunatoneDevicesDataUpdateCoordinator
type LunatoneConfigEntry = ConfigEntry[LunatoneData]

class LunatoneInfoDataUpdateCoordinator(DataUpdateCoordinator[InfoData]):
    config_entry: LunatoneConfigEntry
    info_api: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: LunatoneConfigEntry, info_api: Info) -> None: ...
    async def _async_update_data(self) -> InfoData: ...

class LunatoneDevicesDataUpdateCoordinator(DataUpdateCoordinator[dict[int, Device]]):
    config_entry: LunatoneConfigEntry
    devices_api: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: LunatoneConfigEntry, devices_api: Devices) -> None: ...
    async def _async_update_data(self) -> dict[int, Device]: ...
