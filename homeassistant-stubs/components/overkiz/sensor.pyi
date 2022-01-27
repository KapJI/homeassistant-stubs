from . import HomeAssistantOverkizData as HomeAssistantOverkizData
from .const import DOMAIN as DOMAIN, IGNORED_OVERKIZ_DEVICES as IGNORED_OVERKIZ_DEVICES, OVERKIZ_STATE_TO_TRANSLATION as OVERKIZ_STATE_TO_TRANSLATION
from .coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from .entity import OverkizDescriptiveEntity as OverkizDescriptiveEntity, OverkizDeviceClass as OverkizDeviceClass, OverkizEntity as OverkizEntity
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, ENERGY_WATT_HOUR as ENERGY_WATT_HOUR, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, POWER_WATT as POWER_WATT, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, TEMP_CELSIUS as TEMP_CELSIUS, TIME_SECONDS as TIME_SECONDS, VOLUME_FLOW_RATE_CUBIC_METERS_PER_HOUR as VOLUME_FLOW_RATE_CUBIC_METERS_PER_HOUR, VOLUME_LITERS as VOLUME_LITERS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pyoverkiz.types import StateType as OverkizStateType
from typing import Any

class OverkizSensorDescription(SensorEntityDescription):
    native_value: Union[Callable[[OverkizStateType], StateType], None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, native_value) -> None: ...

SENSOR_DESCRIPTIONS: list[OverkizSensorDescription]
SUPPORTED_STATES: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OverkizStateSensor(OverkizDescriptiveEntity, SensorEntity):
    entity_description: OverkizSensorDescription
    @property
    def native_value(self) -> StateType: ...

class OverkizHomeKitSetupCodeSensor(OverkizEntity, SensorEntity):
    _attr_icon: str
    _attr_entity_category: Any
    _attr_name: str
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator) -> None: ...
    @property
    def native_value(self) -> Union[str, None]: ...
    @property
    def device_info(self) -> DeviceInfo: ...
