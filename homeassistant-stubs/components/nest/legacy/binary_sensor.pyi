from . import NestSensorDevice as NestSensorDevice
from .const import DATA_NEST as DATA_NEST, DATA_NEST_CONFIG as DATA_NEST_CONFIG
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, DEVICE_CLASS_CONNECTIVITY as DEVICE_CLASS_CONNECTIVITY, DEVICE_CLASS_MOTION as DEVICE_CLASS_MOTION, DEVICE_CLASS_OCCUPANCY as DEVICE_CLASS_OCCUPANCY, DEVICE_CLASS_SOUND as DEVICE_CLASS_SOUND
from homeassistant.const import CONF_BINARY_SENSORS as CONF_BINARY_SENSORS, CONF_MONITORED_CONDITIONS as CONF_MONITORED_CONDITIONS
from typing import Any

_LOGGER: Any
BINARY_TYPES: Any
CLIMATE_BINARY_TYPES: Any
CAMERA_BINARY_TYPES: Any
STRUCTURE_BINARY_TYPES: Any
STRUCTURE_BINARY_STATE_MAP: Any
_BINARY_TYPES_DEPRECATED: Any
_VALID_BINARY_SENSOR_TYPES: Any

def setup_platform(hass, config, add_entities, discovery_info: Any | None = ...) -> None: ...
async def async_setup_legacy_entry(hass, entry, async_add_entities) -> None: ...

class NestBinarySensor(NestSensorDevice, BinarySensorEntity):
    @property
    def is_on(self): ...
    @property
    def device_class(self): ...
    _state: Any
    def update(self) -> None: ...

class NestActivityZoneSensor(NestBinarySensor):
    zone: Any
    _name: Any
    def __init__(self, structure, device, zone) -> None: ...
    @property
    def unique_id(self): ...
    @property
    def device_class(self): ...
    _state: Any
    def update(self) -> None: ...
