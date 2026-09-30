from .const import METER_ENERGY as METER_ENERGY
from .coordinator import SofarConfigEntry as SofarConfigEntry
from .entity import SofarEntity as SofarEntity, SofarEntityDescription as SofarEntityDescription
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from datetime import date
from homeassistant.components.sensor import RestoreSensor as RestoreSensor, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfApparentPower as UnitOfApparentPower, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfReactivePower as UnitOfReactivePower, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from sofar_modbus.model import CorrectedTotal as CorrectedTotal
from sofar_modbus.modern.device import SofarInverter as SofarInverter
from typing import override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: SofarConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def _is_battery_pack(description: SofarSensorDescription) -> bool: ...
def _sensor_class(description: SofarSensorDescription) -> type[SofarSensor | SofarTotalSensor]: ...

class SofarSensor(SofarEntity, SensorEntity):
    entity_description: SofarSensorDescription
    @property
    @override
    def native_value(self) -> str | int | float | date | None: ...

class SofarTotalSensor(SofarEntity, RestoreSensor):
    entity_description: SofarSensorDescription
    _attr_native_value: Incomplete
    @override
    async def async_added_to_hass(self) -> None: ...
    @property
    @override
    def native_value(self) -> int | float | None: ...

@dataclass(frozen=True, kw_only=True)
class SofarSensorDescription(SensorEntityDescription, SofarEntityDescription):
    value_fn: Callable[[SofarInverter], StateType]
    total_fn: Callable[[SofarInverter], CorrectedTotal] | None = ...

@dataclass(frozen=True, kw_only=True)
class _PartMeasurement:
    key: str
    translation_key: str
    device_class: SensorDeviceClass | None = ...
    native_unit_of_measurement: str | None = ...
    state_class: SensorStateClass | None = ...
    suggested_display_precision: int | None = ...
    entity_category: EntityCategory | None = ...
    entity_registry_enabled_default: bool = ...
    value_fn: Callable[[SofarInverter, int], StateType]

_PV_STRING_MEASUREMENTS: Incomplete
_BATTERY_MEASUREMENTS: Incomplete

def _part_sensors(kind: str, components: Mapping[int, str], measurements: tuple[_PartMeasurement, ...]) -> tuple[SofarSensorDescription, ...]: ...
def _part_value_fn(value_fn: Callable[[SofarInverter, int], StateType], number: int) -> Callable[[SofarInverter], StateType]: ...

SENSOR_DESCRIPTIONS: tuple[SofarSensorDescription, ...]
