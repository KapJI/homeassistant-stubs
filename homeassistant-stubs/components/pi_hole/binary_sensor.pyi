from . import PiHoleEntity as PiHoleEntity
from .const import BINARY_SENSOR_TYPES as BINARY_SENSOR_TYPES, BINARY_SENSOR_TYPES_STATISTICS_ONLY as BINARY_SENSOR_TYPES_STATISTICS_ONLY, CONF_STATISTICS_ONLY as CONF_STATISTICS_ONLY, DATA_KEY_API as DATA_KEY_API, DATA_KEY_COORDINATOR as DATA_KEY_COORDINATOR, PiHoleBinarySensorEntityDescription as PiHoleBinarySensorEntityDescription
from hole import Hole as Hole
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PiHoleBinarySensor(PiHoleEntity, BinarySensorEntity):
    entity_description: PiHoleBinarySensorEntityDescription
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, api: Hole, coordinator: DataUpdateCoordinator, name: str, server_unique_id: str, description: PiHoleBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...
