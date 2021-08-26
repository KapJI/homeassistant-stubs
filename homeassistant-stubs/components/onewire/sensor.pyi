from .const import CONF_MOUNT_DIR as CONF_MOUNT_DIR, CONF_NAMES as CONF_NAMES, CONF_TYPE_OWSERVER as CONF_TYPE_OWSERVER, CONF_TYPE_SYSBUS as CONF_TYPE_SYSBUS, DOMAIN as DOMAIN, PRESSURE_CBAR as PRESSURE_CBAR, READ_MODE_FLOAT as READ_MODE_FLOAT, READ_MODE_INT as READ_MODE_INT
from .onewire_entities import OneWireBaseEntity as OneWireBaseEntity, OneWireEntityDescription as OneWireEntityDescription, OneWireProxyEntity as OneWireProxyEntity
from .onewirehub import OneWireHub as OneWireHub
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, STATE_CLASS_TOTAL_INCREASING as STATE_CLASS_TOTAL_INCREASING, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, ATTR_NAME as ATTR_NAME, CONF_TYPE as CONF_TYPE, DEVICE_CLASS_CURRENT as DEVICE_CLASS_CURRENT, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_ILLUMINANCE as DEVICE_CLASS_ILLUMINANCE, DEVICE_CLASS_PRESSURE as DEVICE_CLASS_PRESSURE, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_VOLTAGE as DEVICE_CLASS_VOLTAGE, ELECTRIC_CURRENT_AMPERE as ELECTRIC_CURRENT_AMPERE, ELECTRIC_POTENTIAL_VOLT as ELECTRIC_POTENTIAL_VOLT, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, PRESSURE_MBAR as PRESSURE_MBAR, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pi1wire import OneWireInterface as OneWireInterface
from types import MappingProxyType
from typing import Any

class OneWireSensorEntityDescription(OneWireEntityDescription, SensorEntityDescription): ...

SIMPLE_TEMPERATURE_SENSOR_DESCRIPTION: Any
_LOGGER: Any
DEVICE_SENSORS: dict[str, tuple[OneWireSensorEntityDescription, ...]]
DEVICE_SUPPORT_SYSBUS: Any
HOBBYBOARD_EF: dict[str, tuple[OneWireSensorEntityDescription, ...]]
EDS_SENSORS: dict[str, tuple[OneWireSensorEntityDescription, ...]]

def get_sensor_types(device_sub_type: str) -> dict[str, Any]: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def get_entities(onewirehub: OneWireHub, config: MappingProxyType[str, Any]) -> list[SensorEntity]: ...

class OneWireSensor(OneWireBaseEntity, SensorEntity):
    entity_description: OneWireSensorEntityDescription

class OneWireProxySensor(OneWireProxyEntity, OneWireSensor):
    entity_description: OneWireSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...

class OneWireDirectSensor(OneWireSensor):
    _attr_unique_id: Any
    _owsensor: Any
    def __init__(self, description: OneWireSensorEntityDescription, device_id: str, device_info: DeviceInfo, device_file: str, name: str, owsensor: OneWireInterface) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    async def get_temperature(self) -> float: ...
    _value_raw: Any
    _state: Any
    async def async_update(self) -> None: ...
