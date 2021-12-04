from . import ToloSaunaCoordinatorEntity as ToloSaunaCoordinatorEntity, ToloSaunaUpdateCoordinator as ToloSaunaUpdateCoordinator
from .const import DOMAIN as DOMAIN
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, ENTITY_CATEGORY_DIAGNOSTIC as ENTITY_CATEGORY_DIAGNOSTIC, PERCENTAGE as PERCENTAGE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ToloWaterLevelSensor(ToloSaunaCoordinatorEntity, SensorEntity):
    _attr_entity_category: Any
    _attr_name: str
    _attr_icon: str
    _attr_state_class: Any
    _attr_native_unit_of_measurement: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ConfigEntry) -> None: ...
    @property
    def native_value(self) -> int: ...

class ToloTankTemperatureSensor(ToloSaunaCoordinatorEntity, SensorEntity):
    _attr_entity_category: Any
    _attr_name: str
    _attr_device_class: Any
    _attr_state_class: Any
    _attr_native_unit_of_measurement: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ConfigEntry) -> None: ...
    @property
    def native_value(self) -> int: ...
