from . import TeslemetryConfigEntry as TeslemetryConfigEntry
from .const import DOMAIN as DOMAIN, ENERGY_HISTORY_FIELDS as ENERGY_HISTORY_FIELDS, LOGGER as LOGGER
from .helpers import flatten as flatten
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from tesla_fleet_api.exceptions import TeslaFleetError
from tesla_fleet_api.teslemetry import EnergySite as EnergySite, Teslemetry as Teslemetry, Vehicle as Vehicle
from typing import Any

RETRY_EXCEPTIONS: Incomplete

def _get_retry_after(e: TeslaFleetError) -> float: ...

VEHICLE_INTERVAL: Incomplete
VEHICLE_WAIT: Incomplete
ENERGY_LIVE_INTERVAL: Incomplete
ENERGY_INFO_INTERVAL: Incomplete
ENERGY_HISTORY_INTERVAL: Incomplete
METADATA_INTERVAL: Incomplete
ENDPOINTS: Incomplete

class TeslemetryMetadataCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: TeslemetryConfigEntry
    teslemetry: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: TeslemetryConfigEntry, teslemetry: Teslemetry) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...

class TeslemetryVehicleDataCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: TeslemetryConfigEntry
    last_active: datetime
    update_interval: Incomplete
    api: Incomplete
    data: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: TeslemetryConfigEntry, api: Vehicle, product: dict[str, Any]) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...

class TeslemetryEnergySiteLiveCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: TeslemetryConfigEntry
    updated_once: bool
    api: Incomplete
    data: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: TeslemetryConfigEntry, api: EnergySite, data: dict[str, Any]) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...

class TeslemetryEnergySiteInfoCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: TeslemetryConfigEntry
    api: Incomplete
    data: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: TeslemetryConfigEntry, api: EnergySite, product: dict[str, Any]) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...

class TeslemetryEnergyHistoryCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: TeslemetryConfigEntry
    api: Incomplete
    data: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: TeslemetryConfigEntry, api: EnergySite) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
