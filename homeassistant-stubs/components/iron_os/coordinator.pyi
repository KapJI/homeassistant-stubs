from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pynecil import CharSetting as CharSetting, DeviceInfoResponse as DeviceInfoResponse, IronOSUpdate as IronOSUpdate, LatestRelease, LiveDataResponse, Pynecil as Pynecil, SettingsDataResponse

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
SCAN_INTERVAL_GITHUB: Incomplete
SCAN_INTERVAL_SETTINGS: Incomplete

@dataclass
class IronOSCoordinators:
    live_data: IronOSLiveDataCoordinator
    settings: IronOSSettingsCoordinator
type IronOSConfigEntry = ConfigEntry[IronOSCoordinators]

class IronOSBaseCoordinator[_DataT](DataUpdateCoordinator[_DataT]):
    device_info: DeviceInfoResponse
    config_entry: IronOSConfigEntry
    device: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: IronOSConfigEntry, device: Pynecil, update_interval: timedelta) -> None: ...
    async def _async_setup(self) -> None: ...

class IronOSLiveDataCoordinator(IronOSBaseCoordinator[LiveDataResponse]):
    def __init__(self, hass: HomeAssistant, config_entry: IronOSConfigEntry, device: Pynecil) -> None: ...
    device_info: Incomplete
    async def _async_update_data(self) -> LiveDataResponse: ...
    @property
    def has_tip(self) -> bool: ...

class IronOSSettingsCoordinator(IronOSBaseCoordinator[SettingsDataResponse]):
    def __init__(self, hass: HomeAssistant, config_entry: IronOSConfigEntry, device: Pynecil) -> None: ...
    async def _async_update_data(self) -> SettingsDataResponse: ...
    async def write(self, characteristic: CharSetting, value: bool | Enum | float) -> None: ...

class IronOSFirmwareUpdateCoordinator(DataUpdateCoordinator[LatestRelease]):
    github: Incomplete
    def __init__(self, hass: HomeAssistant, github: IronOSUpdate) -> None: ...
    async def _async_update_data(self) -> LatestRelease: ...
