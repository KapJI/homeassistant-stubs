from .const import CONF_URL_ENERGY as CONF_URL_ENERGY, CONF_URL_PUBLIC_WEATHER as CONF_URL_PUBLIC_WEATHER, CONF_URL_WEATHER as CONF_URL_WEATHER, CONF_WEATHER_AREAS as CONF_WEATHER_AREAS, DATA_HANDLER as DATA_HANDLER, DOMAIN as DOMAIN, NETATMO_CREATE_BATTERY as NETATMO_CREATE_BATTERY, NETATMO_CREATE_ROOM_SENSOR as NETATMO_CREATE_ROOM_SENSOR, NETATMO_CREATE_SENSOR as NETATMO_CREATE_SENSOR, NETATMO_CREATE_WEATHER_SENSOR as NETATMO_CREATE_WEATHER_SENSOR, SIGNAL_NAME as SIGNAL_NAME
from .data_handler import HOME as HOME, NetatmoDataHandler as NetatmoDataHandler, NetatmoDevice as NetatmoDevice, NetatmoRoom as NetatmoRoom, PUBLIC as PUBLIC
from .helper import NetatmoArea as NetatmoArea
from .netatmo_entity_base import NetatmoBase as NetatmoBase
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, DEGREE as DEGREE, PERCENTAGE as PERCENTAGE, UnitOfPower as UnitOfPower, UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfPressure as UnitOfPressure, UnitOfSoundPressure as UnitOfSoundPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import async_entries_for_config_entry as async_entries_for_config_entry
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete
SUPPORTED_PUBLIC_SENSOR_TYPES: tuple[str, ...]

class NetatmoRequiredKeysMixin:
    netatmo_name: str
    def __init__(self, netatmo_name) -> None: ...

class NetatmoSensorEntityDescription(SensorEntityDescription, NetatmoRequiredKeysMixin):
    def __init__(self, netatmo_name, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_precision, native_unit_of_measurement, options, state_class, suggested_unit_of_measurement) -> None: ...

SENSOR_TYPES: tuple[NetatmoSensorEntityDescription, ...]
SENSOR_TYPES_KEYS: Incomplete
BATTERY_SENSOR_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NetatmoWeatherSensor(NetatmoBase, SensorEntity):
    _attr_has_entity_name: bool
    entity_description: NetatmoSensorEntityDescription
    _module: Incomplete
    _id: Incomplete
    _station_id: Incomplete
    _device_name: Incomplete
    _attr_name: Incomplete
    _model: Incomplete
    _config_url: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice, description: NetatmoSensorEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    _attr_native_value: Incomplete
    def async_update_callback(self) -> None: ...

class NetatmoClimateBatterySensor(NetatmoBase, SensorEntity):
    entity_description: NetatmoSensorEntityDescription
    _module: Incomplete
    _id: Incomplete
    _attr_name: Incomplete
    _room_id: Incomplete
    _model: Incomplete
    _config_url: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice) -> None: ...
    _attr_available: bool
    _attr_native_value: Incomplete
    def async_update_callback(self) -> None: ...

class NetatmoSensor(NetatmoBase, SensorEntity):
    entity_description: NetatmoSensorEntityDescription
    _module: Incomplete
    _id: Incomplete
    _attr_name: Incomplete
    _room_id: Incomplete
    _model: Incomplete
    _config_url: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice, description: NetatmoSensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    def async_update_callback(self) -> None: ...

def process_health(health: int) -> str: ...
def process_rf(strength: int) -> str: ...
def process_wifi(strength: int) -> str: ...

class NetatmoRoomSensor(NetatmoBase, SensorEntity):
    entity_description: NetatmoSensorEntityDescription
    _room: Incomplete
    _id: Incomplete
    _attr_name: Incomplete
    _room_id: Incomplete
    _model: Incomplete
    _config_url: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, netatmo_room: NetatmoRoom, description: NetatmoSensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    def async_update_callback(self) -> None: ...

class NetatmoPublicSensor(NetatmoBase, SensorEntity):
    _attr_has_entity_name: bool
    entity_description: NetatmoSensorEntityDescription
    _signal_name: Incomplete
    _station: Incomplete
    area: Incomplete
    _mode: Incomplete
    _area_name: Incomplete
    _id: Incomplete
    _device_name: Incomplete
    _attr_name: Incomplete
    _show_on_map: Incomplete
    _config_url: Incomplete
    _attr_unique_id: Incomplete
    _model: Incomplete
    def __init__(self, data_handler: NetatmoDataHandler, area: NetatmoArea, description: NetatmoSensorEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_config_update_callback(self, area: NetatmoArea) -> None: ...
    _attr_native_value: Incomplete
    _attr_available: bool
    def async_update_callback(self) -> None: ...
