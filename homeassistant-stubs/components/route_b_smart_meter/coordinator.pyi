from .const import CONNECT_RETRIES as CONNECT_RETRIES, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN, REOPEN_DELAYS as REOPEN_DELAYS
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_ID as CONF_ID, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

_LOGGER: Incomplete

@dataclass
class BRouteData:
    instantaneous_current_r_phase: float | None
    instantaneous_current_t_phase: float | None
    instantaneous_power: float | None
    total_consumption: float | None
type BRouteConfigEntry = ConfigEntry[BRouteUpdateCoordinator]

@dataclass
class BRouteDeviceInfo:
    serial_number: str | None = ...
    manufacturer_code: str | None = ...
    echonet_version: str | None = ...

class BRouteUpdateCoordinator(DataUpdateCoordinator[BRouteData]):
    device_info_data: BRouteDeviceInfo
    device: Incomplete
    bid: Incomplete
    _password: Incomplete
    api: Incomplete
    def __init__(self, hass: HomeAssistant, entry: BRouteConfigEntry) -> None: ...
    @override
    async def _async_setup(self) -> None: ...
    def _fetch_device_info(self) -> None: ...
    def _get_data(self) -> BRouteData: ...
    @override
    async def _async_update_data(self) -> BRouteData: ...
