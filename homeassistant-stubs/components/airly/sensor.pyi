from . import AirlyDataUpdateCoordinator as AirlyDataUpdateCoordinator
from .const import ATTRIBUTION as ATTRIBUTION, ATTR_ADVICE as ATTR_ADVICE, ATTR_API_ADVICE as ATTR_API_ADVICE, ATTR_API_CAQI as ATTR_API_CAQI, ATTR_API_CAQI_DESCRIPTION as ATTR_API_CAQI_DESCRIPTION, ATTR_API_CAQI_LEVEL as ATTR_API_CAQI_LEVEL, ATTR_API_HUMIDITY as ATTR_API_HUMIDITY, ATTR_API_PM1 as ATTR_API_PM1, ATTR_API_PM10 as ATTR_API_PM10, ATTR_API_PM25 as ATTR_API_PM25, ATTR_API_PRESSURE as ATTR_API_PRESSURE, ATTR_API_TEMPERATURE as ATTR_API_TEMPERATURE, ATTR_DESCRIPTION as ATTR_DESCRIPTION, ATTR_LEVEL as ATTR_LEVEL, ATTR_LIMIT as ATTR_LIMIT, ATTR_PERCENT as ATTR_PERCENT, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, SUFFIX_LIMIT as SUFFIX_LIMIT, SUFFIX_PERCENT as SUFFIX_PERCENT, URL as URL
from collections.abc import Callable as Callable
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONF_NAME as CONF_NAME, DEVICE_CLASS_AQI as DEVICE_CLASS_AQI, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_PM1 as DEVICE_CLASS_PM1, DEVICE_CLASS_PM10 as DEVICE_CLASS_PM10, DEVICE_CLASS_PM25 as DEVICE_CLASS_PM25, DEVICE_CLASS_PRESSURE as DEVICE_CLASS_PRESSURE, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, PERCENTAGE as PERCENTAGE, PRESSURE_HPA as PRESSURE_HPA, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

PARALLEL_UPDATES: int

class AirlySensorEntityDescription(SensorEntityDescription):
    value: Callable

SENSOR_TYPES: tuple[AirlySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirlySensor(CoordinatorEntity, SensorEntity):
    coordinator: AirlyDataUpdateCoordinator
    entity_description: AirlySensorEntityDescription
    _attr_device_info: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attrs: Any
    def __init__(self, coordinator: AirlyDataUpdateCoordinator, name: str, description: AirlySensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
