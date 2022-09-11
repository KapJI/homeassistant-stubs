from . import NAMDataUpdateCoordinator as NAMDataUpdateCoordinator
from .const import ATTR_BME280_HUMIDITY as ATTR_BME280_HUMIDITY, ATTR_BME280_PRESSURE as ATTR_BME280_PRESSURE, ATTR_BME280_TEMPERATURE as ATTR_BME280_TEMPERATURE, ATTR_BMP180_PRESSURE as ATTR_BMP180_PRESSURE, ATTR_BMP180_TEMPERATURE as ATTR_BMP180_TEMPERATURE, ATTR_BMP280_PRESSURE as ATTR_BMP280_PRESSURE, ATTR_BMP280_TEMPERATURE as ATTR_BMP280_TEMPERATURE, ATTR_DHT22_HUMIDITY as ATTR_DHT22_HUMIDITY, ATTR_DHT22_TEMPERATURE as ATTR_DHT22_TEMPERATURE, ATTR_HECA_HUMIDITY as ATTR_HECA_HUMIDITY, ATTR_HECA_TEMPERATURE as ATTR_HECA_TEMPERATURE, ATTR_MHZ14A_CARBON_DIOXIDE as ATTR_MHZ14A_CARBON_DIOXIDE, ATTR_SDS011_CAQI as ATTR_SDS011_CAQI, ATTR_SDS011_CAQI_LEVEL as ATTR_SDS011_CAQI_LEVEL, ATTR_SDS011_P1 as ATTR_SDS011_P1, ATTR_SDS011_P2 as ATTR_SDS011_P2, ATTR_SHT3X_HUMIDITY as ATTR_SHT3X_HUMIDITY, ATTR_SHT3X_TEMPERATURE as ATTR_SHT3X_TEMPERATURE, ATTR_SIGNAL_STRENGTH as ATTR_SIGNAL_STRENGTH, ATTR_SPS30_CAQI as ATTR_SPS30_CAQI, ATTR_SPS30_CAQI_LEVEL as ATTR_SPS30_CAQI_LEVEL, ATTR_SPS30_P0 as ATTR_SPS30_P0, ATTR_SPS30_P1 as ATTR_SPS30_P1, ATTR_SPS30_P2 as ATTR_SPS30_P2, ATTR_SPS30_P4 as ATTR_SPS30_P4, ATTR_UPTIME as ATTR_UPTIME, DOMAIN as DOMAIN, MIGRATION_SENSORS as MIGRATION_SENSORS
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, PERCENTAGE as PERCENTAGE, PRESSURE_HPA as PRESSURE_HPA, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util.dt import utcnow as utcnow

PARALLEL_UPDATES: int
_LOGGER: Incomplete
SENSORS: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NAMSensor(CoordinatorEntity[NAMDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: NAMDataUpdateCoordinator, description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[StateType, datetime]: ...
    @property
    def available(self) -> bool: ...

class NAMSensorUptime(NAMSensor):
    @property
    def native_value(self) -> datetime: ...
