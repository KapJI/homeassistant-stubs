from . import PiHoleEntity as PiHoleEntity
from .const import ATTR_BLOCKED_DOMAINS as ATTR_BLOCKED_DOMAINS, DATA_KEY_API as DATA_KEY_API, DATA_KEY_COORDINATOR as DATA_KEY_COORDINATOR, SENSOR_DICT as SENSOR_DICT, SENSOR_LIST as SENSOR_LIST
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
    _condition: Any
    _condition_name: Any
    _unit_of_measurement: Any
    _icon: Any
    def __init__(self, api: Hole, coordinator: DataUpdateCoordinator, name: str, sensor_name: str, server_unique_id: str) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def icon(self) -> str: ...
    @property
    def unit_of_measurement(self) -> str: ...
    @property
    def state(self) -> Any: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
