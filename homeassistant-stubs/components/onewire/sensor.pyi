from .const import DEVICE_KEYS_0_3 as DEVICE_KEYS_0_3, DEVICE_KEYS_A_B as DEVICE_KEYS_A_B, DOMAIN as DOMAIN, OPTION_ENTRY_DEVICE_OPTIONS as OPTION_ENTRY_DEVICE_OPTIONS, OPTION_ENTRY_SENSOR_PRECISION as OPTION_ENTRY_SENSOR_PRECISION, PRECISION_MAPPING_FAMILY_28 as PRECISION_MAPPING_FAMILY_28, READ_MODE_FLOAT as READ_MODE_FLOAT, READ_MODE_INT as READ_MODE_INT
from .onewire_entities import OneWireEntity as OneWireEntity, OneWireEntityDescription as OneWireEntityDescription
from .onewirehub import OneWireHub as OneWireHub
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from types import MappingProxyType
from typing import Any

class OneWireSensorEntityDescription(OneWireEntityDescription, SensorEntityDescription):
    override_key: Callable[[str, Mapping[str, Any]], str] | None
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, read_mode, override_key) -> None: ...

def _get_sensor_precision_family_28(device_id: str, options: Mapping[str, Any]) -> str: ...

SIMPLE_TEMPERATURE_SENSOR_DESCRIPTION: Incomplete
_LOGGER: Incomplete
DEVICE_SENSORS: dict[str, tuple[OneWireSensorEntityDescription, ...]]
HOBBYBOARD_EF: dict[str, tuple[OneWireSensorEntityDescription, ...]]
EDS_SENSORS: dict[str, tuple[OneWireSensorEntityDescription, ...]]

def get_sensor_types(device_sub_type: str) -> dict[str, tuple[OneWireSensorEntityDescription, ...]]: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def get_entities(onewire_hub: OneWireHub, options: MappingProxyType[str, Any]) -> list[OneWireSensor]: ...

class OneWireSensor(OneWireEntity, SensorEntity):
    entity_description: OneWireSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...
