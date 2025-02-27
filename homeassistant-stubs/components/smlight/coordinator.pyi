import abc
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SCAN_FIRMWARE_INTERVAL as SCAN_FIRMWARE_INTERVAL, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from abc import abstractmethod
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pysmlight import Api2 as Api2, Info as Info, Sensors
from pysmlight.const import Settings as Settings
from pysmlight.models import FirmwareList as FirmwareList

@dataclass(kw_only=True)
class SmlightData:
    data: SmDataUpdateCoordinator
    firmware: SmFirmwareUpdateCoordinator

@dataclass
class SmData:
    sensors: Sensors
    info: Info

@dataclass
class SmFwData:
    info: Info
    esp_firmware: FirmwareList
    zb_firmware: list[FirmwareList]
type SmConfigEntry = ConfigEntry[SmlightData]

class SmBaseDataUpdateCoordinator[_DataT](DataUpdateCoordinator[_DataT], metaclass=abc.ABCMeta):
    config_entry: SmConfigEntry
    client: Incomplete
    unique_id: str | None
    legacy_api: int
    def __init__(self, hass: HomeAssistant, config_entry: SmConfigEntry, client: Api2) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> _DataT: ...
    @abstractmethod
    async def _internal_update_data(self) -> _DataT: ...

class SmDataUpdateCoordinator(SmBaseDataUpdateCoordinator[SmData]):
    def update_setting(self, setting: Settings, value: bool | int) -> None: ...
    async def _internal_update_data(self) -> SmData: ...

class SmFirmwareUpdateCoordinator(SmBaseDataUpdateCoordinator[SmFwData]):
    update_interval: Incomplete
    in_progress: bool
    def __init__(self, hass: HomeAssistant, config_entry: SmConfigEntry, client: Api2) -> None: ...
    async def _internal_update_data(self) -> SmFwData: ...
