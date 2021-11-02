from . import SimpliSafe as SimpliSafe, SimpliSafeBaseSensor as SimpliSafeBaseSensor
from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_DOOR as DEVICE_CLASS_DOOR, DEVICE_CLASS_GAS as DEVICE_CLASS_GAS, DEVICE_CLASS_MOISTURE as DEVICE_CLASS_MOISTURE, DEVICE_CLASS_MOTION as DEVICE_CLASS_MOTION, DEVICE_CLASS_SAFETY as DEVICE_CLASS_SAFETY, DEVICE_CLASS_SMOKE as DEVICE_CLASS_SMOKE
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from simplipy.entity import Entity as SimplipyEntity
from simplipy.system.v2 import SystemV2 as SystemV2
from simplipy.system.v3 import SystemV3 as SystemV3
from typing import Any

SUPPORTED_BATTERY_SENSOR_TYPES: Any
TRIGGERED_SENSOR_TYPES: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TriggeredBinarySensor(SimpliSafeBaseSensor, BinarySensorEntity):
    _attr_device_class: Any
    def __init__(self, simplisafe: SimpliSafe, system: Union[SystemV2, SystemV3], sensor: SimplipyEntity, device_class: str) -> None: ...
    _attr_is_on: Any
    def async_update_from_rest_api(self) -> None: ...

class BatteryBinarySensor(SimpliSafeBaseSensor, BinarySensorEntity):
    _attr_device_class: Any
    _attr_unique_id: Any
    def __init__(self, simplisafe: SimpliSafe, system: Union[SystemV2, SystemV3], sensor: SimplipyEntity) -> None: ...
    _attr_is_on: Any
    def async_update_from_rest_api(self) -> None: ...
