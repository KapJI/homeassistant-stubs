from . import BMWConnectedDriveBaseEntity as BMWConnectedDriveBaseEntity
from .const import DOMAIN as DOMAIN, UNIT_MAP as UNIT_MAP
from .coordinator import BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from _typeshed import Incomplete
from bimmer_connected.vehicle import ConnectedDriveVehicle as ConnectedDriveVehicle
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_UNIT_SYSTEM_IMPERIAL as CONF_UNIT_SYSTEM_IMPERIAL, LENGTH_KILOMETERS as LENGTH_KILOMETERS, LENGTH_MILES as LENGTH_MILES, PERCENTAGE as PERCENTAGE, VOLUME_GALLONS as VOLUME_GALLONS, VOLUME_LITERS as VOLUME_LITERS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.unit_system import UnitSystem as UnitSystem

_LOGGER: Incomplete

class BMWSensorEntityDescription(SensorEntityDescription):
    unit_metric: Union[str, None]
    unit_imperial: Union[str, None]
    value: Callable
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, unit_metric, unit_imperial, value) -> None: ...

def convert_and_round(state: tuple, converter: Callable[[Union[float, None], str], float], precision: int) -> Union[float, None]: ...

SENSOR_TYPES: dict[str, BMWSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWConnectedDriveSensor(BMWConnectedDriveBaseEntity, SensorEntity):
    entity_description: BMWSensorEntityDescription
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: BMWDataUpdateCoordinator, vehicle: ConnectedDriveVehicle, description: BMWSensorEntityDescription, unit_system: UnitSystem) -> None: ...
    _attr_native_value: Incomplete
    def _handle_coordinator_update(self) -> None: ...
