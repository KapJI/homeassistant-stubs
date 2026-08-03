from . import GoogleHealthConfigEntry as GoogleHealthConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import GoogleHealthActivityCoordinator as GoogleHealthActivityCoordinator, GoogleHealthBodyCoordinator as GoogleHealthBodyCoordinator, GoogleHealthDataUpdateCoordinator as GoogleHealthDataUpdateCoordinator, GoogleHealthDeviceCoordinator as GoogleHealthDeviceCoordinator, GoogleHealthNutritionCoordinator as GoogleHealthNutritionCoordinator, GoogleHealthSleepCoordinator as GoogleHealthSleepCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from google_health_api.model import PairedDevice as PairedDevice
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfEnergy as UnitOfEnergy, UnitOfLength as UnitOfLength, UnitOfMass as UnitOfMass, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo, async_get_device_id_by_identifier as async_get_device_id_by_identifier
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util.unit_system import US_CUSTOMARY_SYSTEM as US_CUSTOMARY_SYSTEM, UnitSystem as UnitSystem
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class GoogleHealthSensorEntityDescription[_CoordinatorT: GoogleHealthDataUpdateCoordinator[Any], _ValueT: StateType](SensorEntityDescription):
    value_fn: Callable[[Any], _ValueT]
    suggested_unit_fn: Callable[[UnitSystem], str | None] | None = ...

ACTIVITY_SENSORS: list[GoogleHealthSensorEntityDescription[GoogleHealthActivityCoordinator, Any]]
BODY_SENSORS: list[GoogleHealthSensorEntityDescription[GoogleHealthBodyCoordinator, Any]]
SLEEP_SENSORS: list[GoogleHealthSensorEntityDescription[GoogleHealthSleepCoordinator, Any]]
NUTRITION_SENSORS: list[GoogleHealthSensorEntityDescription[GoogleHealthNutritionCoordinator, Any]]

@dataclass(frozen=True, kw_only=True)
class GoogleHealthDeviceSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[PairedDevice], datetime | StateType]

DEVICE_SENSORS: list[GoogleHealthDeviceSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: GoogleHealthConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class GoogleHealthSensor[_CoordinatorT: GoogleHealthDataUpdateCoordinator[Any]](CoordinatorEntity[_CoordinatorT], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: GoogleHealthSensorEntityDescription[_CoordinatorT, Any]
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: _CoordinatorT, entry_id: str, description: GoogleHealthSensorEntityDescription[_CoordinatorT, Any]) -> None: ...
    @property
    @override
    def native_value(self) -> StateType: ...
    @property
    @override
    def suggested_unit_of_measurement(self) -> str | None: ...

class GoogleHealthDeviceSensor(CoordinatorEntity[GoogleHealthDeviceCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    _attr_entity_category: Incomplete
    entity_description: GoogleHealthDeviceSensorEntityDescription
    device_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: GoogleHealthDeviceCoordinator, entry_id: str, device: PairedDevice, description: GoogleHealthDeviceSensorEntityDescription) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def native_value(self) -> datetime | StateType: ...
