from .const import CONF_NAMES as CONF_NAMES, CONF_TYPE_OWSERVER as CONF_TYPE_OWSERVER, CONF_TYPE_SYSBUS as CONF_TYPE_SYSBUS, DOMAIN as DOMAIN, READ_MODE_FLOAT as READ_MODE_FLOAT, READ_MODE_INT as READ_MODE_INT
from .onewire_entities import OneWireBaseEntity as OneWireBaseEntity, OneWireEntityDescription as OneWireEntityDescription, OneWireProxyEntity as OneWireProxyEntity
from .onewirehub import OneWireHub as OneWireHub
from homeassistant.components.onewire.model import OWDirectDeviceDescription as OWDirectDeviceDescription, OWServerDeviceDescription as OWServerDeviceDescription
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_TYPE as CONF_TYPE, ELECTRIC_POTENTIAL_VOLT as ELECTRIC_POTENTIAL_VOLT, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, PRESSURE_CBAR as PRESSURE_CBAR, PRESSURE_MBAR as PRESSURE_MBAR, TEMP_CELSIUS as TEMP_CELSIUS
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
HOBBYBOARD_EF: dict[str, tuple[OneWireSensorEntityDescription, ...]]
EDS_SENSORS: dict[str, tuple[OneWireSensorEntityDescription, ...]]

def get_sensor_types(device_sub_type: str) -> dict[str, tuple[OneWireSensorEntityDescription, ...]]: ...
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
