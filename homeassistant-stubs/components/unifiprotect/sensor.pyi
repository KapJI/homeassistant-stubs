from .const import DISPATCH_ADOPT as DISPATCH_ADOPT, DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .entity import EventEntityMixin as EventEntityMixin, ProtectDeviceEntity as ProtectDeviceEntity, ProtectNVREntity as ProtectNVREntity, async_all_device_entities as async_all_device_entities
from .models import PermRequired as PermRequired, ProtectEventMixin as ProtectEventMixin, ProtectRequiredKeysMixin as ProtectRequiredKeysMixin, T as T
from .utils import async_get_light_motion_current as async_get_light_motion_current
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfDataRate as UnitOfDataRate, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfInformation as UnitOfInformation, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyunifiprotect.data import Camera, NVR, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel, ProtectDeviceModel as ProtectDeviceModel, ProtectModelWithId as ProtectModelWithId, Sensor
from typing import Any

_LOGGER: Incomplete
OBJECT_TYPE_NONE: str

@dataclass
class ProtectSensorEntityDescription(ProtectRequiredKeysMixin[T], SensorEntityDescription):
    precision: int | None = ...
    def get_ufp_value(self, obj: T) -> Any: ...
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, ufp_required_field, ufp_value, ufp_value_fn, ufp_enabled, ufp_perm, precision) -> None: ...

@dataclass
class ProtectSensorEventEntityDescription(ProtectEventMixin[T], SensorEntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, ufp_required_field, ufp_value, ufp_value_fn, ufp_enabled, ufp_perm, ufp_event_obj) -> None: ...

def _get_uptime(obj: ProtectDeviceModel) -> datetime | None: ...
def _get_nvr_recording_capacity(obj: NVR) -> int: ...
def _get_nvr_memory(obj: NVR) -> float | None: ...
def _get_alarm_sound(obj: Sensor) -> str: ...

ALL_DEVICES_SENSORS: tuple[ProtectSensorEntityDescription, ...]
CAMERA_SENSORS: tuple[ProtectSensorEntityDescription, ...]
CAMERA_DISABLED_SENSORS: tuple[ProtectSensorEntityDescription, ...]
SENSE_SENSORS: tuple[ProtectSensorEntityDescription, ...]
DOORLOCK_SENSORS: tuple[ProtectSensorEntityDescription, ...]
NVR_SENSORS: tuple[ProtectSensorEntityDescription, ...]
NVR_DISABLED_SENSORS: tuple[ProtectSensorEntityDescription, ...]
EVENT_SENSORS: tuple[ProtectSensorEventEntityDescription, ...]
LIGHT_SENSORS: tuple[ProtectSensorEntityDescription, ...]
MOTION_TRIP_SENSORS: tuple[ProtectSensorEntityDescription, ...]
CHIME_SENSORS: tuple[ProtectSensorEntityDescription, ...]
VIEWER_SENSORS: tuple[ProtectSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _async_event_entities(data: ProtectData, ufp_device: Camera | None = ...) -> list[ProtectDeviceEntity]: ...
def _async_nvr_entities(data: ProtectData) -> list[ProtectDeviceEntity]: ...

class ProtectDeviceSensor(ProtectDeviceEntity, SensorEntity):
    entity_description: ProtectSensorEntityDescription
    _attr_native_value: Incomplete
    def _async_update_device_from_protect(self, device: ProtectModelWithId) -> None: ...
    def _async_updated_event(self, device: ProtectModelWithId) -> None: ...

class ProtectNVRSensor(ProtectNVREntity, SensorEntity):
    entity_description: ProtectSensorEntityDescription
    _attr_native_value: Incomplete
    def _async_update_device_from_protect(self, device: ProtectModelWithId) -> None: ...
    def _async_updated_event(self, device: ProtectModelWithId) -> None: ...

class ProtectEventSensor(EventEntityMixin, SensorEntity):
    entity_description: ProtectSensorEventEntityDescription
    _attr_native_value: Incomplete
    _event: Incomplete
    _attr_extra_state_attributes: Incomplete
    def _async_update_device_from_protect(self, device: ProtectModelWithId) -> None: ...
