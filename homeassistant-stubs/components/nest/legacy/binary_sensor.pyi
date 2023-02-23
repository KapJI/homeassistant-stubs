from . import NestSensorDevice as NestSensorDevice
from .const import DATA_NEST as DATA_NEST, DATA_NEST_CONFIG as DATA_NEST_CONFIG
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_BINARY_SENSORS as CONF_BINARY_SENSORS, CONF_MONITORED_CONDITIONS as CONF_MONITORED_CONDITIONS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete
BINARY_TYPES: Incomplete
CLIMATE_BINARY_TYPES: Incomplete
CAMERA_BINARY_TYPES: Incomplete
STRUCTURE_BINARY_TYPES: Incomplete
STRUCTURE_BINARY_STATE_MAP: Incomplete
_BINARY_TYPES_DEPRECATED: Incomplete
_VALID_BINARY_SENSOR_TYPES: Incomplete

async def async_setup_legacy_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NestBinarySensor(NestSensorDevice, BinarySensorEntity):
    @property
    def is_on(self): ...
    @property
    def device_class(self): ...
    _state: Incomplete
    def update(self) -> None: ...

class NestActivityZoneSensor(NestBinarySensor):
    zone: Incomplete
    _name: Incomplete
    def __init__(self, structure, device, zone) -> None: ...
    @property
    def unique_id(self): ...
    @property
    def device_class(self): ...
    _state: Incomplete
    def update(self) -> None: ...
