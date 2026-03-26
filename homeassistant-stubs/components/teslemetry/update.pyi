from . import TeslemetryConfigEntry as TeslemetryConfigEntry
from .entity import TeslemetryRootEntity as TeslemetryRootEntity, TeslemetryVehiclePollingEntity as TeslemetryVehiclePollingEntity, TeslemetryVehicleStreamEntity as TeslemetryVehicleStreamEntity
from .helpers import handle_vehicle_command as handle_vehicle_command
from .models import TeslemetryVehicleData as TeslemetryVehicleData
from _typeshed import Incomplete
from homeassistant.components.update import UpdateEntity as UpdateEntity, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from tesla_fleet_api.const import Scope
from tesla_fleet_api.teslemetry import Vehicle as Vehicle
from typing import Any

AVAILABLE: str
DOWNLOADING: str
INSTALLING: str
WIFI_WAIT: str
SCHEDULED: str
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: TeslemetryConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TeslemetryUpdateEntity(TeslemetryRootEntity, UpdateEntity):
    api: Vehicle
    _attr_supported_features: Incomplete
    _attr_in_progress: bool
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...

class TeslemetryVehiclePollingUpdateEntity(TeslemetryVehiclePollingEntity, TeslemetryUpdateEntity):
    scoped: Incomplete
    def __init__(self, data: TeslemetryVehicleData, scopes: list[Scope]) -> None: ...
    _attr_supported_features: Incomplete
    _attr_installed_version: Incomplete
    _attr_latest_version: Incomplete
    _attr_in_progress: bool
    _attr_update_percentage: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryStreamingUpdateEntity(TeslemetryVehicleStreamEntity, TeslemetryUpdateEntity, RestoreEntity):
    _download_percentage: int
    _install_percentage: int
    scoped: Incomplete
    def __init__(self, data: TeslemetryVehicleData, scopes: list[Scope]) -> None: ...
    _attr_in_progress: Incomplete
    _attr_installed_version: Incomplete
    _attr_latest_version: Incomplete
    _attr_supported_features: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def _async_handle_software_update_download_percent_complete(self, value: float | None) -> None: ...
    def _async_handle_software_update_installation_percent_complete(self, value: float | None) -> None: ...
    def _async_handle_software_update_scheduled_start_time(self, value: str | None) -> None: ...
    def _async_handle_software_update_version(self, value: str | None) -> None: ...
    def _async_handle_version(self, value: str | None) -> None: ...
    _attr_update_percentage: Incomplete
    def _async_update_progress(self) -> None: ...
