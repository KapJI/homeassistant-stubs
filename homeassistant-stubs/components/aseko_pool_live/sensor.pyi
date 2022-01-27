from . import AsekoDataUpdateCoordinator as AsekoDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from .entity import AsekoEntity as AsekoEntity
from aioaseko import Unit as Unit, Variable as Variable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class VariableSensorEntity(AsekoEntity, SensorEntity):
    attr_state_class: Any
    _variable: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_native_unit_of_measurement: Any
    _attr_icon: Any
    _attr_device_class: Any
    def __init__(self, unit: Unit, variable: Variable, coordinator: AsekoDataUpdateCoordinator) -> None: ...
    @property
    def native_value(self) -> Union[int, None]: ...
