import pyatmo
from .const import CONF_URL_CONTROL as CONF_URL_CONTROL, CONF_URL_ENERGY as CONF_URL_ENERGY, CONF_URL_PUBLIC_WEATHER as CONF_URL_PUBLIC_WEATHER, CONF_URL_SECURITY as CONF_URL_SECURITY, CONF_WEATHER_AREAS as CONF_WEATHER_AREAS, DOMAIN as DOMAIN, NETATMO_CREATE_CLIMATE_BATTERY_SENSOR as NETATMO_CREATE_CLIMATE_BATTERY_SENSOR, NETATMO_CREATE_LEGACY_SENSOR as NETATMO_CREATE_LEGACY_SENSOR, NETATMO_CREATE_ROOM_SENSOR as NETATMO_CREATE_ROOM_SENSOR, NETATMO_CREATE_SENSOR as NETATMO_CREATE_SENSOR, NETATMO_CREATE_WEATHER_SENSOR as NETATMO_CREATE_WEATHER_SENSOR, SIGNAL_NAME as SIGNAL_NAME
from .data_handler import HOME as HOME, NetatmoConfigEntry as NetatmoConfigEntry, NetatmoDataHandler as NetatmoDataHandler, NetatmoDevice as NetatmoDevice, NetatmoRoom as NetatmoRoom, PUBLIC as PUBLIC
from .entity import NetatmoBaseEntity as NetatmoBaseEntity, NetatmoModuleEntity as NetatmoModuleEntity, NetatmoRoomEntity as NetatmoRoomEntity, NetatmoWeatherModuleEntity as NetatmoWeatherModuleEntity
from .helper import NetatmoArea as NetatmoArea
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, DEGREE as DEGREE, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfPower as UnitOfPower, UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfPressure as UnitOfPressure, UnitOfSoundPressure as UnitOfSoundPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pyatmo.modules import PublicWeatherArea as PublicWeatherArea
from pyatmo.modules.device_types import DeviceCategory as NetatmoDeviceCategory
from typing import Any, Final

_LOGGER: Incomplete
DIRECTION_OPTIONS: Incomplete

def process_health(health: StateType) -> str | None: ...
def process_rf(strength: StateType) -> str | None: ...
def process_wifi(strength: StateType) -> str | None: ...

@dataclass(frozen=True, kw_only=True)
class NetatmoSensorEntityDescription(SensorEntityDescription):
    netatmo_name: str | None = ...
    is_sticky: bool | None = ...
    value_fn: Callable[[StateType], StateType] = ...

NETATMO_WEATHER_SENSOR_DESCRIPTIONS: Final[list[NetatmoSensorEntityDescription]]

@dataclass(frozen=True, kw_only=True)
class NetatmoPublicWeatherSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[PublicWeatherArea], dict[str, Any]]

PUBLIC_WEATHER_STATION_TYPES: tuple[NetatmoPublicWeatherSensorEntityDescription, ...]
NETATMO_CLIMATE_BATTERY_SENSOR_DESCRIPTIONS: Final[list[NetatmoSensorEntityDescription]]
NETATMO_OPENING_SENSOR_DESCRIPTIONS: Final[list[NetatmoSensorEntityDescription]]
DEVICE_CATEGORY_CLIMATE_BATTERY_SENSORS: Final[dict[NetatmoDeviceCategory, list[NetatmoSensorEntityDescription]]]
DEVICE_CATEGORY_NEW_SENSORS: Final[dict[NetatmoDeviceCategory, list[NetatmoSensorEntityDescription]]]
DEVICE_CATEGORY_WEATHER_SENSORS: Final[dict[NetatmoDeviceCategory, list[NetatmoSensorEntityDescription]]]
DEVICE_CATEGORY_LEGACY_SENSORS: Final[dict[NetatmoDeviceCategory, list[NetatmoSensorEntityDescription]]]
DEVICE_CATEGORY_SENSOR_URLS: Final[dict[NetatmoDeviceCategory, str]]

async def async_setup_entry(hass: HomeAssistant, entry: NetatmoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NetatmoBaseSensor(NetatmoModuleEntity, SensorEntity):
    entity_description: NetatmoSensorEntityDescription
    _attr_configuration_url: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice, description: NetatmoSensorEntityDescription, **kwargs: Any) -> None: ...
    _attr_available: bool
    _attr_native_value: Incomplete
    @callback
    def async_update_callback(self) -> None: ...

class NetatmoWeatherSensor(NetatmoWeatherModuleEntity, NetatmoBaseSensor):
    entity_description: NetatmoSensorEntityDescription
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice, description: NetatmoSensorEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    _attr_native_value: Incomplete
    @callback
    def async_update_callback(self) -> None: ...

class NetatmoLegacySensor(NetatmoBaseSensor):
    entity_description: NetatmoSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice, description: NetatmoSensorEntityDescription) -> None: ...

class NetatmoClimateBatterySensor(NetatmoLegacySensor):
    entity_description: NetatmoSensorEntityDescription
    device: pyatmo.modules.NRV
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice, description: NetatmoSensorEntityDescription) -> None: ...
    _attr_available: bool
    _attr_native_value: Incomplete
    @callback
    def async_update_callback(self) -> None: ...

class NetatmoSensor(NetatmoBaseSensor):
    entity_description: NetatmoSensorEntityDescription
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice, description: NetatmoSensorEntityDescription) -> None: ...
    _attr_available: bool
    _attr_native_value: Incomplete
    @callback
    def async_update_callback(self) -> None: ...

class NetatmoRoomSensor(NetatmoRoomEntity, SensorEntity):
    entity_description: NetatmoSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, netatmo_room: NetatmoRoom, description: NetatmoSensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def async_update_callback(self) -> None: ...

class NetatmoPublicSensor(NetatmoBaseEntity, SensorEntity):
    entity_description: NetatmoPublicWeatherSensorEntityDescription
    _signal_name: Incomplete
    _station: Incomplete
    area: Incomplete
    _mode: Incomplete
    _show_on_map: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, data_handler: NetatmoDataHandler, area: NetatmoArea, description: NetatmoPublicWeatherSensorEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_config_update_callback(self, area: NetatmoArea) -> None: ...
    _attr_available: bool
    _attr_native_value: Incomplete
    @callback
    def async_update_callback(self) -> None: ...
