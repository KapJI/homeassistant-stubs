from .const import CONF_MOUNT_DIR as CONF_MOUNT_DIR, CONF_NAMES as CONF_NAMES, CONF_TYPE_OWSERVER as CONF_TYPE_OWSERVER, CONF_TYPE_SYSBUS as CONF_TYPE_SYSBUS, DEFAULT_OWSERVER_PORT as DEFAULT_OWSERVER_PORT, DEFAULT_SYSBUS_MOUNT_DIR as DEFAULT_SYSBUS_MOUNT_DIR, DOMAIN as DOMAIN, SENSOR_TYPE_COUNT as SENSOR_TYPE_COUNT, SENSOR_TYPE_CURRENT as SENSOR_TYPE_CURRENT, SENSOR_TYPE_HUMIDITY as SENSOR_TYPE_HUMIDITY, SENSOR_TYPE_ILLUMINANCE as SENSOR_TYPE_ILLUMINANCE, SENSOR_TYPE_MOISTURE as SENSOR_TYPE_MOISTURE, SENSOR_TYPE_PRESSURE as SENSOR_TYPE_PRESSURE, SENSOR_TYPE_TEMPERATURE as SENSOR_TYPE_TEMPERATURE, SENSOR_TYPE_VOLTAGE as SENSOR_TYPE_VOLTAGE, SENSOR_TYPE_WETNESS as SENSOR_TYPE_WETNESS
from .model import DeviceComponentDescription as DeviceComponentDescription
from .onewire_entities import OneWireBaseEntity as OneWireBaseEntity, OneWireProxyEntity as OneWireProxyEntity
from .onewirehub import OneWireHub as OneWireHub
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType, StateType as StateType
from pi1wire import OneWireInterface as OneWireInterface
from types import MappingProxyType
from typing import Any

_LOGGER: Any
DEVICE_SENSORS: dict[str, list[DeviceComponentDescription]]
DEVICE_SUPPORT_SYSBUS: Any
HOBBYBOARD_EF: dict[str, list[DeviceComponentDescription]]
EDS_SENSORS: dict[str, list[DeviceComponentDescription]]

def get_sensor_types(device_sub_type: str) -> dict[str, Any]: ...
async def async_setup_platform(hass: HomeAssistant, config: dict[str, Any], async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def get_entities(onewirehub: OneWireHub, config: MappingProxyType[str, Any]) -> list[OneWireBaseEntity]: ...

class OneWireSensor(OneWireBaseEntity, SensorEntity):
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...

class OneWireProxySensor(OneWireProxyEntity, OneWireSensor):
    @property
    def state(self) -> StateType: ...

class OneWireDirectSensor(OneWireSensor):
    _owsensor: Any
    def __init__(self, name: str, device_file: str, device_info: DeviceInfo, owsensor: OneWireInterface) -> None: ...
    @property
    def state(self) -> StateType: ...
    async def get_temperature(self) -> float: ...
    _value_raw: Any
    _state: Any
    async def async_update(self) -> None: ...
