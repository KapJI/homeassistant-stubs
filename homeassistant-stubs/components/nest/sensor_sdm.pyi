from .const import DATA_SUBSCRIBER as DATA_SUBSCRIBER, DOMAIN as DOMAIN
from .device_info import NestDeviceInfo as NestDeviceInfo
from _typeshed import Incomplete
from google_nest_sdm.device import Device as Device
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete
DEVICE_TYPE_MAP: Incomplete

async def async_setup_sdm_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensorBase(SensorEntity):
    _attr_should_poll: bool
    _attr_state_class: Incomplete
    _device: Incomplete
    _device_info: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, device: Device) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class TemperatureSensor(SensorBase):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    @property
    def name(self) -> str: ...
    @property
    def native_value(self) -> float: ...

class HumiditySensor(SensorBase):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    @property
    def name(self) -> str: ...
    @property
    def native_value(self) -> int: ...
