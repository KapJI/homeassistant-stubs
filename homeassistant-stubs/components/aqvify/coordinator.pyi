from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.dt import utcnow as utcnow
from pyaqvify import AqvifyAPI as AqvifyAPI, AqvifyDeviceData as AqvifyDeviceData, AqvifyDevices as AqvifyDevices, AqvifyHourAggregatedValues
from typing import override

_LOGGER: Incomplete
UPDATE_INTERVAL: Incomplete
UPDATE_INTERVAL_SLOW: Incomplete
type AqvifyConfigEntry = ConfigEntry[AqvifyRuntimeData]

@dataclass
class AqvifyRuntimeData:
    coordinator: AqvifyCoordinator
    aggr_data_coordinator: AqvifyAggrDataCoordinator

@dataclass
class AqvifyCoordinatorData:
    devices: AqvifyDevices
    device_data: dict[str, AqvifyDeviceData]

class AqvifyCoordinator(DataUpdateCoordinator[AqvifyCoordinatorData]):
    config_entry: AqvifyConfigEntry
    api_client: Incomplete
    previous_devices: set[str]
    def __init__(self, hass: HomeAssistant, entry: AqvifyConfigEntry, api_client: AqvifyAPI) -> None: ...
    @override
    async def _async_setup(self) -> None: ...
    @override
    async def _async_update_data(self) -> AqvifyCoordinatorData: ...
    def async_add_devices(self, added_devices: set[str]) -> tuple[set[str], set[str]]: ...

class AqvifyAggrDataCoordinator(DataUpdateCoordinator[dict[str, AqvifyHourAggregatedValues]]):
    config_entry: AqvifyConfigEntry
    api_client: Incomplete
    def __init__(self, hass: HomeAssistant, entry: AqvifyConfigEntry, api_client: AqvifyAPI) -> None: ...
    @staticmethod
    def _get_times() -> tuple[str, str]: ...
    @override
    async def _async_update_data(self) -> dict[str, AqvifyHourAggregatedValues]: ...
