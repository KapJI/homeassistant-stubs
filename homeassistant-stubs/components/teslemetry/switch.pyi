from . import TeslemetryConfigEntry as TeslemetryConfigEntry
from .entity import TeslemetryEnergyInfoEntity as TeslemetryEnergyInfoEntity, TeslemetryRootEntity as TeslemetryRootEntity, TeslemetryVehiclePollingEntity as TeslemetryVehiclePollingEntity, TeslemetryVehicleStreamEntity as TeslemetryVehicleStreamEntity
from .helpers import handle_command as handle_command, handle_vehicle_command as handle_vehicle_command
from .models import TeslemetryEnergyData as TeslemetryEnergyData, TeslemetryVehicleData as TeslemetryVehicleData
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import StateType as StateType
from tesla_fleet_api.const import Scope
from tesla_fleet_api.teslemetry import Vehicle as Vehicle
from teslemetry_stream import TeslemetryStreamVehicle as TeslemetryStreamVehicle
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class TeslemetrySwitchEntityDescription(SwitchEntityDescription):
    polling: bool = ...
    on_func: Callable[[Vehicle], Awaitable[dict[str, Any]]]
    off_func: Callable[[Vehicle], Awaitable[dict[str, Any]]]
    scopes: list[Scope]
    value_func: Callable[[StateType], bool] = ...
    streaming_listener: Callable[[TeslemetryStreamVehicle, Callable[[bool | None], None]], Callable[[], None]]
    streaming_firmware: str = ...
    unique_id: str | None = ...

VEHICLE_DESCRIPTIONS: tuple[TeslemetrySwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TeslemetryConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TeslemetryVehicleSwitchEntity(TeslemetryRootEntity, SwitchEntity):
    api: Vehicle
    _attr_device_class: Incomplete
    entity_description: TeslemetrySwitchEntityDescription
    _attr_is_on: bool
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class TeslemetryVehiclePollingVehicleSwitchEntity(TeslemetryVehiclePollingEntity, TeslemetryVehicleSwitchEntity):
    entity_description: Incomplete
    scoped: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, data: TeslemetryVehicleData, description: TeslemetrySwitchEntityDescription, scopes: list[Scope]) -> None: ...
    _attr_is_on: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryStreamingVehicleSwitchEntity(TeslemetryVehicleStreamEntity, TeslemetryVehicleSwitchEntity, RestoreEntity):
    entity_description: Incomplete
    scoped: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, data: TeslemetryVehicleData, description: TeslemetrySwitchEntityDescription, scopes: list[Scope]) -> None: ...
    _attr_is_on: bool
    async def async_added_to_hass(self) -> None: ...
    def _value_callback(self, value: bool | None) -> None: ...

class TeslemetryChargeFromGridSwitchEntity(TeslemetryEnergyInfoEntity, SwitchEntity):
    _attr_device_class: Incomplete
    scoped: Incomplete
    def __init__(self, data: TeslemetryEnergyData, scopes: list[Scope]) -> None: ...
    _attr_is_on: Incomplete
    def _async_update_attrs(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class TeslemetryStormModeSwitchEntity(TeslemetryEnergyInfoEntity, SwitchEntity):
    _attr_device_class: Incomplete
    scoped: Incomplete
    def __init__(self, data: TeslemetryEnergyData, scopes: list[Scope]) -> None: ...
    _attr_available: Incomplete
    _attr_is_on: Incomplete
    def _async_update_attrs(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
