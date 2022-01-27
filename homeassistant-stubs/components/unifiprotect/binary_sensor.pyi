from .const import DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .entity import EventThumbnailMixin as EventThumbnailMixin, ProtectDeviceEntity as ProtectDeviceEntity, ProtectNVREntity as ProtectNVREntity, async_all_device_entities as async_all_device_entities
from .models import ProtectRequiredKeysMixin as ProtectRequiredKeysMixin
from .utils import get_nested_attr as get_nested_attr
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LAST_TRIP_TIME as ATTR_LAST_TRIP_TIME, ATTR_MODEL as ATTR_MODEL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyunifiprotect.data import Camera as Camera, Event as Event, Light as Light, NVR as NVR, Sensor
from typing import Any

_LOGGER: Any
_KEY_DOOR: str

class ProtectBinaryEntityDescription(ProtectRequiredKeysMixin, BinarySensorEntityDescription):
    ufp_last_trip_value: Union[str, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, ufp_required_field, ufp_value, ufp_value_fn, ufp_enabled, ufp_last_trip_value) -> None: ...

MOUNT_DEVICE_CLASS_MAP: Any
CAMERA_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
LIGHT_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
SENSE_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
MOTION_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
DOORLOCK_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
DISK_SENSORS: tuple[ProtectBinaryEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _async_motion_entities(data: ProtectData) -> list[ProtectDeviceEntity]: ...
def _async_nvr_entities(data: ProtectData) -> list[ProtectDeviceEntity]: ...

class ProtectDeviceBinarySensor(ProtectDeviceEntity, BinarySensorEntity):
    device: Union[Camera, Light, Sensor]
    entity_description: ProtectBinaryEntityDescription
    _attr_is_on: Any
    _attr_extra_state_attributes: Any
    def _async_update_device_from_protect(self) -> None: ...

class ProtectDiskBinarySensor(ProtectNVREntity, BinarySensorEntity):
    entity_description: ProtectBinaryEntityDescription
    _index: Any
    def __init__(self, data: ProtectData, device: NVR, description: ProtectBinaryEntityDescription, index: int) -> None: ...
    _attr_available: Any
    _attr_is_on: Any
    _attr_extra_state_attributes: Any
    def _async_update_device_from_protect(self) -> None: ...

class ProtectEventBinarySensor(EventThumbnailMixin, ProtectDeviceBinarySensor):
    device: Camera
    def _async_get_event(self) -> Union[Event, None]: ...
