from . import DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.sensor import RestoreSensor as RestoreSensor, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, ENERGY_MEGA_WATT_HOUR as ENERGY_MEGA_WATT_HOUR, PERCENTAGE as PERCENTAGE, POWER_WATT as POWER_WATT, TEMP_CELSIUS as TEMP_CELSIUS, VOLUME_CUBIC_FEET as VOLUME_CUBIC_FEET, VOLUME_CUBIC_METERS as VOLUME_CUBIC_METERS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, StateType as StateType

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DemoSensor(SensorEntity):
    _attr_should_poll: bool
    _attr_device_class: Incomplete
    _attr_name: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_native_value: Incomplete
    _attr_state_class: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, unique_id: str, name: str, state: StateType, device_class: SensorDeviceClass, state_class: Union[SensorStateClass, None], unit_of_measurement: Union[str, None], battery: StateType) -> None: ...

class DemoSumSensor(RestoreSensor):
    _attr_should_poll: bool
    _attr_native_value: float
    entity_id: Incomplete
    _attr_device_class: Incomplete
    _attr_name: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    _attr_unique_id: Incomplete
    _five_minute_increase: Incomplete
    _attr_device_info: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, unique_id: str, name: str, five_minute_increase: float, device_class: SensorDeviceClass, state_class: Union[SensorStateClass, None], unit_of_measurement: Union[str, None], battery: StateType, suggested_entity_id: str) -> None: ...
    def _async_bump_sum(self, now: datetime) -> None: ...
    async def async_added_to_hass(self) -> None: ...
