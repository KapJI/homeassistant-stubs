from . import AirVisualEntity as AirVisualEntity
from .const import CONF_CITY as CONF_CITY, CONF_COUNTRY as CONF_COUNTRY, CONF_INTEGRATION_TYPE as CONF_INTEGRATION_TYPE, DOMAIN as DOMAIN, INTEGRATION_TYPE_GEOGRAPHY_COORDS as INTEGRATION_TYPE_GEOGRAPHY_COORDS, INTEGRATION_TYPE_GEOGRAPHY_NAME as INTEGRATION_TYPE_GEOGRAPHY_NAME
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, ATTR_STATE as ATTR_STATE, CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_BILLION as CONCENTRATION_PARTS_PER_BILLION, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_SHOW_ON_MAP as CONF_SHOW_ON_MAP, CONF_STATE as CONF_STATE, PERCENTAGE as PERCENTAGE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

ATTR_CITY: str
ATTR_COUNTRY: str
ATTR_POLLUTANT_SYMBOL: str
ATTR_POLLUTANT_UNIT: str
ATTR_REGION: str
DEVICE_CLASS_POLLUTANT_LABEL: str
DEVICE_CLASS_POLLUTANT_LEVEL: str
SENSOR_KIND_AQI: str
SENSOR_KIND_BATTERY_LEVEL: str
SENSOR_KIND_CO2: str
SENSOR_KIND_HUMIDITY: str
SENSOR_KIND_LEVEL: str
SENSOR_KIND_PM_0_1: str
SENSOR_KIND_PM_1_0: str
SENSOR_KIND_PM_2_5: str
SENSOR_KIND_POLLUTANT: str
SENSOR_KIND_SENSOR_LIFE: str
SENSOR_KIND_TEMPERATURE: str
SENSOR_KIND_VOC: str
GEOGRAPHY_SENSOR_DESCRIPTIONS: Incomplete
GEOGRAPHY_SENSOR_LOCALES: Incomplete
NODE_PRO_SENSOR_DESCRIPTIONS: Incomplete
STATE_POLLUTANT_LABEL_CO: str
STATE_POLLUTANT_LABEL_N2: str
STATE_POLLUTANT_LABEL_O3: str
STATE_POLLUTANT_LABEL_P1: str
STATE_POLLUTANT_LABEL_P2: str
STATE_POLLUTANT_LABEL_S2: str
STATE_POLLUTANT_LEVEL_GOOD: str
STATE_POLLUTANT_LEVEL_MODERATE: str
STATE_POLLUTANT_LEVEL_UNHEALTHY_SENSITIVE: str
STATE_POLLUTANT_LEVEL_UNHEALTHY: str
STATE_POLLUTANT_LEVEL_VERY_UNHEALTHY: str
STATE_POLLUTANT_LEVEL_HAZARDOUS: str
POLLUTANT_LEVELS: Incomplete
POLLUTANT_UNITS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirVisualGeographySensor(AirVisualEntity, SensorEntity):
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _locale: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, entry: ConfigEntry, description: SensorEntityDescription, locale: str) -> None: ...
    @property
    def available(self) -> bool: ...
    _attr_native_value: Incomplete
    def update_from_latest_data(self) -> None: ...

class AirVisualNodeProSensor(AirVisualEntity, SensorEntity):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, entry: ConfigEntry, description: SensorEntityDescription) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    _attr_native_value: Incomplete
    def update_from_latest_data(self) -> None: ...
