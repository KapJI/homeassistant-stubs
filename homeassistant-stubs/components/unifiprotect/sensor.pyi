from .data import ProtectData as ProtectData, ProtectDeviceType as ProtectDeviceType, UFPConfigEntry as UFPConfigEntry
from .entity import BaseProtectEntity as BaseProtectEntity, EventEntityMixin as EventEntityMixin, ProtectDeviceEntity as ProtectDeviceEntity, ProtectNVREntity as ProtectNVREntity, async_all_device_entities as async_all_device_entities
from .models import PermRequired as PermRequired, ProtectEntityDescription as ProtectEntityDescription, ProtectEventMixin as ProtectEventMixin, T as T
from .utils import async_get_light_motion_current as async_get_light_motion_current
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Sequence
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfDataRate as UnitOfDataRate, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfInformation as UnitOfInformation, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from uiprotect.data import Camera, ModelType, NVR, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel, ProtectDeviceModel as ProtectDeviceModel, Sensor

_LOGGER: Incomplete
OBJECT_TYPE_NONE: str

@dataclass(frozen=True, kw_only=True)
class ProtectSensorEntityDescription(ProtectEntityDescription[T], SensorEntityDescription):
    precision: int | None = ...
    def __post_init__(self) -> None: ...
    def _rounded_value(self, precision: int, getter: Callable[[T], Any], obj: T) -> Any: ...
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., ufp_required_field=..., ufp_value=..., ufp_value_fn=..., ufp_enabled=..., ufp_perm=..., has_required=..., get_ufp_enabled=..., precision=...) -> None: ...

@dataclass(frozen=True, kw_only=True)
class ProtectSensorEventEntityDescription(ProtectEventMixin[T], SensorEntityDescription):
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., ufp_required_field=..., ufp_value=..., ufp_value_fn=..., ufp_enabled=..., ufp_perm=..., has_required=..., get_ufp_enabled=..., ufp_event_obj=..., ufp_obj_type=...) -> None: ...

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
LICENSE_PLATE_EVENT_SENSORS: tuple[ProtectSensorEventEntityDescription, ...]
LIGHT_SENSORS: tuple[ProtectSensorEntityDescription, ...]
MOTION_TRIP_SENSORS: tuple[ProtectSensorEntityDescription, ...]
CHIME_SENSORS: tuple[ProtectSensorEntityDescription, ...]
VIEWER_SENSORS: tuple[ProtectSensorEntityDescription, ...]
_MODEL_DESCRIPTIONS: dict[ModelType, Sequence[ProtectEntityDescription]]

async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _async_event_entities(data: ProtectData, ufp_device: Camera | None = None) -> list[ProtectDeviceEntity]: ...
def _async_nvr_entities(data: ProtectData) -> list[BaseProtectEntity]: ...

class BaseProtectSensor(BaseProtectEntity, SensorEntity):
    entity_description: ProtectSensorEntityDescription
    _state_attrs: Incomplete
    _attr_native_value: Incomplete
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...

class ProtectDeviceSensor(BaseProtectSensor, ProtectDeviceEntity): ...
class ProtectNVRSensor(BaseProtectSensor, ProtectNVREntity): ...

class ProtectEventSensor(EventEntityMixin, SensorEntity):
    entity_description: ProtectSensorEventEntityDescription
    _state_attrs: Incomplete

class ProtectLicensePlateEventSensor(ProtectEventSensor):
    device: Camera
    _attr_native_value: Incomplete
    _attr_extra_state_attributes: Incomplete
    def _set_event_done(self) -> None: ...
    _event: Incomplete
    _event_end: Incomplete
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...
