from . import SpecializedTurboConfigEntry as SpecializedTurboConfigEntry
from .coordinator import SpecializedTurboCoordinator as SpecializedTurboCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.bluetooth.passive_update_coordinator import PassiveBluetoothCoordinatorEntity as PassiveBluetoothCoordinatorEntity
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, REVOLUTIONS_PER_MINUTE as REVOLUTIONS_PER_MINUTE, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfEnergyDistance as UnitOfEnergyDistance, UnitOfLength as UnitOfLength, UnitOfPower as UnitOfPower, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import CONNECTION_BLUETOOTH as CONNECTION_BLUETOOTH, DeviceInfo as DeviceInfo, format_mac as format_mac
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from specialized_turbo import TelemetrySnapshot as TelemetrySnapshot
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class SpecializedSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[TelemetrySnapshot], StateType]

def _assist_level_name(snap: TelemetrySnapshot) -> str | None: ...

SENSOR_DESCRIPTIONS: tuple[SpecializedSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SpecializedTurboConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SpecializedTurboSensor(PassiveBluetoothCoordinatorEntity[SpecializedTurboCoordinator], SensorEntity):
    entity_description: SpecializedSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SpecializedTurboCoordinator, description: SpecializedSensorEntityDescription, entry: SpecializedTurboConfigEntry) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def native_value(self) -> StateType: ...
