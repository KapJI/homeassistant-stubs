from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_BILLION as CONCENTRATION_PARTS_PER_BILLION, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, UnitOfSoundPressure as UnitOfSoundPressure, UnitOfTemperature as UnitOfTemperature
from python_awair.air_data import AirData as AirData
from python_awair.devices import AwairBaseDevice as AwairBaseDevice

API_CO2: str
API_DUST: str
API_HUMID: str
API_LUX: str
API_PM10: str
API_PM25: str
API_SCORE: str
API_SPL_A: str
API_TEMP: str
API_TIMEOUT: int
API_VOC: str
ATTRIBUTION: str
DOMAIN: str
DUST_ALIASES: Incomplete
LOGGER: Incomplete
UPDATE_INTERVAL_CLOUD: Incomplete
UPDATE_INTERVAL_LOCAL: Incomplete

class AwairRequiredKeysMixin:
    unique_id_tag: str
    def __init__(self, unique_id_tag) -> None: ...

class AwairSensorEntityDescription(SensorEntityDescription, AwairRequiredKeysMixin):
    def __init__(self, unique_id_tag, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_precision, native_unit_of_measurement, options, state_class, suggested_unit_of_measurement) -> None: ...

SENSOR_TYPE_SCORE: Incomplete
SENSOR_TYPES: tuple[AwairSensorEntityDescription, ...]
SENSOR_TYPES_DUST: tuple[AwairSensorEntityDescription, ...]

class AwairResult:
    device: AwairBaseDevice
    air_data: AirData
    def __init__(self, device, air_data) -> None: ...
