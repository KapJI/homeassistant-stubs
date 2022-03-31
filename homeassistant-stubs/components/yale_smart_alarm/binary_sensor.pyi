from .const import COORDINATOR as COORDINATOR, DOMAIN as DOMAIN
from .coordinator import YaleDataUpdateCoordinator as YaleDataUpdateCoordinator
from .entity import YaleAlarmEntity as YaleAlarmEntity, YaleEntity as YaleEntity
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SENSOR_TYPES: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class YaleDoorSensor(YaleEntity, BinarySensorEntity):
    _attr_device_class: Any
    @property
    def is_on(self) -> bool: ...

class YaleProblemSensor(YaleAlarmEntity, BinarySensorEntity):
    entity_description: BinarySensorEntityDescription
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: YaleDataUpdateCoordinator, entity_description: BinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
