from .const import CONF_TYPE_OWSERVER as CONF_TYPE_OWSERVER, CONF_TYPE_SYSBUS as CONF_TYPE_SYSBUS, DEVICE_KEYS_0_3 as DEVICE_KEYS_0_3, DEVICE_KEYS_A_B as DEVICE_KEYS_A_B, DOMAIN as DOMAIN, READ_MODE_FLOAT as READ_MODE_FLOAT, READ_MODE_INT as READ_MODE_INT
from .model import OWDirectDeviceDescription as OWDirectDeviceDescription, OWServerDeviceDescription as OWServerDeviceDescription
from .onewire_entities import OneWireBaseEntity as OneWireBaseEntity, OneWireEntityDescription as OneWireEntityDescription, OneWireProxyEntity as OneWireProxyEntity
from .onewirehub import OneWireHub as OneWireHub
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

class OneWireSensorEntityDescription(OneWireEntityDescription, SensorEntityDescription):
    override_key: Union[str, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, read_mode, override_key) -> None: ...

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
