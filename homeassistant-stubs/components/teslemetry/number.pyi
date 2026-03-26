from . import TeslemetryConfigEntry as TeslemetryConfigEntry
from .entity import TeslemetryEnergyInfoEntity as TeslemetryEnergyInfoEntity, TeslemetryRootEntity as TeslemetryRootEntity, TeslemetryVehiclePollingEntity as TeslemetryVehiclePollingEntity, TeslemetryVehicleStreamEntity as TeslemetryVehicleStreamEntity
from .helpers import handle_command as handle_command, handle_vehicle_command as handle_vehicle_command
from .models import TeslemetryEnergyData as TeslemetryEnergyData, TeslemetryVehicleData as TeslemetryVehicleData
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode, RestoreNumber as RestoreNumber
from homeassistant.const import PERCENTAGE as PERCENTAGE, PRECISION_WHOLE as PRECISION_WHOLE, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, UnitOfElectricCurrent as UnitOfElectricCurrent
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from tesla_fleet_api.const import Scope
from tesla_fleet_api.teslemetry import EnergySite as EnergySite, Vehicle as Vehicle
from teslemetry_stream import TeslemetryStreamVehicle as TeslemetryStreamVehicle
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class TeslemetryNumberVehicleEntityDescription(NumberEntityDescription):
    func: Callable[[Vehicle, int], Awaitable[Any]]
    min_key: str | None = ...
    max_key: str
    native_min_value: float
    native_max_value: float
    scopes: list[Scope]
    value_listener: Callable[[TeslemetryStreamVehicle, Callable[[int | None], None]], Callable[[], None]]
    max_listener: Callable[[TeslemetryStreamVehicle, Callable[[int | None], None]], Callable[[], None]] | None = ...

VEHICLE_DESCRIPTIONS: tuple[TeslemetryNumberVehicleEntityDescription, ...]

@dataclass(frozen=True, kw_only=True)
class TeslemetryNumberBatteryEntityDescription(NumberEntityDescription):
    func: Callable[[EnergySite, float], Awaitable[Any]]
    requires: str | None = ...
    scopes: list[Scope]

ENERGY_INFO_DESCRIPTIONS: tuple[TeslemetryNumberBatteryEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TeslemetryConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TeslemetryVehicleNumberEntity(TeslemetryRootEntity, NumberEntity):
    api: Vehicle
    entity_description: TeslemetryNumberVehicleEntityDescription
    _attr_native_value: Incomplete
    async def async_set_native_value(self, value: float) -> None: ...

class TeslemetryVehiclePollingNumberEntity(TeslemetryVehiclePollingEntity, TeslemetryVehicleNumberEntity):
    scoped: Incomplete
    entity_description: Incomplete
    def __init__(self, data: TeslemetryVehicleData, description: TeslemetryNumberVehicleEntityDescription, scopes: list[Scope]) -> None: ...
    _attr_native_value: Incomplete
    _attr_native_max_value: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryStreamingNumberEntity(TeslemetryVehicleStreamEntity, TeslemetryVehicleNumberEntity, RestoreNumber):
    entity_description: TeslemetryNumberVehicleEntityDescription
    scoped: Incomplete
    _attr_native_max_value: Incomplete
    def __init__(self, data: TeslemetryVehicleData, description: TeslemetryNumberVehicleEntityDescription, scopes: list[Scope]) -> None: ...
    _attr_native_value: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def _value_callback(self, value: int | None) -> None: ...
    def _max_callback(self, value: int | None) -> None: ...

class TeslemetryEnergyInfoNumberSensorEntity(TeslemetryEnergyInfoEntity, NumberEntity):
    entity_description: TeslemetryNumberBatteryEntityDescription
    _attr_native_step = PRECISION_WHOLE
    _attr_native_min_value: int
    _attr_native_max_value: int
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement = PERCENTAGE
    scoped: Incomplete
    def __init__(self, data: TeslemetryEnergyData, description: TeslemetryNumberBatteryEntityDescription, scopes: list[Scope]) -> None: ...
    _attr_native_value: Incomplete
    def _async_update_attrs(self) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
