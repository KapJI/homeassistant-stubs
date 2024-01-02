import abc
from .config_flow import ConfigFlow as ConfigFlow
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyprusalink import JobInfo, LegacyPrinterStatus, PrinterStatus, PrusaLink
from typing import TypeVar

PLATFORMS: list[Platform]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
T = TypeVar('T', PrinterStatus, LegacyPrinterStatus, JobInfo)

class PrusaLinkUpdateCoordinator(DataUpdateCoordinator[T], ABC, metaclass=abc.ABCMeta):
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

class StatusCoordinator(PrusaLinkUpdateCoordinator[PrinterStatus]):
    async def _fetch_data(self) -> PrinterStatus: ...

class LegacyStatusCoordinator(PrusaLinkUpdateCoordinator[LegacyPrinterStatus]):
    async def _fetch_data(self) -> LegacyPrinterStatus: ...

class JobUpdateCoordinator(PrusaLinkUpdateCoordinator[JobInfo]):
    async def _fetch_data(self) -> JobInfo: ...

class PrusaLinkEntity(CoordinatorEntity[PrusaLinkUpdateCoordinator]):
    _attr_has_entity_name: bool
    @property
    def device_info(self) -> DeviceInfo: ...
