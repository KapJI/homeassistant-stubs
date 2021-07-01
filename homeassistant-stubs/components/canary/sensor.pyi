from .const import DATA_COORDINATOR as DATA_COORDINATOR, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER
from .coordinator import CanaryDataUpdateCoordinator as CanaryDataUpdateCoordinator
from .model import SensorTypeItem as SensorTypeItem
from canary.api import Device as Device, Location as Location
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_SIGNAL_STRENGTH as DEVICE_CLASS_SIGNAL_STRENGTH, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Final

SENSOR_VALUE_PRECISION: Final[int]
ATTR_AIR_QUALITY: Final[str]
CANARY_PRO: Final[str]
CANARY_FLEX: Final[str]
SENSOR_TYPES: Final[list[SensorTypeItem]]
STATE_AIR_QUALITY_NORMAL: Final[str]
STATE_AIR_QUALITY_ABNORMAL: Final[str]
STATE_AIR_QUALITY_VERY_ABNORMAL: Final[str]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CanarySensor(CoordinatorEntity, SensorEntity):
    coordinator: CanaryDataUpdateCoordinator
    _sensor_type: Any
    _device_id: Any
    _device_name: Any
    _device_type_name: Any
    _name: Any
    _canary_type: Any
    def __init__(self, coordinator: CanaryDataUpdateCoordinator, sensor_type: SensorTypeItem, location: Location, device: Device) -> None: ...
    @property
    def reading(self) -> Union[float, None]: ...
    @property
    def name(self) -> str: ...
    @property
    def state(self) -> Union[float, None]: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def device_class(self) -> Union[str, None]: ...
    @property
    def icon(self) -> Union[str, None]: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, str], None]: ...
