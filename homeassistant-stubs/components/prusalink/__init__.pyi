import abc
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyprusalink import JobInfo, PrinterInfo, PrusaLink
from typing import Generic, TypeVar

PLATFORMS: list[Platform]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
T = TypeVar('T', PrinterInfo, JobInfo)

class PrusaLinkUpdateCoordinator(DataUpdateCoordinator, ABC, Generic[T], metaclass=abc.ABCMeta):
    config_entry: ConfigEntry
    expect_change_until: float
    api: Incomplete
    def __init__(self, hass: HomeAssistant, api: PrusaLink) -> None: ...
    update_interval: Incomplete
    async def _async_update_data(self) -> T: ...
    @abstractmethod
    async def _fetch_data(self) -> T: ...
    def expect_change(self) -> None: ...
    def _get_update_interval(self, data: T) -> timedelta: ...

class PrinterUpdateCoordinator(PrusaLinkUpdateCoordinator[PrinterInfo]):
    async def _fetch_data(self) -> PrinterInfo: ...
    def _get_update_interval(self, data: T) -> timedelta: ...

class JobUpdateCoordinator(PrusaLinkUpdateCoordinator[JobInfo]):
    async def _fetch_data(self) -> JobInfo: ...

class PrusaLinkEntity(CoordinatorEntity[PrusaLinkUpdateCoordinator]):
    _attr_has_entity_name: bool
    @property
    def device_info(self) -> DeviceInfo: ...
