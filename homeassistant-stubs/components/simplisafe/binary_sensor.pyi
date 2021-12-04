from . import SimpliSafe as SimpliSafe, SimpliSafeEntity as SimpliSafeEntity
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_DOOR as DEVICE_CLASS_DOOR, DEVICE_CLASS_GAS as DEVICE_CLASS_GAS, DEVICE_CLASS_MOISTURE as DEVICE_CLASS_MOISTURE, DEVICE_CLASS_MOTION as DEVICE_CLASS_MOTION, DEVICE_CLASS_SAFETY as DEVICE_CLASS_SAFETY, DEVICE_CLASS_SMOKE as DEVICE_CLASS_SMOKE
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ENTITY_CATEGORY_DIAGNOSTIC as ENTITY_CATEGORY_DIAGNOSTIC
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from simplipy.device.sensor.v3 import SensorV3 as SensorV3
from simplipy.system.v3 import SystemV3 as SystemV3
from typing import Any

SUPPORTED_BATTERY_SENSOR_TYPES: Any
TRIGGERED_SENSOR_TYPES: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TriggeredBinarySensor(SimpliSafeEntity, BinarySensorEntity):
    _attr_device_class: Any
    _device: Any
    def __init__(self, simplisafe: SimpliSafe, system: SystemV3, sensor: SensorV3, device_class: str) -> None: ...
    _attr_is_on: Any
    def async_update_from_rest_api(self) -> None: ...

class BatteryBinarySensor(SimpliSafeEntity, BinarySensorEntity):
    _attr_device_class: Any
    _attr_entity_category: Any
    _attr_name: Any
    _attr_unique_id: Any
    _device: Any
    def __init__(self, simplisafe: SimpliSafe, system: SystemV3, sensor: SensorV3) -> None: ...
    _attr_is_on: Any
    def async_update_from_rest_api(self) -> None: ...
