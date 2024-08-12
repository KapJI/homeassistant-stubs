from .const import DOMAIN as DOMAIN, SIGNAL_EVENTS_CHANGED as SIGNAL_EVENTS_CHANGED, SIGNAL_POSITION_CHANGED as SIGNAL_POSITION_CHANGED
from .entity import Sun as Sun, SunConfigEntry as SunConfigEntry
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import DEGREE as DEGREE, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

ENTITY_ID_SENSOR_FORMAT: Incomplete

@dataclass(kw_only=True, frozen=True)
class SunSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Sun], StateType | datetime]
    signal: str
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn, signal) -> None: ...

SENSOR_TYPES: tuple[SunSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SunConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SunSensor(SensorEntity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _attr_entity_category: Incomplete
    entity_description: SunSensorEntityDescription
    entity_id: Incomplete
    _attr_unique_id: Incomplete
    sun: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, sun: Sun, entity_description: SunSensorEntityDescription, entry_id: str) -> None: ...
    @property
    def native_value(self) -> StateType | datetime: ...
    async def async_added_to_hass(self) -> None: ...
