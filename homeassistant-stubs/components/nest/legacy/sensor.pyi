from . import NestSensorDevice as NestSensorDevice
from .const import DATA_NEST as DATA_NEST, DATA_NEST_CONFIG as DATA_NEST_CONFIG
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.const import CONF_MONITORED_CONDITIONS as CONF_MONITORED_CONDITIONS, CONF_SENSORS as CONF_SENSORS, PERCENTAGE as PERCENTAGE, STATE_OFF as STATE_OFF, UnitOfTemperature as UnitOfTemperature

SENSOR_TYPES: Incomplete
TEMP_SENSOR_TYPES: Incomplete
PROTECT_SENSOR_TYPES: Incomplete
STRUCTURE_SENSOR_TYPES: Incomplete
STATE_HEAT: str
STATE_COOL: str
STRUCTURE_CAMERA_SENSOR_TYPES: Incomplete
_VALID_SENSOR_TYPES: Incomplete
SENSOR_UNITS: Incomplete
SENSOR_DEVICE_CLASSES: Incomplete
VARIABLE_NAME_MAPPING: Incomplete
VALUE_MAPPING: Incomplete
SENSOR_TYPES_DEPRECATED: Incomplete
DEPRECATED_WEATHER_VARS: Incomplete
_SENSOR_TYPES_DEPRECATED: Incomplete
_LOGGER: Incomplete

def setup_platform(hass, config, add_entities, discovery_info: Incomplete | None = ...) -> None: ...
async def async_setup_legacy_entry(hass, entry, async_add_entities) -> None: ...

class NestBasicSensor(NestSensorDevice, SensorEntity):
    @property
    def native_unit_of_measurement(self): ...
    @property
    def native_value(self): ...
    @property
    def device_class(self): ...
    _unit: Incomplete
    _state: Incomplete
    def update(self) -> None: ...

class NestTempSensor(NestSensorDevice, SensorEntity):
    @property
    def native_value(self): ...
    @property
    def native_unit_of_measurement(self): ...
    @property
    def device_class(self): ...
    _unit: Incomplete
    _state: Incomplete
    def update(self) -> None: ...
