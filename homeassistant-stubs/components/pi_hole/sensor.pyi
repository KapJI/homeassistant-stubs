from . import PiHoleEntity as PiHoleEntity
from .const import ATTR_BLOCKED_DOMAINS as ATTR_BLOCKED_DOMAINS, DATA_KEY_API as DATA_KEY_API, DATA_KEY_COORDINATOR as DATA_KEY_COORDINATOR, PiHoleSensorEntityDescription as PiHoleSensorEntityDescription, SENSOR_TYPES as SENSOR_TYPES
from _typeshed import Incomplete
from hole import Hole as Hole
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PiHoleSensor(PiHoleEntity, SensorEntity):
    entity_description: PiHoleSensorEntityDescription
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, api: Hole, coordinator: DataUpdateCoordinator, name: str, server_unique_id: str, description: PiHoleSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Any: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
