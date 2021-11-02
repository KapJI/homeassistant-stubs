from .const import CONF_APPTOKEN as CONF_APPTOKEN, CONF_CURRENT_VALUES as CONF_CURRENT_VALUES, DATA_KEY_API as DATA_KEY_API, DOMAIN as DOMAIN
from homeassistant.components.efergy import EfergyEntity as EfergyEntity
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, STATE_CLASS_TOTAL_INCREASING as STATE_CLASS_TOTAL_INCREASING, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_CURRENCY as CONF_CURRENCY, CONF_MONITORED_VARIABLES as CONF_MONITORED_VARIABLES, CONF_TYPE as CONF_TYPE, DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_MONETARY as DEVICE_CLASS_MONETARY, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, POWER_WATT as POWER_WATT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from pyefergy import Efergy as Efergy
from typing import Any

_LOGGER: Any
SENSOR_TYPES: tuple[SensorEntityDescription, ...]
TYPES_SCHEMA: Any
SENSORS_SCHEMA: Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: entity_platform.AddEntitiesCallback) -> None: ...

class EfergySensor(EfergyEntity, SensorEntity):
    entity_description: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_native_unit_of_measurement: Any
    sid: Any
    period: Any
    def __init__(self, api: Efergy, description: SensorEntityDescription, server_unique_id: str, period: Union[str, None] = ..., currency: Union[str, None] = ..., sid: str = ...) -> None: ...
    _attr_native_value: Any
    _attr_available: bool
    async def async_update(self) -> None: ...
