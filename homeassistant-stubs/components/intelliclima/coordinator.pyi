from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN, FILTER_SCAN_INTERVAL as FILTER_SCAN_INTERVAL, LOGGER as LOGGER
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyintelliclima import IntelliClimaAPI as IntelliClimaAPI, IntelliClimaDevices
from pyintelliclima.intelliclima_types import IntelliClimaFilterStatus
from typing import override

type IntelliClimaConfigEntry = ConfigEntry[IntelliClimaData]
class IntelliClimaCoordinator(DataUpdateCoordinator[IntelliClimaDevices]):
    api: Incomplete
    def __init__(self, hass: HomeAssistant, entry: IntelliClimaConfigEntry, api: IntelliClimaAPI) -> None: ...
    @override
    async def _async_setup(self) -> None: ...
    @override
    async def _async_update_data(self) -> IntelliClimaDevices: ...

class IntelliClimaFilterCoordinator(DataUpdateCoordinator[dict[str, IntelliClimaFilterStatus]]):
    api: Incomplete
    _device_serials: Incomplete
    def __init__(self, hass: HomeAssistant, entry: IntelliClimaConfigEntry, api: IntelliClimaAPI, device_serials: list[str]) -> None: ...
    @override
    async def _async_update_data(self) -> dict[str, IntelliClimaFilterStatus]: ...

@dataclass
class IntelliClimaData:
    devices_coordinator: IntelliClimaCoordinator
    filter_coordinator: IntelliClimaFilterCoordinator
