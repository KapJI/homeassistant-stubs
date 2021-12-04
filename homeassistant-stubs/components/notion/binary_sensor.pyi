from . import NotionEntity as NotionEntity
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SENSOR_BATTERY as SENSOR_BATTERY, SENSOR_DOOR as SENSOR_DOOR, SENSOR_GARAGE_DOOR as SENSOR_GARAGE_DOOR, SENSOR_LEAK as SENSOR_LEAK, SENSOR_MISSING as SENSOR_MISSING, SENSOR_SAFE as SENSOR_SAFE, SENSOR_SLIDING as SENSOR_SLIDING, SENSOR_SMOKE_CO as SENSOR_SMOKE_CO, SENSOR_WINDOW_HINGED_HORIZONTAL as SENSOR_WINDOW_HINGED_HORIZONTAL, SENSOR_WINDOW_HINGED_VERTICAL as SENSOR_WINDOW_HINGED_VERTICAL
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_CONNECTIVITY as DEVICE_CLASS_CONNECTIVITY, DEVICE_CLASS_DOOR as DEVICE_CLASS_DOOR, DEVICE_CLASS_GARAGE_DOOR as DEVICE_CLASS_GARAGE_DOOR, DEVICE_CLASS_MOISTURE as DEVICE_CLASS_MOISTURE, DEVICE_CLASS_SMOKE as DEVICE_CLASS_SMOKE, DEVICE_CLASS_WINDOW as DEVICE_CLASS_WINDOW
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ENTITY_CATEGORY_DIAGNOSTIC as ENTITY_CATEGORY_DIAGNOSTIC
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Literal

class NotionBinarySensorDescriptionMixin:
    on_state: Literal[alarm, critical, leak, not_missing, open]

class NotionBinarySensorDescription(BinarySensorEntityDescription, NotionBinarySensorDescriptionMixin): ...

BINARY_SENSOR_DESCRIPTIONS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NotionBinarySensor(NotionEntity, BinarySensorEntity):
    entity_description: NotionBinarySensorDescription
    _attr_is_on: Any
    def _async_update_from_latest_data(self) -> None: ...
