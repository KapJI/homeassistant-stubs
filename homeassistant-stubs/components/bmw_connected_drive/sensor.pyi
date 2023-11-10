from . import BMWBaseEntity as BMWBaseEntity
from .const import DOMAIN as DOMAIN, UNIT_MAP as UNIT_MAP
from .coordinator import BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from _typeshed import Incomplete
from bimmer_connected.models import ValueWithUnit as ValueWithUnit
from bimmer_connected.vehicle import MyBMWVehicle as MyBMWVehicle
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import LENGTH as LENGTH, PERCENTAGE as PERCENTAGE, UnitOfElectricCurrent as UnitOfElectricCurrent, VOLUME as VOLUME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

_LOGGER: Incomplete

@dataclass
class BMWSensorEntityDescription(SensorEntityDescription):
    key_class: str | None = ...
    unit_type: str | None = ...
    value: Callable = ...
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, key_class, unit_type, value) -> None: ...

def convert_and_round(state: ValueWithUnit, converter: Callable[[float | None, str], float], precision: int) -> float | None: ...

SENSOR_TYPES: dict[str, BMWSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWSensor(BMWBaseEntity, SensorEntity):
    entity_description: BMWSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: BMWDataUpdateCoordinator, vehicle: MyBMWVehicle, description: BMWSensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    def _handle_coordinator_update(self) -> None: ...
