from . import GiosDataUpdateCoordinator as GiosDataUpdateCoordinator
from .const import ATTRIBUTION as ATTRIBUTION, ATTR_AQI as ATTR_AQI, ATTR_INDEX as ATTR_INDEX, ATTR_PM25 as ATTR_PM25, ATTR_STATION as ATTR_STATION, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, SENSOR_TYPES as SENSOR_TYPES
from .model import GiosSensorEntityDescription as GiosSensorEntityDescription
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, ATTR_NAME as ATTR_NAME, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.entity_registry import async_get_registry as async_get_registry
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class GiosSensor(CoordinatorEntity, SensorEntity):
    coordinator: GiosDataUpdateCoordinator
    entity_description: GiosSensorEntityDescription
    _attr_device_info: Any
    _attr_icon: str
    _attr_name: Any
    _attr_unique_id: Any
    _attrs: Any
    def __init__(self, name: str, coordinator: GiosDataUpdateCoordinator, description: GiosSensorEntityDescription) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def state(self) -> StateType: ...

class GiosAqiSensor(GiosSensor):
    @property
    def state(self) -> StateType: ...
    @property
    def available(self) -> bool: ...
