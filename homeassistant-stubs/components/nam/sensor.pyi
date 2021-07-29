from . import NAMDataUpdateCoordinator as NAMDataUpdateCoordinator
from .const import ATTR_UPTIME as ATTR_UPTIME, DOMAIN as DOMAIN, MIGRATION_SENSORS as MIGRATION_SENSORS, SENSORS as SENSORS
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
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
    _attr_device_info: Any
    _attr_unique_id: Any
    entity_description: Any
    def __init__(self, coordinator: NAMDataUpdateCoordinator, description: SensorEntityDescription) -> None: ...
    @property
    def state(self) -> StateType: ...
    @property
    def available(self) -> bool: ...

class NAMSensorUptime(NAMSensor):
    @property
    def state(self) -> str: ...
