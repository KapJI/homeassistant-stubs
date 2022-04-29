from . import BMWConnectedDriveBaseEntity as BMWConnectedDriveBaseEntity
from .const import DOMAIN as DOMAIN, UNIT_MAP as UNIT_MAP
from .coordinator import BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from _typeshed import Incomplete
from bimmer_connected.vehicle import ConnectedDriveVehicle as ConnectedDriveVehicle
from bimmer_connected.vehicle_status import ConditionBasedServiceReport as ConditionBasedServiceReport, VehicleStatus as VehicleStatus
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.unit_system import UnitSystem as UnitSystem
from typing import Any

_LOGGER: Incomplete

def _condition_based_services(vehicle_state: VehicleStatus, unit_system: UnitSystem) -> dict[str, Any]: ...
def _check_control_messages(vehicle_state: VehicleStatus) -> dict[str, Any]: ...
def _format_cbs_report(report: ConditionBasedServiceReport, unit_system: UnitSystem) -> dict[str, Any]: ...

class BMWRequiredKeysMixin:
    value_fn: Callable[[VehicleStatus], bool]
    def __init__(self, value_fn) -> None: ...

class BMWBinarySensorEntityDescription(BinarySensorEntityDescription, BMWRequiredKeysMixin):
    attr_fn: Union[Callable[[VehicleStatus, UnitSystem], dict[str, Any]], None]
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, name, unit_of_measurement, attr_fn) -> None: ...

SENSOR_TYPES: tuple[BMWBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWConnectedDriveSensor(BMWConnectedDriveBaseEntity, BinarySensorEntity):
    entity_description: BMWBinarySensorEntityDescription
    _unit_system: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: BMWDataUpdateCoordinator, vehicle: ConnectedDriveVehicle, description: BMWBinarySensorEntityDescription, unit_system: UnitSystem) -> None: ...
    _attr_is_on: Incomplete
    _attr_extra_state_attributes: Incomplete
    def _handle_coordinator_update(self) -> None: ...
