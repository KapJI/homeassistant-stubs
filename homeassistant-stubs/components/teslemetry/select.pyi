from . import TeslemetryConfigEntry as TeslemetryConfigEntry
from .entity import TeslemetryEnergyInfoEntity as TeslemetryEnergyInfoEntity, TeslemetryRootEntity as TeslemetryRootEntity, TeslemetryVehiclePollingEntity as TeslemetryVehiclePollingEntity, TeslemetryVehicleStreamEntity as TeslemetryVehicleStreamEntity
from .helpers import handle_command as handle_command, handle_vehicle_command as handle_vehicle_command
from .models import TeslemetryEnergyData as TeslemetryEnergyData, TeslemetryVehicleData as TeslemetryVehicleData
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from tesla_fleet_api.const import Scope
from tesla_fleet_api.teslemetry import Vehicle as Vehicle
from teslemetry_stream import TeslemetryStreamVehicle as TeslemetryStreamVehicle
from typing import Any

OFF: str
LOW: str
MEDIUM: str
HIGH: str
PARALLEL_UPDATES: int
LEVEL: Incomplete

@dataclass(frozen=True, kw_only=True)
class TeslemetrySelectEntityDescription(SelectEntityDescription):
    select_fn: Callable[[Vehicle, int], Awaitable[Any]]
    supported_fn: Callable[[dict], bool] = ...
    streaming_listener: Callable[[TeslemetryStreamVehicle, Callable[[int | None], None]], Callable[[], None]] | None = ...
    options: list[str]

VEHICLE_DESCRIPTIONS: tuple[TeslemetrySelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TeslemetryConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TeslemetrySelectEntity(TeslemetryRootEntity, SelectEntity):
    api: Vehicle
    entity_description: TeslemetrySelectEntityDescription
    _climate: bool
    _attr_current_option: Incomplete
    async def async_select_option(self, option: str) -> None: ...

class TeslemetryVehiclePollingSelectEntity(TeslemetryVehiclePollingEntity, TeslemetrySelectEntity):
    entity_description: Incomplete
    scoped: Incomplete
    def __init__(self, data: TeslemetryVehicleData, description: TeslemetrySelectEntityDescription, scopes: list[Scope]) -> None: ...
    _climate: Incomplete
    _attr_current_option: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryStreamingSelectEntity(TeslemetryVehicleStreamEntity, TeslemetrySelectEntity, RestoreEntity):
    entity_description: Incomplete
    scoped: Incomplete
    _attr_current_option: Incomplete
    def __init__(self, data: TeslemetryVehicleData, description: TeslemetrySelectEntityDescription, scopes: list[Scope]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _value_callback(self, value: int | None) -> None: ...
    _climate: Incomplete
    def _climate_callback(self, value: bool | None) -> None: ...

class TeslemetryOperationSelectEntity(TeslemetryEnergyInfoEntity, SelectEntity):
    _attr_options: list[str]
    scoped: Incomplete
    def __init__(self, data: TeslemetryEnergyData, scopes: list[Scope]) -> None: ...
    _attr_current_option: Incomplete
    def _async_update_attrs(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...

class TeslemetryExportRuleSelectEntity(TeslemetryEnergyInfoEntity, SelectEntity, RestoreEntity):
    _attr_options: list[str]
    scoped: Incomplete
    def __init__(self, data: TeslemetryEnergyData, scopes: list[Scope]) -> None: ...
    _attr_current_option: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def _async_update_attrs(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
