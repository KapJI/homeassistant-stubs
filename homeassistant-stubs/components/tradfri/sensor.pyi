from .base_class import TradfriBaseDevice as TradfriBaseDevice
from .const import CONF_GATEWAY_ID as CONF_GATEWAY_ID, DEVICES as DEVICES, DOMAIN as DOMAIN, KEY_API as KEY_API
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pytradfri.command import Command as Command
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TradfriSensor(TradfriBaseDevice, SensorEntity):
    _attr_device_class: Any
    _attr_native_unit_of_measurement: Any
    _attr_unique_id: Any
    def __init__(self, device: Command, api: Callable[[Union[Command, list[Command]]], Any], gateway_id: str) -> None: ...
    @property
    def native_value(self) -> Union[int, None]: ...
