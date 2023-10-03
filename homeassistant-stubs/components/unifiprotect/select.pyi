from .const import DISPATCH_ADOPT as DISPATCH_ADOPT, DOMAIN as DOMAIN, TYPE_EMPTY_VALUE as TYPE_EMPTY_VALUE
from .data import ProtectData as ProtectData
from .entity import ProtectDeviceEntity as ProtectDeviceEntity, async_all_device_entities as async_all_device_entities
from .models import PermRequired as PermRequired, ProtectSetableKeysMixin as ProtectSetableKeysMixin, T as T
from .utils import async_get_light_motion_current as async_get_light_motion_current
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from enum import Enum
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyunifiprotect.api import ProtectApiClient as ProtectApiClient
from pyunifiprotect.data import Camera, Doorlock, Light, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel, ProtectModelWithId as ProtectModelWithId, Sensor, Viewer
from typing import Any, Final

_LOGGER: Incomplete
_KEY_LIGHT_MOTION: str
INFRARED_MODES: Incomplete
CHIME_TYPES: Incomplete
MOUNT_TYPES: Incomplete
LIGHT_MODE_MOTION: str
LIGHT_MODE_MOTION_DARK: str
LIGHT_MODE_DARK: str
LIGHT_MODE_OFF: str
LIGHT_MODES: Incomplete
LIGHT_MODE_TO_SETTINGS: Incomplete
MOTION_MODE_TO_LIGHT_MODE: Incomplete
DEVICE_RECORDING_MODES: Incomplete
DEVICE_CLASS_LCD_MESSAGE: Final[str]

class ProtectSelectEntityDescription(ProtectSetableKeysMixin[T], SelectEntityDescription):
    ufp_options: list[dict[str, Any]] | None
    ufp_options_fn: Callable[[ProtectApiClient], list[dict[str, Any]]] | None
    ufp_enum_type: type[Enum] | None
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, options, ufp_required_field, ufp_value, ufp_value_fn, ufp_enabled, ufp_perm, ufp_set_method, ufp_set_method_fn, ufp_options, ufp_options_fn, ufp_enum_type) -> None: ...

def _get_viewer_options(api: ProtectApiClient) -> list[dict[str, Any]]: ...
def _get_doorbell_options(api: ProtectApiClient) -> list[dict[str, Any]]: ...
def _get_paired_camera_options(api: ProtectApiClient) -> list[dict[str, Any]]: ...
def _get_viewer_current(obj: Viewer) -> str: ...
def _get_doorbell_current(obj: Camera) -> str | None: ...
async def _set_light_mode(obj: Light, mode: str) -> None: ...
async def _set_paired_camera(obj: Light | Sensor | Doorlock, camera_id: str) -> None: ...
async def _set_doorbell_message(obj: Camera, message: str) -> None: ...
async def _set_liveview(obj: Viewer, liveview_id: str) -> None: ...

CAMERA_SELECTS: tuple[ProtectSelectEntityDescription, ...]
LIGHT_SELECTS: tuple[ProtectSelectEntityDescription, ...]
SENSE_SELECTS: tuple[ProtectSelectEntityDescription, ...]
DOORLOCK_SELECTS: tuple[ProtectSelectEntityDescription, ...]
VIEWER_SELECTS: tuple[ProtectSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProtectSelects(ProtectDeviceEntity, SelectEntity):
    device: Camera | Light | Viewer
    entity_description: ProtectSelectEntityDescription
    _attr_name: Incomplete
    def __init__(self, data: ProtectData, device: Camera | Light | Viewer, description: ProtectSelectEntityDescription) -> None: ...
    _attr_current_option: Incomplete
    def _async_update_device_from_protect(self, device: ProtectModelWithId) -> None: ...
    _attr_options: Incomplete
    _hass_to_unifi_options: Incomplete
    _unifi_to_hass_options: Incomplete
    def _async_set_options(self, data: ProtectData, description: ProtectSelectEntityDescription) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
    def _async_updated_event(self, device: ProtectModelWithId) -> None: ...
