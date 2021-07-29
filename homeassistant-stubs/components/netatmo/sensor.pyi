import pyatmo
from .const import CONF_WEATHER_AREAS as CONF_WEATHER_AREAS, DATA_HANDLER as DATA_HANDLER, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, SIGNAL_NAME as SIGNAL_NAME
from .data_handler import HOMECOACH_DATA_CLASS_NAME as HOMECOACH_DATA_CLASS_NAME, NetatmoDataHandler as NetatmoDataHandler, PUBLICDATA_DATA_CLASS_NAME as PUBLICDATA_DATA_CLASS_NAME, WEATHERSTATION_DATA_CLASS_NAME as WEATHERSTATION_DATA_CLASS_NAME
from .helper import NetatmoArea as NetatmoArea
from .netatmo_entity_base import NetatmoBase as NetatmoBase
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, DEGREE as DEGREE, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_CO2 as DEVICE_CLASS_CO2, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_PRESSURE as DEVICE_CLASS_PRESSURE, DEVICE_CLASS_SIGNAL_STRENGTH as DEVICE_CLASS_SIGNAL_STRENGTH, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, LENGTH_MILLIMETERS as LENGTH_MILLIMETERS, PERCENTAGE as PERCENTAGE, PRESSURE_MBAR as PRESSURE_MBAR, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, SOUND_PRESSURE_DB as SOUND_PRESSURE_DB, SPEED_KILOMETERS_PER_HOUR as SPEED_KILOMETERS_PER_HOUR, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.device_registry import async_entries_for_config_entry as async_entries_for_config_entry
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, NamedTuple

_LOGGER: Any
SUPPORTED_PUBLIC_SENSOR_TYPES: tuple[str, ...]

class NetatmoRequiredKeysMixin:
    netatmo_name: str

class NetatmoSensorEntityDescription(SensorEntityDescription, NetatmoRequiredKeysMixin): ...

SENSOR_TYPES: tuple[NetatmoSensorEntityDescription, ...]
SENSOR_TYPES_KEYS: Any
MODULE_TYPE_OUTDOOR: str
MODULE_TYPE_WIND: str
MODULE_TYPE_RAIN: str
MODULE_TYPE_INDOOR: str

class BatteryData(NamedTuple):
    full: int
    high: int
    medium: int
    low: int

BATTERY_VALUES: Any
PUBLIC: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NetatmoSensor(NetatmoBase, SensorEntity):
    entity_description: NetatmoSensorEntityDescription
    _id: Any
    _station_id: Any
    _device_name: Any
    _attr_name: Any
    _model: Any
    _attr_unique_id: Any
    def __init__(self, data_handler: NetatmoDataHandler, data_class_name: str, module_info: dict, description: NetatmoSensorEntityDescription) -> None: ...
    @property
    def _data(self) -> pyatmo.AsyncWeatherStationData: ...
    @property
    def available(self) -> bool: ...
    _attr_state: Any
    def async_update_callback(self) -> None: ...

def fix_angle(angle: int) -> int: ...
def process_angle(angle: int) -> str: ...
def process_battery(data: int, model: str) -> str: ...
def process_health(health: int) -> str: ...
def process_rf(strength: int) -> str: ...
def process_wifi(strength: int) -> str: ...

class NetatmoPublicSensor(NetatmoBase, SensorEntity):
    entity_description: NetatmoSensorEntityDescription
    _signal_name: Any
    area: Any
    _mode: Any
    _area_name: Any
    _id: Any
    _device_name: Any
    _attr_name: Any
    _show_on_map: Any
    _attr_unique_id: Any
    _model: Any
    def __init__(self, data_handler: NetatmoDataHandler, area: NetatmoArea, description: NetatmoSensorEntityDescription) -> None: ...
    @property
    def _data(self) -> pyatmo.AsyncPublicData: ...
    async def async_added_to_hass(self) -> None: ...
    _data_classes: Any
    async def async_config_update_callback(self, area: NetatmoArea) -> None: ...
    _attr_state: Any
    _attr_available: Any
    def async_update_callback(self) -> None: ...
