from .const import ATTRIBUTION as ATTRIBUTION, ATTR_ACTIVE as ATTR_ACTIVE, ATTR_MEASURE_TIME as ATTR_MEASURE_TIME, CONF_STATION as CONF_STATION, DOMAIN as DOMAIN, NONE_IS_ZERO_SENSORS as NONE_IS_ZERO_SENSORS
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_MONITORED_CONDITIONS as CONF_MONITORED_CONDITIONS, CONF_NAME as CONF_NAME, DEGREE as DEGREE, LENGTH_MILLIMETERS as LENGTH_MILLIMETERS, PERCENTAGE as PERCENTAGE, SPEED_METERS_PER_SECOND as SPEED_METERS_PER_SECOND, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util import Throttle as Throttle
from pytrafikverket.trafikverket_weather import TrafikverketWeather, WeatherStationInfo as WeatherStationInfo
from typing import Any

_LOGGER: Any
MIN_TIME_BETWEEN_UPDATES: Any
SCAN_INTERVAL: Any

class TrafikverketRequiredKeysMixin:
    api_key: str
    def __init__(self, api_key) -> None: ...

class TrafikverketSensorEntityDescription(SensorEntityDescription, TrafikverketRequiredKeysMixin):
    def __init__(self, api_key, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

SENSOR_TYPES: tuple[TrafikverketSensorEntityDescription, ...]
SENSOR_KEYS: Any
PLATFORM_SCHEMA: Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TrafikverketWeatherStation(SensorEntity):
    entity_description: TrafikverketSensorEntityDescription
    _attr_attribution: Any
    _attr_name: Any
    _attr_unique_id: Any
    _station: Any
    _weather_api: Any
    _attr_device_info: Any
    _weather: Any
    def __init__(self, weather_api: TrafikverketWeather, entry_id: str, sensor_station: str, description: TrafikverketSensorEntityDescription) -> None: ...
    _attr_native_value: Any
    _attr_extra_state_attributes: Any
    async def async_update(self) -> None: ...
