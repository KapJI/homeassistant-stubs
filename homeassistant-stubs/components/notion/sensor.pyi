from . import NotionEntity as NotionEntity
from .const import DATA_COORDINATOR as DATA_COORDINATOR, DOMAIN as DOMAIN, LOGGER as LOGGER, SENSOR_TEMPERATURE as SENSOR_TEMPERATURE
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

SENSOR_TYPES: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NotionSensor(NotionEntity, SensorEntity):
    _attr_unit_of_measurement: Any
    def __init__(self, coordinator: DataUpdateCoordinator, task_id: str, sensor_id: str, bridge_id: str, system_id: str, name: str, device_class: str, unit: str) -> None: ...
    _attr_state: Any
    def _async_update_from_latest_data(self) -> None: ...
