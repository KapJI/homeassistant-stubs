from . import EfergyEntity as EfergyEntity
from .const import CONF_CURRENT_VALUES as CONF_CURRENT_VALUES, DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, POWER_WATT as POWER_WATT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.typing import StateType as StateType
from pyefergy import Efergy as Efergy
from typing import Any

SENSOR_TYPES: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: entity_platform.AddEntitiesCallback) -> None: ...

class EfergySensor(EfergyEntity, SensorEntity):
    entity_description: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_native_unit_of_measurement: Any
    sid: Any
    period: Any
    def __init__(self, api: Efergy, description: SensorEntityDescription, server_unique_id: str, period: Union[str, None] = ..., currency: Union[str, None] = ..., sid: Union[int, None] = ...) -> None: ...
    _attr_native_value: Any
    _attr_available: bool
    async def async_update(self) -> None: ...
