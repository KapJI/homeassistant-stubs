import abc
from .const import DOMAIN as DOMAIN, SCAN_INTERVAL as SCAN_INTERVAL, _LOGGER as _LOGGER
from _typeshed import Incomplete
from abc import abstractmethod
from aiocomelit.api import AlarmDataObject, ComelitCommonApi as ComelitCommonApi, ComelitSerialBridgeObject, ComelitVedoApi, ComelitVedoAreaObject as ComelitVedoAreaObject, ComelitVedoZoneObject as ComelitVedoZoneObject, ComeliteSerialBridgeApi
from aiohttp import ClientSession as ClientSession
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import TypeVar

type ComelitConfigEntry = ConfigEntry[ComelitBaseCoordinator]
T = TypeVar('T', bound=dict[str, dict[int, ComelitSerialBridgeObject]] | AlarmDataObject)

class ComelitBaseCoordinator(DataUpdateCoordinator[T], metaclass=abc.ABCMeta):
    _hw_version: str
    config_entry: ComelitConfigEntry
    api: ComelitCommonApi
    _device: Incomplete
    _host: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ComelitConfigEntry, device: str, host: str) -> None: ...
    def platform_device_info(self, object_class: ComelitVedoZoneObject | ComelitVedoAreaObject | ComelitSerialBridgeObject, object_type: str) -> dr.DeviceInfo: ...
    async def _async_update_data(self) -> T: ...
    @abstractmethod
    async def _async_update_system_data(self) -> T: ...

class ComelitSerialBridge(ComelitBaseCoordinator[dict[str, dict[int, ComelitSerialBridgeObject]]]):
    _hw_version: str
    api: ComeliteSerialBridgeApi
    def __init__(self, hass: HomeAssistant, entry: ComelitConfigEntry, host: str, port: int, pin: int, session: ClientSession) -> None: ...
    async def _async_update_system_data(self) -> dict[str, dict[int, ComelitSerialBridgeObject]]: ...

class ComelitVedoSystem(ComelitBaseCoordinator[AlarmDataObject]):
    _hw_version: str
    api: ComelitVedoApi
    def __init__(self, hass: HomeAssistant, entry: ComelitConfigEntry, host: str, port: int, pin: int, session: ClientSession) -> None: ...
    async def _async_update_system_data(self) -> AlarmDataObject: ...
