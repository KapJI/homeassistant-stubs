from . import AirlyDataUpdateCoordinator as AirlyDataUpdateCoordinator
from .const import ATTRIBUTION as ATTRIBUTION, ATTR_ADVICE as ATTR_ADVICE, ATTR_API_ADVICE as ATTR_API_ADVICE, ATTR_API_CAQI as ATTR_API_CAQI, ATTR_API_CAQI_DESCRIPTION as ATTR_API_CAQI_DESCRIPTION, ATTR_API_CAQI_LEVEL as ATTR_API_CAQI_LEVEL, ATTR_API_PM10 as ATTR_API_PM10, ATTR_API_PM25 as ATTR_API_PM25, ATTR_DESCRIPTION as ATTR_DESCRIPTION, ATTR_LEVEL as ATTR_LEVEL, ATTR_LIMIT as ATTR_LIMIT, ATTR_PERCENT as ATTR_PERCENT, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, SENSOR_TYPES as SENSOR_TYPES, SUFFIX_LIMIT as SUFFIX_LIMIT, SUFFIX_PERCENT as SUFFIX_PERCENT
from .model import AirlySensorEntityDescription as AirlySensorEntityDescription
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

PARALLEL_UPDATES: int

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
    def state(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
