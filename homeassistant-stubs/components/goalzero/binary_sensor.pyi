from . import YetiEntity as YetiEntity
from .const import DATA_KEY_API as DATA_KEY_API, DATA_KEY_COORDINATOR as DATA_KEY_COORDINATOR, DOMAIN as DOMAIN
from goalzero import Yeti as Yeti
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

PARALLEL_UPDATES: int
BINARY_SENSOR_TYPES: tuple[BinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class YetiBinarySensor(YetiEntity, BinarySensorEntity):
    entity_description: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, api: Yeti, coordinator: DataUpdateCoordinator, name: str, description: BinarySensorEntityDescription, server_unique_id: str) -> None: ...
    @property
    def is_on(self) -> bool: ...
