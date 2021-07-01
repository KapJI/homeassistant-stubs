from . import NAMDataUpdateCoordinator as NAMDataUpdateCoordinator
from .const import ATTR_ENABLED as ATTR_ENABLED, ATTR_LABEL as ATTR_LABEL, ATTR_UNIT as ATTR_UNIT, ATTR_UPTIME as ATTR_UPTIME, DOMAIN as DOMAIN, MIGRATION_SENSORS as MIGRATION_SENSORS, SENSORS as SENSORS
from homeassistant.components.sensor import ATTR_STATE_CLASS as ATTR_STATE_CLASS, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_ICON as ATTR_ICON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util.dt import utcnow as utcnow
from typing import Any

PARALLEL_UPDATES: int
_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NAMSensor(CoordinatorEntity, SensorEntity):
    coordinator: NAMDataUpdateCoordinator
    _attr_device_class: Any
    _attr_device_info: Any
    _attr_entity_registry_enabled_default: Any
    _attr_icon: Any
    _attr_name: Any
    _attr_state_class: Any
    _attr_unique_id: Any
    _attr_unit_of_measurement: Any
    sensor_type: Any
    def __init__(self, coordinator: NAMDataUpdateCoordinator, sensor_type: str) -> None: ...
    @property
    def state(self) -> StateType: ...
    @property
    def available(self) -> bool: ...

class NAMSensorUptime(NAMSensor):
    @property
    def state(self) -> str: ...
