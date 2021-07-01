from . import AirlyDataUpdateCoordinator as AirlyDataUpdateCoordinator
from .const import ATTRIBUTION as ATTRIBUTION, ATTR_ADVICE as ATTR_ADVICE, ATTR_API_ADVICE as ATTR_API_ADVICE, ATTR_API_CAQI as ATTR_API_CAQI, ATTR_API_CAQI_DESCRIPTION as ATTR_API_CAQI_DESCRIPTION, ATTR_API_CAQI_LEVEL as ATTR_API_CAQI_LEVEL, ATTR_API_PM10 as ATTR_API_PM10, ATTR_API_PM25 as ATTR_API_PM25, ATTR_DESCRIPTION as ATTR_DESCRIPTION, ATTR_LABEL as ATTR_LABEL, ATTR_LEVEL as ATTR_LEVEL, ATTR_LIMIT as ATTR_LIMIT, ATTR_PERCENT as ATTR_PERCENT, ATTR_UNIT as ATTR_UNIT, ATTR_VALUE as ATTR_VALUE, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, SENSOR_TYPES as SENSOR_TYPES, SUFFIX_LIMIT as SUFFIX_LIMIT, SUFFIX_PERCENT as SUFFIX_PERCENT
from homeassistant.components.sensor import ATTR_STATE_CLASS as ATTR_STATE_CLASS, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ICON as ATTR_ICON, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirlySensor(CoordinatorEntity, SensorEntity):
    coordinator: AirlyDataUpdateCoordinator
    _description: Any
    _attr_device_class: Any
    _attr_icon: Any
    _attr_name: Any
    _attr_state_class: Any
    _attr_unique_id: Any
    _attr_unit_of_measurement: Any
    _attrs: Any
    kind: Any
    def __init__(self, coordinator: AirlyDataUpdateCoordinator, name: str, kind: str) -> None: ...
    @property
    def state(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def device_info(self) -> DeviceInfo: ...
