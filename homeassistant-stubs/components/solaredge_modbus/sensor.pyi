from .const import LOGGER as LOGGER, SUBSYSTEM_STORAGE_CAPACITY as SUBSYSTEM_STORAGE_CAPACITY
from .coordinator import SolarEdgeModbusConfigEntry as SolarEdgeModbusConfigEntry
from .entity import SolarEdgeModbusBatteryEntity as SolarEdgeModbusBatteryEntity, SolarEdgeModbusInverterEntity as SolarEdgeModbusInverterEntity, SolarEdgeModbusMeterEntity as SolarEdgeModbusMeterEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import RestoreSensor as RestoreSensor, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfApparentPower as UnitOfApparentPower, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfReactivePower as UnitOfReactivePower, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from solaredged import Battery as Battery, Inverter as Inverter, Meter as Meter, SolarEdge as SolarEdge, StorageCapacity as StorageCapacity
from typing import override

PARALLEL_UPDATES: int
_MULTI_PHASE: Incomplete
_MULTI_PHASE_METER: Incomplete
_THREE_PHASE_METER: Incomplete
_NEUTRAL_METER: Incomplete
_PHASE_NEUTRAL_METER: Incomplete

@dataclass(frozen=True, kw_only=True)
class SolarEdgeModbusSensorEntityDescription[ComponentT](SensorEntityDescription):
    exists_fn: Callable[[ComponentT], bool] = ...
    value_fn: Callable[[ComponentT], StateType]

INVERTER_SENSORS: tuple[SolarEdgeModbusSensorEntityDescription[Inverter], ...]
METER_SENSORS: tuple[SolarEdgeModbusSensorEntityDescription[Meter], ...]
BATTERY_SENSORS: tuple[SolarEdgeModbusSensorEntityDescription[Battery], ...]

def _inverter_sensor(entry: SolarEdgeModbusConfigEntry, description: SolarEdgeModbusSensorEntityDescription[Inverter]) -> SensorEntity: ...
def _meter_sensor(entry: SolarEdgeModbusConfigEntry, description: SolarEdgeModbusSensorEntityDescription[Meter], index: int) -> SensorEntity: ...
def _battery_sensor(entry: SolarEdgeModbusConfigEntry, description: SolarEdgeModbusSensorEntityDescription[Battery], index: int) -> SensorEntity: ...

STORAGE_CAPACITY_SENSORS: tuple[SolarEdgeModbusSensorEntityDescription[StorageCapacity], ...]

async def async_setup_entry(hass: HomeAssistant, entry: SolarEdgeModbusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def _reported_storage(solaredge: SolarEdge) -> StorageCapacity | None: ...

class SolarEdgeModbusInverterSensorEntity(SolarEdgeModbusInverterEntity, SensorEntity):
    entity_description: SolarEdgeModbusSensorEntityDescription[Inverter]
    @property
    @override
    def native_value(self) -> StateType: ...

class SolarEdgeModbusMeterSensorEntity(SolarEdgeModbusMeterEntity, SensorEntity):
    entity_description: SolarEdgeModbusSensorEntityDescription[Meter]
    @property
    @override
    def native_value(self) -> StateType: ...

class SolarEdgeModbusStorageCapacitySensorEntity(SolarEdgeModbusInverterEntity, SensorEntity):
    entity_description: SolarEdgeModbusSensorEntityDescription[StorageCapacity]
    _component: Incomplete
    def __init__(self, *, entry: SolarEdgeModbusConfigEntry, description: SolarEdgeModbusSensorEntityDescription[StorageCapacity], component: StorageCapacity) -> None: ...
    @property
    @override
    def native_value(self) -> StateType: ...

class SolarEdgeModbusEnergySensorEntity(RestoreSensor):
    _highest_value: float | None
    _glitch_logged: bool
    @override
    async def async_added_to_hass(self) -> None: ...
    @property
    @override
    def native_value(self) -> StateType: ...

class SolarEdgeModbusInverterEnergySensorEntity(SolarEdgeModbusEnergySensorEntity, SolarEdgeModbusInverterSensorEntity): ...
class SolarEdgeModbusMeterEnergySensorEntity(SolarEdgeModbusEnergySensorEntity, SolarEdgeModbusMeterSensorEntity): ...

class SolarEdgeModbusBatterySensorEntity(SolarEdgeModbusBatteryEntity, SensorEntity):
    entity_description: SolarEdgeModbusSensorEntityDescription[Battery]
    @property
    @override
    def native_value(self) -> StateType: ...

class SolarEdgeModbusBatteryEnergySensorEntity(SolarEdgeModbusEnergySensorEntity, SolarEdgeModbusBatterySensorEntity): ...
