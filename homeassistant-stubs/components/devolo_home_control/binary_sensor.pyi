from .const import DOMAIN as DOMAIN
from .devolo_device import DevoloDeviceEntity as DevoloDeviceEntity
from devolo_home_control_api.devices.zwave import Zwave as Zwave
from devolo_home_control_api.homecontrol import HomeControl as HomeControl
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, DEVICE_CLASS_DOOR as DEVICE_CLASS_DOOR, DEVICE_CLASS_HEAT as DEVICE_CLASS_HEAT, DEVICE_CLASS_MOISTURE as DEVICE_CLASS_MOISTURE, DEVICE_CLASS_MOTION as DEVICE_CLASS_MOTION, DEVICE_CLASS_PROBLEM as DEVICE_CLASS_PROBLEM, DEVICE_CLASS_SAFETY as DEVICE_CLASS_SAFETY, DEVICE_CLASS_SMOKE as DEVICE_CLASS_SMOKE
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

DEVICE_CLASS_MAPPING: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloBinaryDeviceEntity(DevoloDeviceEntity, BinarySensorEntity):
    _binary_sensor_property: Any
    _attr_device_class: Any
    _value: Any
    _attr_entity_registry_enabled_default: bool
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str) -> None: ...
    @property
    def is_on(self) -> bool: ...

class DevoloRemoteControl(DevoloDeviceEntity, BinarySensorEntity):
    _remote_control_property: Any
    _key: Any
    _attr_is_on: bool
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str, key: int) -> None: ...
    def _sync(self, message: tuple) -> None: ...
