from .const import DATA_SUBSCRIBER as DATA_SUBSCRIBER, DOMAIN as DOMAIN
from .device_info import NestDeviceInfo as NestDeviceInfo
from google_nest_sdm.device import Device as Device
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, PERCENTAGE as PERCENTAGE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Any
DEVICE_TYPE_MAP: Any

async def async_setup_sdm_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensorBase(SensorEntity):
    _device: Any
    _device_info: Any
    def __init__(self, device: Device) -> None: ...
    @property
    def should_poll(self) -> bool: ...
    @property
    def unique_id(self) -> Union[str, None]: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    async def async_added_to_hass(self) -> None: ...

class TemperatureSensor(SensorBase):
    @property
    def name(self) -> str: ...
    @property
    def state(self) -> float: ...
    @property
    def unit_of_measurement(self) -> str: ...
    @property
    def device_class(self) -> str: ...

class HumiditySensor(SensorBase):
    @property
    def unique_id(self) -> Union[str, None]: ...
    @property
    def name(self) -> str: ...
    @property
    def state(self) -> float: ...
    @property
    def unit_of_measurement(self) -> str: ...
    @property
    def device_class(self) -> str: ...
