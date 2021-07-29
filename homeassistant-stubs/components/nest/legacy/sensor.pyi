from . import NestSensorDevice as NestSensorDevice
from .const import DATA_NEST as DATA_NEST, DATA_NEST_CONFIG as DATA_NEST_CONFIG
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.const import CONF_MONITORED_CONDITIONS as CONF_MONITORED_CONDITIONS, CONF_SENSORS as CONF_SENSORS, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, PERCENTAGE as PERCENTAGE, STATE_OFF as STATE_OFF, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from typing import Any

SENSOR_TYPES: Any
TEMP_SENSOR_TYPES: Any
PROTECT_SENSOR_TYPES: Any
STRUCTURE_SENSOR_TYPES: Any
STATE_HEAT: str
STATE_COOL: str
STRUCTURE_CAMERA_SENSOR_TYPES: Any
_VALID_SENSOR_TYPES: Any
SENSOR_UNITS: Any
SENSOR_DEVICE_CLASSES: Any
VARIABLE_NAME_MAPPING: Any
VALUE_MAPPING: Any
SENSOR_TYPES_DEPRECATED: Any
DEPRECATED_WEATHER_VARS: Any
_SENSOR_TYPES_DEPRECATED: Any
_LOGGER: Any

def setup_platform(hass, config, add_entities, discovery_info: Any | None = ...) -> None: ...
async def async_setup_legacy_entry(hass, entry, async_add_entities) -> None: ...

class NestBasicSensor(NestSensorDevice, SensorEntity):
    @property
    def unit_of_measurement(self): ...
    @property
    def state(self): ...
    @property
    def device_class(self): ...
    _unit: Any
    _state: Any
    def update(self) -> None: ...

class NestTempSensor(NestSensorDevice, SensorEntity):
    @property
    def state(self): ...
    @property
    def unit_of_measurement(self): ...
    @property
    def device_class(self): ...
    _unit: Any
    _state: Any
    def update(self) -> None: ...
