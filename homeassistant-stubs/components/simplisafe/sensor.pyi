from . import SimpliSafe as SimpliSafe, SimpliSafeEntity as SimpliSafeEntity
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from simplipy.device.sensor.v3 import SensorV3 as SensorV3
from simplipy.system.v3 import SystemV3 as SystemV3
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SimplisafeFreezeSensor(SimpliSafeEntity, SensorEntity):
    _attr_device_class: Any
    _attr_native_unit_of_measurement: Any
    _attr_state_class: Any
    _device: Any
    def __init__(self, simplisafe: SimpliSafe, system: SystemV3, sensor: SensorV3) -> None: ...
    _attr_native_value: Any
    def async_update_from_rest_api(self) -> None: ...
