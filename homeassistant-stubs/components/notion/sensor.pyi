from . import NotionEntity as NotionEntity
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SENSOR_TEMPERATURE as SENSOR_TEMPERATURE
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SENSOR_DESCRIPTIONS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NotionSensor(NotionEntity, SensorEntity):
    _attr_native_value: Any
    def _async_update_from_latest_data(self) -> None: ...
