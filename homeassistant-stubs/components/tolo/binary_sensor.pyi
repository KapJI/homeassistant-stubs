from . import ToloSaunaCoordinatorEntity as ToloSaunaCoordinatorEntity, ToloSaunaUpdateCoordinator as ToloSaunaUpdateCoordinator
from .const import DOMAIN as DOMAIN
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ToloFlowInBinarySensor(ToloSaunaCoordinatorEntity, BinarySensorEntity):
    _attr_entity_category: Any
    _attr_name: str
    _attr_device_class: Any
    _attr_icon: str
    _attr_unique_id: Any
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ConfigEntry) -> None: ...
    @property
    def is_on(self) -> bool: ...

class ToloFlowOutBinarySensor(ToloSaunaCoordinatorEntity, BinarySensorEntity):
    _attr_entity_category: Any
    _attr_name: str
    _attr_device_class: Any
    _attr_icon: str
    _attr_unique_id: Any
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ConfigEntry) -> None: ...
    @property
    def is_on(self) -> bool: ...
