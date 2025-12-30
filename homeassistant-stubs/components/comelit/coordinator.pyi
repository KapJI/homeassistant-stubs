import abc
from .const import DOMAIN as DOMAIN, ObjectClassType as ObjectClassType, SCAN_INTERVAL as SCAN_INTERVAL, _LOGGER as _LOGGER
from _typeshed import Incomplete
from abc import abstractmethod
from aiocomelit.api import ComelitCommonApi as ComelitCommonApi, ComelitVedoApi, ComeliteSerialBridgeApi
from aiohttp import ClientSession as ClientSession
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import TypeVar

type ComelitConfigEntry = ConfigEntry[ComelitBaseCoordinator]
T = TypeVar('T', bound=dict[str, Mapping[int, ObjectClassType]])

class ComelitBaseCoordinator(DataUpdateCoordinator[T], metaclass=abc.ABCMeta):
    _hw_version: str
    config_entry: ComelitConfigEntry
    api: ComelitCommonApi
    _device: Incomplete
    _host: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ComelitConfigEntry, device: str, host: str) -> None: ...
    def platform_device_info(self, object_class: ObjectClassType, object_type: str) -> dr.DeviceInfo: ...
    async def _async_update_data(self) -> T: ...
    @abstractmethod
    async def _async_update_system_data(self) -> T: ...
    async def _async_remove_stale_devices(self, previous_list: Mapping[int, ObjectClassType], current_list: Mapping[int, ObjectClassType], dev_type: str) -> None: ...

class ComelitSerialBridge(ComelitBaseCoordinator[T]):
    _hw_version: str
    api: ComeliteSerialBridgeApi
    vedo_pin: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ComelitConfigEntry, host: str, port: int, pin: str, vedo_pin: str | None, session: ClientSession) -> None: ...
    async def _async_update_system_data(self) -> T: ...

class ComelitVedoSystem(ComelitBaseCoordinator[T]):
    _hw_version: str
    api: ComelitVedoApi
    vedo_pin: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ComelitConfigEntry, host: str, port: int, pin: str, session: ClientSession) -> None: ...
    async def _async_update_system_data(self) -> T: ...
