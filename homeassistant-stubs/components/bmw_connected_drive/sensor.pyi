from . import BMWConnectedDriveAccount as BMWConnectedDriveAccount, BMWConnectedDriveBaseEntity as BMWConnectedDriveBaseEntity
from .const import CONF_ACCOUNT as CONF_ACCOUNT, DATA_ENTRIES as DATA_ENTRIES, UNIT_MAP as UNIT_MAP
from bimmer_connected.vehicle import ConnectedDriveVehicle as ConnectedDriveVehicle
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_UNIT_SYSTEM_IMPERIAL as CONF_UNIT_SYSTEM_IMPERIAL, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, LENGTH_KILOMETERS as LENGTH_KILOMETERS, LENGTH_MILES as LENGTH_MILES, PERCENTAGE as PERCENTAGE, TIME_HOURS as TIME_HOURS, VOLUME_GALLONS as VOLUME_GALLONS, VOLUME_LITERS as VOLUME_LITERS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.unit_system import UnitSystem as UnitSystem
from typing import Any

_LOGGER: Any

class BMWSensorEntityDescription(SensorEntityDescription):
    unit_metric: Union[str, None]
    unit_imperial: Union[str, None]
    value: Callable

SENSOR_TYPES: dict[str, BMWSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWConnectedDriveSensor(BMWConnectedDriveBaseEntity, SensorEntity):
    entity_description: BMWSensorEntityDescription
    _attr_name: Any
    _attr_unique_id: Any
    _attr_native_unit_of_measurement: Any
    def __init__(self, account: BMWConnectedDriveAccount, vehicle: ConnectedDriveVehicle, description: BMWSensorEntityDescription, unit_system: UnitSystem) -> None: ...
    @property
    def native_value(self) -> StateType: ...
