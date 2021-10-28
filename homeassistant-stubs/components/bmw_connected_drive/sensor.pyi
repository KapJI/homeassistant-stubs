from . import BMWConnectedDriveAccount as BMWConnectedDriveAccount, BMWConnectedDriveBaseEntity as BMWConnectedDriveBaseEntity
from .const import CONF_ACCOUNT as CONF_ACCOUNT, DATA_ENTRIES as DATA_ENTRIES
from bimmer_connected.vehicle import ConnectedDriveVehicle as ConnectedDriveVehicle
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_UNIT_SYSTEM_IMPERIAL as CONF_UNIT_SYSTEM_IMPERIAL, DEVICE_CLASS_TIMESTAMP as DEVICE_CLASS_TIMESTAMP, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, ENERGY_WATT_HOUR as ENERGY_WATT_HOUR, LENGTH_KILOMETERS as LENGTH_KILOMETERS, LENGTH_MILES as LENGTH_MILES, MASS_KILOGRAMS as MASS_KILOGRAMS, PERCENTAGE as PERCENTAGE, TIME_HOURS as TIME_HOURS, TIME_MINUTES as TIME_MINUTES, VOLUME_GALLONS as VOLUME_GALLONS, VOLUME_LITERS as VOLUME_LITERS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.icon import icon_for_battery_level as icon_for_battery_level
from homeassistant.util.unit_system import UnitSystem as UnitSystem
from typing import Any

_LOGGER: Any

class BMWSensorEntityDescription(SensorEntityDescription):
    unit_metric: Union[str, None]
    unit_imperial: Union[str, None]

SENSOR_TYPES: dict[str, BMWSensorEntityDescription]
DEFAULT_BMW_DESCRIPTION: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWConnectedDriveSensor(BMWConnectedDriveBaseEntity, SensorEntity):
    entity_description: BMWSensorEntityDescription
    _service: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_native_unit_of_measurement: Any
    def __init__(self, account: BMWConnectedDriveAccount, vehicle: ConnectedDriveVehicle, description: BMWSensorEntityDescription, unit_system: UnitSystem, service: Union[str, None] = ...) -> None: ...
    _attr_native_value: Any
    _attr_icon: Any
    def update(self) -> None: ...
