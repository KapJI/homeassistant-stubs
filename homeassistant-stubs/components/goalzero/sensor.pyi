from . import YetiEntity as YetiEntity
from .const import DATA_KEY_API as DATA_KEY_API, DATA_KEY_COORDINATOR as DATA_KEY_COORDINATOR, DOMAIN as DOMAIN
from goalzero import Yeti as Yeti
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, ELECTRIC_CURRENT_AMPERE as ELECTRIC_CURRENT_AMPERE, ELECTRIC_POTENTIAL_VOLT as ELECTRIC_POTENTIAL_VOLT, ENERGY_WATT_HOUR as ENERGY_WATT_HOUR, PERCENTAGE as PERCENTAGE, POWER_WATT as POWER_WATT, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, TEMP_CELSIUS as TEMP_CELSIUS, TIME_MINUTES as TIME_MINUTES, TIME_SECONDS as TIME_SECONDS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

SENSOR_TYPES: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class YetiSensor(YetiEntity, SensorEntity):
    _attr_name: Any
    entity_description: Any
    _attr_unique_id: Any
    def __init__(self, api: Yeti, coordinator: DataUpdateCoordinator, name: str, description: SensorEntityDescription, server_unique_id: str) -> None: ...
    @property
    def native_value(self) -> StateType: ...
