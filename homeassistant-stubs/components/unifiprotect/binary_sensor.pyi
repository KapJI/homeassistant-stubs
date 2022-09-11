from .const import DISPATCH_ADOPT as DISPATCH_ADOPT, DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .entity import EventThumbnailMixin as EventThumbnailMixin, ProtectDeviceEntity as ProtectDeviceEntity, ProtectNVREntity as ProtectNVREntity, async_all_device_entities as async_all_device_entities
from .models import PermRequired as PermRequired, ProtectRequiredKeysMixin as ProtectRequiredKeysMixin
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyunifiprotect.data import Camera, Event as Event, Light as Light, NVR as NVR, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel, ProtectModelWithId as ProtectModelWithId, Sensor
from pyunifiprotect.data.nvr import UOSDisk as UOSDisk

_LOGGER: Incomplete
_KEY_DOOR: str

class ProtectBinaryEntityDescription(ProtectRequiredKeysMixin, BinarySensorEntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, ufp_required_field, ufp_value, ufp_value_fn, ufp_enabled, ufp_perm) -> None: ...

MOUNT_DEVICE_CLASS_MAP: Incomplete
CAMERA_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
LIGHT_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
SENSE_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
MOTION_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
DOORLOCK_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
VIEWER_SENSORS: tuple[ProtectBinaryEntityDescription, ...]
DISK_SENSORS: tuple[ProtectBinaryEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _async_motion_entities(data: ProtectData, ufp_device: Union[ProtectAdoptableDeviceModel, None] = ...) -> list[ProtectDeviceEntity]: ...
def _async_nvr_entities(data: ProtectData) -> list[ProtectDeviceEntity]: ...

class ProtectDeviceBinarySensor(ProtectDeviceEntity, BinarySensorEntity):
    device: Union[Camera, Light, Sensor]
    entity_description: ProtectBinaryEntityDescription
    _attr_is_on: Incomplete
    def _async_update_device_from_protect(self, device: ProtectModelWithId) -> None: ...

class ProtectDiskBinarySensor(ProtectNVREntity, BinarySensorEntity):
    _disk: UOSDisk
    entity_description: ProtectBinaryEntityDescription
    def __init__(self, data: ProtectData, device: NVR, description: ProtectBinaryEntityDescription, disk: UOSDisk) -> None: ...
    _attr_available: bool
    _attr_is_on: Incomplete
    def _async_update_device_from_protect(self, device: ProtectModelWithId) -> None: ...

class ProtectEventBinarySensor(EventThumbnailMixin, ProtectDeviceBinarySensor):
    device: Camera
    def _async_get_event(self) -> Union[Event, None]: ...
