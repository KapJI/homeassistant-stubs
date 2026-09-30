from . import BitvisConfigEntry as BitvisConfigEntry
from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import BitvisDataUpdateCoordinator as BitvisDataUpdateCoordinator
from _typeshed import Incomplete
from bitvis_protobuf.han_port_pb2 import HanPortSample as HanPortSample
from bitvis_protobuf.powerhub_pb2 import Diagnostic as Diagnostic
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfReactiveEnergy as UnitOfReactiveEnergy, UnitOfReactivePower as UnitOfReactivePower
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

PARALLEL_UPDATES: int

def _optional(field: str) -> Callable[[HanPortSample], float | None]: ...

@dataclass(frozen=True, kw_only=True)
class BitvisSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[HanPortSample], float | None]

@dataclass(frozen=True, kw_only=True)
class BitvisDiagnosticSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Diagnostic], float | int | str | datetime | None]

SENSOR_DESCRIPTIONS: tuple[BitvisSensorEntityDescription, ...]
UPTIME_DESCRIPTION: Incomplete
DIAGNOSTIC_SENSOR_DESCRIPTIONS: tuple[BitvisDiagnosticSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: BitvisConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BitvisBaseSensorEntity(CoordinatorEntity[BitvisDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: BitvisDataUpdateCoordinator, description: SensorEntityDescription) -> None: ...

class BitvisSensorEntity(BitvisBaseSensorEntity):
    entity_description: BitvisSensorEntityDescription
    @property
    @override
    def native_value(self) -> float | None: ...
    @property
    @override
    def available(self) -> bool: ...

class BitvisDiagnosticSensorEntity(BitvisBaseSensorEntity):
    entity_description: BitvisDiagnosticSensorEntityDescription
    @property
    @override
    def native_value(self) -> float | int | str | datetime | None: ...
    @property
    @override
    def available(self) -> bool: ...

class BitvisUptimeSensorEntity(BitvisBaseSensorEntity):
    @property
    @override
    def native_value(self) -> datetime | None: ...
    @property
    @override
    def available(self) -> bool: ...
