from .const import DATA_SUBSCRIBER as DATA_SUBSCRIBER, DOMAIN as DOMAIN
from .device_info import NestDeviceInfo as NestDeviceInfo
from google_nest_sdm.device import Device as Device
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Any
DEVICE_TYPE_MAP: Any

async def async_setup_sdm_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensorBase(SensorEntity):
    _attr_should_poll: bool
    _attr_state_class: Any
    _device: Any
    _device_info: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, device: Device) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class TemperatureSensor(SensorBase):
    _attr_device_class: Any
    _attr_native_unit_of_measurement: Any
    @property
    def name(self) -> str: ...
    @property
    def native_value(self) -> float: ...

class HumiditySensor(SensorBase):
    _attr_device_class: Any
    _attr_native_unit_of_measurement: Any
    @property
    def name(self) -> str: ...
    @property
    def native_value(self) -> int: ...
